from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.modules.sample_folder_structure_main_module.sub_module_2 import service
from app.modules.sample_folder_structure_main_module.sub_module_2.schema import (
    SubModuleTwoRecordCreate,
    SubModuleTwoRecordRead,
    SubModuleTwoRecordUpdate,
)

router = APIRouter(
    prefix="/sample/sub-module-two/records",
    tags=["sample — sub_module_2"],
)


@router.get("", response_model=list[SubModuleTwoRecordRead])
def list_sub_module_two_records(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
) -> list[SubModuleTwoRecordRead]:
    return service.list_sub_module_two_records(db, skip=skip, limit=limit)


@router.post(
    "",
    response_model=SubModuleTwoRecordRead,
    status_code=status.HTTP_201_CREATED,
)
def create_sub_module_two_record(
    create_data: SubModuleTwoRecordCreate,
    db: Session = Depends(get_db),
) -> SubModuleTwoRecordRead:
    return service.create_sub_module_two_record(db, create_data)


@router.get("/{record_id}", response_model=SubModuleTwoRecordRead)
def get_sub_module_two_record(
    record_id: int, db: Session = Depends(get_db)
) -> SubModuleTwoRecordRead:
    return service.get_sub_module_two_record(db, record_id)


@router.patch("/{record_id}", response_model=SubModuleTwoRecordRead)
def update_sub_module_two_record(
    record_id: int,
    update_data: SubModuleTwoRecordUpdate,
    db: Session = Depends(get_db),
) -> SubModuleTwoRecordRead:
    return service.update_sub_module_two_record(db, record_id, update_data)


@router.delete("/{record_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sub_module_two_record(record_id: int, db: Session = Depends(get_db)) -> None:
    service.delete_sub_module_two_record(db, record_id)
