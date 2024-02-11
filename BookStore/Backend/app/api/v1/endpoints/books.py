from fastapi import APIRouter
from db import SessionDep
from models.book_model import BookCreate
from curd.books_curd import get_books, create_book
router = APIRouter()


@router.get("")
def get_all_books(session:SessionDep):
    return {'books':get_books(session=session)}


@router.post("")
def post_books(session:SessionDep, book_details: BookCreate):
    create_book(session=session, book_details=book_details)
    return {'status':True}
