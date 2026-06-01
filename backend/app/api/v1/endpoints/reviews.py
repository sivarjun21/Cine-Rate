from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.models.review import Review
from app.models.user import User

from app.schemas.review_schema import ReviewCreate


router = APIRouter()


@router.post("/")
def create_review(
    review: ReviewCreate,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.username == review.username
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    existing_review = db.query(
        Review
    ).filter(
        Review.movie_id == review.movie_id,
        Review.user_id == user.id
    ).first()

    if existing_review:
        raise HTTPException(
            status_code=400,
            detail="You already reviewed this movie"
        )

    new_review = Review(
        user_id=user.id,
        movie_id=review.movie_id,
        movie_title=review.movie_title,
        rating=review.rating,
        review_text=review.review_text
    )

    db.add(new_review)

    db.commit()

    db.refresh(new_review)

    return {
        "message": "Review created successfully"
    }


@router.get("/movie/{movie_id}")
def get_reviews(
    movie_id: int,
    db: Session = Depends(get_db)
):

    reviews = db.query(
        Review
    ).filter(
        Review.movie_id == movie_id
    ).all()

    result = []

    for review in reviews:

        user = db.query(User).filter(
            User.id == review.user_id
        ).first()

        result.append({
            "id": review.id,
            "movie_id": review.movie_id,
            "movie_title": review.movie_title,
            "rating": review.rating,
            "review_text": review.review_text,
            "username": user.username if user else "Unknown User"
        })

    return result


@router.get("/all")
def get_all_reviews(
    db: Session = Depends(get_db)
):

    reviews = db.query(
        Review
    ).all()

    result = []

    for review in reviews:

        user = db.query(User).filter(
            User.id == review.user_id
        ).first()

        result.append({
            "id": review.id,
            "movie_id": review.movie_id,
            "movie_title": review.movie_title,
            "rating": review.rating,
            "review_text": review.review_text,
            "username": user.username if user else "Unknown User"
        })

    return result