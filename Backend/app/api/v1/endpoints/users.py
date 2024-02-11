from fastapi import APIRouter
from models.user_model import UserCreate
from db import SessionDep
from curd.user_curd import add_user
from sqlalchemy.exc import IntegrityError

router = APIRouter()


@router.post("", description="Register User", status_code=200)
def register_user(session: SessionDep, user_details: UserCreate):
    try:
        return {"status": add_user(session=session, user_details=user_details)}
    except IntegrityError as e:
        print(e)
        return {"status": False, "message": "Email already Exists"}
