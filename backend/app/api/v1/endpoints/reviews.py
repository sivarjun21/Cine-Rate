from fastapi import APIRouter

print("REVIEWS 1")
from fastapi import Depends

print("REVIEWS 2")
from fastapi import HTTPException

print("REVIEWS 3")
from sqlalchemy.orm import Session

print("REVIEWS 4")
from app.core.database import get_db

print("REVIEWS 5")
from app.models.review import Review

print("REVIEWS 6")
from app.models.user import User

print("REVIEWS 7")
from app.schemas.review_schema import ReviewCreate

print("REVIEWS 8")


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