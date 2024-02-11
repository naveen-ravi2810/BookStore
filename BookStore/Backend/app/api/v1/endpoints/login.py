from fastapi import APIRouter
from db import SessionDep, r_conn
from models.user_model import UserLogin
from curd.user_curd import login_user

router = APIRouter()


@router.post("")
def login(session: SessionDep, user_details: UserLogin):
    user = login_user(session=session, r_conn=r_conn, user_details=user_details)
    if user:
        return user
    return {"status": False}
