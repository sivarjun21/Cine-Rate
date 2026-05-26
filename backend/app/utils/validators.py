from fastapi import HTTPException
from fastapi import status

from app.core.constants import (
    MIN_RATING,
    MAX_RATING
)


def validate_rating(
    rating: float
):
    if rating < MIN_RATING or rating > MAX_RATING:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                f"Rating must be between "
                f"{MIN_RATING} and {MAX_RATING}"
            )
        )


def validate_review_text(
    review_text: str
):
    if review_text and len(review_text) > 1000:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                "Review text cannot exceed "
                "1000 characters"
            )
        )


def validate_movie_title(
    title: str
):
    if not title.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Movie title cannot be empty"
        )