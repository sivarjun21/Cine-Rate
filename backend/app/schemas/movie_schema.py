from pydantic import BaseModel

from datetime import datetime


class MovieBase(BaseModel):
    title: str
    release_year: int | None = None
    description: str | None = None
    poster_url: str | None = None


class MovieCreate(MovieBase):
    pass


class MovieResponse(MovieBase):
    id: int
    average_rating: float
    created_at: datetime

    class Config:
        from_attributes = True