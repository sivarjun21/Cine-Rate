from fastapi import APIRouter

from app.api.v1.endpoints import movies
from app.api.v1.endpoints import reviews
from app.api.v1.endpoints import auth


api_router = APIRouter()

api_router.include_router(
    movies.router,
    prefix="/movies",
    tags=["Movies"]
)

api_router.include_router(
    reviews.router,
    prefix="/reviews",
    tags=["Reviews"]
)

api_router.include_router(
    auth.router,
    prefix="/auth",
    tags=["Auth"]
)