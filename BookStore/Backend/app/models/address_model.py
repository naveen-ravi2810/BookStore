from sqlmodel import SQLModel, Field, Relationship
from models.base_uuid_model import BaseUUID
from uuid import UUID
from typing import List
from datetime import datetime


class AddressBase(SQLModel):
    recipient_name: str
    house_no_name: str
    street_no_name: str
    city: str
    state: str
    zip_code: int
    country: str
    is_primary: bool = Field(default=False, nullable=False)


class Addresses(AddressBase, BaseUUID, table=True):
    user_id: UUID = Field(foreign_key="users.id")
    users: List["Users"] = Relationship(back_populates="address")


class AddressCreate(AddressBase):
    pass


class AddressShow(SQLModel):
    recipient_name: str
    house_no_name: str
    street_no_name: str
    city: str
    state: str
    zip_code: int
    country: str
    created_on: datetime
