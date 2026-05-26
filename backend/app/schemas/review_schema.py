from pydantic import BaseModel
from pydantic import Field

from datetime import datetime


class ReviewBase(BaseModel):
    rating: float = Field(
        ge=1,
        le=10
    )

    review_text: str | None = None


class ReviewCreate(ReviewBase):
    movie_id: int


class ReviewResponse(ReviewBase):
    id: int
    user_id: int
    movie_id: int
    created_at: datetime

    class Config:
        from_attributes = True