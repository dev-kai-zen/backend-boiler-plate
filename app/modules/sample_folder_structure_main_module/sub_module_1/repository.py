from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modules.sample_folder_structure_main_module.sub_module_1.model import (
    SubModuleOneRecord,
)
from app.modules.sample_folder_structure_main_module.sub_module_1.schema import (
    SubModuleOneRecordCreate,
    SubModuleOneRecordUpdate,
)


def list_sub_module_one_records(
    db: Session, *, skip: int = 0, limit: int = 100
) -> list[SubModuleOneRecord]:
    select_statement = (
        select(SubModuleOneRecord)
        .where(SubModuleOneRecord.deleted_at.is_(None))
        .offset(skip)
        .limit(limit)
    )
    return list(db.scalars(select_statement).all())


def get_sub_module_one_record(db: Session, record_id: int) -> SubModuleOneRecord | None:
    persisted = db.get(SubModuleOneRecord, record_id)
    if persisted is None or persisted.deleted_at is not None:
        return None
    return persisted


def create_sub_module_one_record(
    db: Session, create_data: SubModuleOneRecordCreate
) -> SubModuleOneRecord:
    persisted = SubModuleOneRecord(
        title=create_data.title, description=create_data.description
    )
    db.add(persisted)
    db.commit()
    db.refresh(persisted)
    return persisted


def update_sub_module_one_record(
    db: Session,
    persisted: SubModuleOneRecord,
    update_data: SubModuleOneRecordUpdate,
) -> SubModuleOneRecord:
    for key, value in update_data.model_dump(exclude_unset=True).items():
        setattr(persisted, key, value)
    db.add(persisted)
    db.commit()
    db.refresh(persisted)
    return persisted


def delete_sub_module_one_record(db: Session, persisted: SubModuleOneRecord) -> None:
    db.delete(persisted)
    db.commit()
