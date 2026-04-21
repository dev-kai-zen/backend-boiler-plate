from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.modules.sample_folder_structure_main_module.sub_module_2 import repository
from app.modules.sample_folder_structure_main_module.sub_module_2.schema import (
    SubModuleTwoRecordCreate,
    SubModuleTwoRecordRead,
    SubModuleTwoRecordUpdate,
)


def list_sub_module_two_records(
    db: Session, *, skip: int = 0, limit: int = 100
) -> list[SubModuleTwoRecordRead]:
    rows = repository.list_sub_module_two_records(db, skip=skip, limit=limit)
    return [SubModuleTwoRecordRead.model_validate(r) for r in rows]


def get_sub_module_two_record(db: Session, record_id: int) -> SubModuleTwoRecordRead:
    persisted = repository.get_sub_module_two_record(db, record_id)
    if persisted is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sub-module two record not found",
        )
    return SubModuleTwoRecordRead.model_validate(persisted)


def create_sub_module_two_record(
    db: Session, create_data: SubModuleTwoRecordCreate
) -> SubModuleTwoRecordRead:
    persisted = repository.create_sub_module_two_record(db, create_data)
    return SubModuleTwoRecordRead.model_validate(persisted)


def update_sub_module_two_record(
    db: Session, record_id: int, update_data: SubModuleTwoRecordUpdate
) -> SubModuleTwoRecordRead:
    persisted = repository.get_sub_module_two_record(db, record_id)
    if persisted is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sub-module two record not found",
        )
    persisted = repository.update_sub_module_two_record(
        db, persisted, update_data
    )
    return SubModuleTwoRecordRead.model_validate(persisted)


def delete_sub_module_two_record(db: Session, record_id: int) -> None:
    persisted = repository.get_sub_module_two_record(db, record_id)
    if persisted is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Sub-module two record not found",
        )
    repository.delete_sub_module_two_record(db, persisted)
