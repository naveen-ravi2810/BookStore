from sqlmodel import Session, create_engine
from core.settings import setting
from typing import Annotated
from fastapi import Depends
from redis import Redis

engine = create_engine(setting.DB_URI)


def get_db():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_db)]

r_conn = Redis(host=setting.REDIS_HOST, port=setting.REDIS_PORT, db=setting.REDIS_DB)
