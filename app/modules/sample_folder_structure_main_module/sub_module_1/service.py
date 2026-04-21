from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.modules.sample_folder_structure_main_module.sub_module_1 import repository
from app.modules.sample_folder_structure_main_module.sub_module_1.schema import (
    SubModuleOneRecordCreate,
    SubModuleOneRecordRead,
    SubModuleOneRecordUpdate,
)


def list_sub_module_one_records(
    db: Session, *, skip: int = 0, limit: int = 100
) -> list[SubModuleOneRecordRead]:
    rows = repository.list_sub_module_one_records(db, skip=skip, limit=limit)
    return [SubModuleOneRecordRead.model_validate(r) for r in rows]


def get_sub_module_one_record(db: Session, record_id: int) -> SubModuleOneRecordRead:
    persisted = repository.get_sub_module_one_record(db, record_id)
    if persisted is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sub-module one record not found",
        )
    return SubModuleOneRecordRead.model_validate(persisted)


def create_sub_module_one_record(
    db: Session, create_data: SubModuleOneRecordCreate
) -> SubModuleOneRecordRead:
    persisted = repository.create_sub_module_one_record(db, create_data)
    return SubModuleOneRecordRead.model_validate(persisted)


def update_sub_module_one_record(
    db: Session, record_id: int, update_data: SubModuleOneRecordUpdate
) -> SubModuleOneRecordRead:
    persisted = repository.get_sub_module_one_record(db, record_id)
    if persisted is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sub-module one record not found",
        )
    persisted = repository.update_sub_module_one_record(
        db, persisted, update_data
    )
    return SubModuleOneRecordRead.model_validate(persisted)


def delete_sub_module_one_record(db: Session, record_id: int) -> None:
    persisted = repository.get_sub_module_one_record(db, record_id)
    if persisted is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sub-module one record not found",
        )
    repository.delete_sub_module_one_record(db, persisted)
