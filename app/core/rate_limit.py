"""Per-IP fixed-window rate limits (in-process). Stricter bucket for auth routes."""

from __future__ import annotations

from collections.abc import Awaitable, Callable
from threading import Lock
import time

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

from app.core.config import Settings

_lock = Lock()
# logical key (e.g. "auth:127.0.0.1") -> (window_id, count in that window)
_windows: dict[str, tuple[int, int]] = {}


def client_ip(request: Request) -> str:
    forwarded = request.headers.get("x-forwarded-for")
    if forwarded:
        return forwarded.split(",")[0].strip()
    if request.client:
        return request.client.host
    return "unknown"


def _enforce_fixed_window(
    logical_key: str,
    limit: int,
    window_seconds: int,
) -> tuple[bool, int]:
    """Return (allowed, retry_after_seconds)."""
    if limit <= 0:
        return True, 0
    now = int(time.time())
    window_id = now // window_seconds
    with _lock:
        prev = _windows.get(logical_key)
        if prev is None or prev[0] != window_id:
            _windows[logical_key] = (window_id, 1)
            return True, 0
        _wid, count = prev
        count += 1
        _windows[logical_key] = (_wid, count)
        if count > limit:
            retry_after = window_seconds - (now % window_seconds)
            if retry_after <= 0:
                retry_after = window_seconds
            return False, retry_after
        return True, 0


class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, settings: Settings):
        super().__init__(app)
        self._settings = settings

    async def dispatch(
        self,
        request: Request,
        call_next: Callable[[Request], Awaitable[Response]],
    ) -> Response:
        s = self._settings
        if not s.rate_limit_enabled:
            return await call_next(request)

        path = request.url.path
        prefix = s.api_v1_prefix.rstrip("/")
        if not path.startswith(prefix):
            return await call_next(request)

        rel = path.removeprefix(prefix)
        if not rel.startswith("/"):
            rel = f"/{rel}"

        if rel.startswith("/auth"):
            limit = s.rate_limit_auth_per_minute
            bucket = "auth"
        else:
            limit = s.rate_limit_api_per_minute
            bucket = "api"

        ip = client_ip(request)
        logical_key = f"{bucket}:{ip}"

        allowed, retry_after = _enforce_fixed_window(
            logical_key,
            limit,
            s.rate_limit_window_seconds,
        )

        if not allowed:
            return JSONResponse(
                status_code=429,
                content={"detail": "Too many requests"},
                headers={"Retry-After": str(retry_after)},
            )

        return await call_next(request)
