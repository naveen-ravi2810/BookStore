from bcrypt import hashpw, gensalt, checkpw
from models.user_model import Users
import jwt
import time
from core.settings import setting
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

JWT_SECRET_KEY = setting.JWT_KEY
JWT_ALGORITHM = setting.JWT_ALGORITHM


def hash_password(password: str) -> str:
    return hashpw(password=password.encode("utf-8"), salt=gensalt()).decode("utf-8")


def check_hash_pw(bcrypt_pw, text):
    print(bcrypt_pw)
    print(text)
    return checkpw(
        password=text.encode("utf-8"), hashed_password=bcrypt_pw.encode("utf-8")
    )


def login_token(user: Users):
    curr_time = int(time.time())
    access_token = jwt.encode(
        payload={
            "id": str(user.id),
            "identity": user.email,
            "iat": curr_time,
            "exp": curr_time + (60 * 60 * 24 * 30),
        },
        key=JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )
    refresh_token = jwt.encode(
        payload={
            "id": str(user.id),
            "fresh": True,
            "identity": user.email,
            "iat": curr_time,
            "exp": curr_time + (60 * 60 * 24 * 30 * 12),
        },
        key=JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM,
    )
    return access_token, refresh_token


class JWTBearer(HTTPBearer):

    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(
            JWTBearer, self
        ).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid authentication scheme."
                )
            try:
                payload = decode_jwt(credentials.credentials)
                if payload:
                    return payload
                else:
                    raise HTTPException(
                        status_code=403, detail="Invalid or Expire Token"
                    )
            except HTTPException as e:
                raise HTTPException(status_code=403, detail=e.detail)
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")


def decode_jwt(token: str):
    try:
        return jwt.decode(jwt=token, key=JWT_SECRET_KEY, algorithms=JWT_ALGORITHM)
    except:
        return False
