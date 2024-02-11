from sqlmodel import Session, select
from models.book_model import Books, BookCreate


def get_books(session:Session):
    books = session.execute(select(Books)).scalars().all()
    return books


def create_book(session:Session, book_details:BookCreate):
    book = Books(**book_details.dict())
    session.add(book)
    session.commit()
    return book_details