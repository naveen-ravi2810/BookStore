from sqlmodel import SQLModel
from models.base_uuid_model import BaseUUID


class GenreBase():
    name: str


class Genres(GenreBase, BaseUUID, table=True):
    pass


class GenreCreate(GenreBase):
    pass
