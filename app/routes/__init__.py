from fastapi import APIRouter

from app.modules.app_testing.app_testing_routes import router as routes_test_router
from app.modules.sample_folder_structure_main_module.routes import (
    sample_main_module_routes,
)


def register_v1_routes() -> APIRouter:
    router = APIRouter()
    router.include_router(routes_test_router)
    router.include_router(sample_main_module_routes())
    return router
