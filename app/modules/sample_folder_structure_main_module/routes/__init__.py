from fastapi import APIRouter

from app.modules.sample_folder_structure_main_module.sub_module_1.router import (
    router as sub_module_one_router,
)
from app.modules.sample_folder_structure_main_module.sub_module_2.router import (
    router as sub_module_two_router,
)


def sample_main_module_routes() -> APIRouter:
    router = APIRouter()
    router.include_router(sub_module_one_router)
    router.include_router(sub_module_two_router)
    return router
