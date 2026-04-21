from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.modules.sample_folder_structure_main_module.sub_module_1 import service
from app.modules.sample_folder_structure_main_module.sub_module_1.schema import (
    SubModuleOneRecordCreate,
    SubModuleOneRecordRead,
    SubModuleOneRecordUpdate,
)

router = APIRouter(
    prefix="/sample/sub-module-one/records",
    tags=["sample — sub_module_1"],
)


@router.get("", response_model=list[SubModuleOneRecordRead])
def list_sub_module_one_records(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
) -> list[SubModuleOneRecordRead]:
    return service.list_sub_module_one_records(db, skip=skip, limit=limit)


@router.post(
    "",
    response_model=SubModuleOneRecordRead,
    status_code=status.HTTP_201_CREATED,
)
def create_sub_module_one_record(
    create_data: SubModuleOneRecordCreate,
    db: Session = Depends(get_db),
) -> SubModuleOneRecordRead:
    return service.create_sub_module_one_record(db, create_data)


@router.get("/{record_id}", response_model=SubModuleOneRecordRead)
def get_sub_module_one_record(
    record_id: int, db: Session = Depends(get_db)
) -> SubModuleOneRecordRead:
    return service.get_sub_module_one_record(db, record_id)


@router.patch("/{record_id}", response_model=SubModuleOneRecordRead)
def update_sub_module_one_record(
    record_id: int,
    update_data: SubModuleOneRecordUpdate,
    db: Session = Depends(get_db),
) -> SubModuleOneRecordRead:
    return service.update_sub_module_one_record(db, record_id, update_data)


@router.delete("/{record_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sub_module_one_record(record_id: int, db: Session = Depends(get_db)) -> None:
    service.delete_sub_module_one_record(db, record_id)
