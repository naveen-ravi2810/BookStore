from typing import List
from models.author_book_model import AuthorBookLink
from sqlmodel import SQLModel, Field, Relationship
from models.base_uuid_model import BaseUUID
from datetime import datetime


class BookBase(SQLModel):
    name: str = Field(unique=True)
    description: str
    price: int
    publish_year: datetime


class Books(BookBase, BaseUUID, table=True):
    authors: List["Authors"] = Relationship(back_populates="books", link_model=AuthorBookLink)


class BookCreate(BookBase):
    authors: List