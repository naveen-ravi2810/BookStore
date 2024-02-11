from sqlmodel import Session, select
from models.address_model import Addresses, AddressCreate
from models.user_model import Users


def get_address_by_email(email: str, session: Session):
    statement = select(Addresses).where(Users.email == email)
    address = session.execute(statement).scalars().all()
    return address


def add_address_by_email(email: str, session: Session, address_details: AddressCreate):
    statement = select(Users.id).where(Users.email == email)
    print(session.execute(statement).scalar())
    address = Addresses(**address_details.dict(), user_id=session.execute(statement).scalar())
    session.add(address)
    session.commit()
    return True
