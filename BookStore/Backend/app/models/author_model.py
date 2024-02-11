from sqlmodel import SQLModel, Relationship
from typing import List
from models.base_uuid_model import BaseUUID
from models.author_book_model import AuthorBookLink


class AuthorBase(SQLModel):
    first_name: str
    last_name: str
    description: str


class Authors(AuthorBase, BaseUUID, table=True):
    books: List["Books"] = Relationship(back_populates="authors", link_model=AuthorBookLink)


class AuthorCreate(AuthorBase):
    pass
