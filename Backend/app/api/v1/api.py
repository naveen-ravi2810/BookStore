from api.v1.endpoints.users import router as users_route
from api.v1.endpoints.login import router as login_route
from api.v1.endpoints.address import router as address_route
from api.v1.endpoints.authors import router as author_route
from api.v1.endpoints.books import router as books_route
from fastapi import APIRouter

api = APIRouter()

api.include_router(login_route, prefix="/login", tags=["Login"])
api.include_router(users_route, prefix="/users", tags=["User"])
api.include_router(address_route, prefix="/address", tags=["Address"])
api.include_router(author_route, prefix="/author", tags=["Author"])
api.include_router(books_route, prefix="/books", tags=["Books"])
