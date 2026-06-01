from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import api_router

from app.core.database import Base
from app.core.database import engine

# Import models so SQLAlchemy creates tables
from app.models.user import User
from app.models.movie import Movie
from app.models.review import Review


# Create tables
Base.metadata.create_all(
    bind=engine
)


app = FastAPI(
    title="CineRate API"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():

    return {
        "message": "Backend working"
    }


app.include_router(
    api_router,
    prefix="/api/v1"
)