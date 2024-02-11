from fastapi import FastAPI
from api.v1.api import api as router

app = FastAPI()

app.include_router(router)
