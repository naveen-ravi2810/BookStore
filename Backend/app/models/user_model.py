from models.base_uuid_model import BaseUUID
from sqlmodel import SQLModel, Field, Relationship
from typing import List
from models.address_model import Addresses
from datetime import datetime


class UserBase(SQLModel):
    first_name: str = Field()
    last_name: str = Field()
    email: str = Field(unique=True, index=True)
    DOB: datetime


class Users(UserBase, BaseUUID, table=True):
    password: str
    phone: str = Field(unique=True)
    profile_image_url: str = Field(default="")
    address: List[Addresses] = Relationship(back_populates="users")


class UserCreate(UserBase):
    password: str
    phone: int


class UserLogin(SQLModel):
    email: str
    password: str
