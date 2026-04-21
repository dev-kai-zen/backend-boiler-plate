import secrets
from datetime import timedelta
from typing import Any, Callable, cast

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.config import get_settings
from app.core.db import get_db

router = APIRouter()


@router.get("/")
def read_root() -> dict[str, str]:
    return {"message": f"Connected to the API: {get_settings().app_name}"}


@router.get("/health")
async def health() -> dict[str, str]:
    settings = get_settings()
    return {"status": "Healthy", "service": settings.app_name}


@router.get("/db-ping")
def db_ping(db: Session = Depends(get_db)) -> dict[str, bool | int]:
    one = cast(int, db.execute(text("SELECT 1")).scalar_one())
    return {"ok": True, "select_1": one}

