from fastapi import APIRouter

print("BEFORE MOVIES")
from app.api.v1.endpoints import movies
print("AFTER MOVIES")

print("BEFORE REVIEWS")
from app.api.v1.endpoints import reviews
print("AFTER REVIEWS")

print("BEFORE AUTH")
from app.api.v1.endpoints import auth
print("AFTER AUTH")

api_router = APIRouter()

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