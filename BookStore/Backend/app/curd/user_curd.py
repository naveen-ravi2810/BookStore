from sqlmodel import Session, select
from redis import Redis
from models.user_model import Users, UserCreate, UserLogin
from core.security import hash_password, check_hash_pw, login_token


def add_user(session: Session, user_details: UserCreate):
    user = Users(
        first_name=user_details.first_name,
        last_name=user_details.last_name,
        email=user_details.email,
        phone=user_details.phone,
        DOB=user_details.DOB,
        password=hash_password(user_details.password),
    )
    session.add(user)
    session.commit()
    return True


def login_user(session: Session, r_conn: Redis, user_details: UserLogin):
    statement = select(Users).where(Users.email == user_details.email)
    user = session.execute(statement).scalar()
    print(user)
    if user:
        print(user.password)
        if check_hash_pw(bcrypt_pw=user.password, text=user_details.password):
            access_token, refresh_token = login_token(user=user)
            r_conn.setex(
                name=f"access_token:{user.email}",
                value=access_token,
                time=60 * 60 * 24 * 30,
            )
            r_conn.setex(
                name=f"refresh_token:{user.email}",
                value=refresh_token,
                time=60 * 60 * 24 * 30 * 12,
            )
            return {
                "status": True,
                "access_token": access_token,
                "refresh_token": refresh_token,
            }
    return False
