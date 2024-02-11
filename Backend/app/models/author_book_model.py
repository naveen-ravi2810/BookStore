from sqlmodel import SQLModel, Field
from uuid import UUID


class AuthorBookLink(SQLModel,table=True):
    author_id: UUID = Field(default=None, foreign_key="authors.id", primary_key=True)
    book_id: UUID = Field(default=None, foreign_key="books.id", primary_key=True)
