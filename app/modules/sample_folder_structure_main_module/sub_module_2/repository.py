from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modules.sample_folder_structure_main_module.sub_module_2.model import (
    SubModuleTwoRecord,
)
from app.modules.sample_folder_structure_main_module.sub_module_2.schema import (
    SubModuleTwoRecordCreate,
    SubModuleTwoRecordUpdate,
)


def list_sub_module_two_records(
    db: Session, *, skip: int = 0, limit: int = 100
) -> list[SubModuleTwoRecord]:
    select_statement = (
        select(SubModuleTwoRecord)
        .where(SubModuleTwoRecord.deleted_at.is_(None))
        .offset(skip)
        .limit(limit)
    )
    return list(db.scalars(select_statement).all())


def get_sub_module_two_record(db: Session, record_id: int) -> SubModuleTwoRecord | None:
    persisted = db.get(SubModuleTwoRecord, record_id)
    if persisted is None or persisted.deleted_at is not None:
        return None
    return persisted


def create_sub_module_two_record(
    db: Session, create_data: SubModuleTwoRecordCreate
) -> SubModuleTwoRecord:
    persisted = SubModuleTwoRecord(
        title=create_data.title, description=create_data.description
    )
    db.add(persisted)
    db.commit()
    db.refresh(persisted)
    return persisted


def update_sub_module_two_record(
    db: Session,
    persisted: SubModuleTwoRecord,
    update_data: SubModuleTwoRecordUpdate,
) -> SubModuleTwoRecord:
    for key, value in update_data.model_dump(exclude_unset=True).items():
        setattr(persisted, key, value)
    db.add(persisted)
    db.commit()
    db.refresh(persisted)
    return persisted


def delete_sub_module_two_record(db: Session, persisted: SubModuleTwoRecord) -> None:
    db.delete(persisted)
    db.commit()
