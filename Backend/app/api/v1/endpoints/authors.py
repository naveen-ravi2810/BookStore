from fastapi import APIRouter
from models.author_model import AuthorCreate
from db import SessionDep

router = APIRouter()


@router.post("")
def get_authors(session: SessionDep, author_details: AuthorCreate):
    return {'1': author_details}
