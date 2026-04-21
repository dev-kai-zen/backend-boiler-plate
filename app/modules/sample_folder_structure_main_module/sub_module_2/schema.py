from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class SubModuleTwoRecordBase(BaseModel):
    title: str = Field(max_length=200)
    description: str | None = Field(default=None, max_length=2000)


class SubModuleTwoRecordCreate(SubModuleTwoRecordBase):
    pass


class SubModuleTwoRecordUpdate(BaseModel):
    title: str | None = Field(default=None, max_length=200)
    description: str | None = Field(default=None, max_length=2000)


class SubModuleTwoRecordRead(SubModuleTwoRecordBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None
