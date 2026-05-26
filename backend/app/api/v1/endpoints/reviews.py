from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from app.api.deps import get_current_user

from app.core.database import get_db

from app.models.review import Review
from app.models.movie import Movie
from app.models.user import User

from app.schemas.review_schema import ReviewCreate
from app.schemas.review_schema import ReviewResponse


router = APIRouter()


@router.post(
    "/",
    response_model=ReviewResponse,
    status_code=status.HTTP_201_CREATED
)
def create_review(
    review_data: ReviewCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    movie = db.query(Movie).filter(
        Movie.id == review_data.movie_id
    ).first()

    if not movie:
        raise HTTPException(
            status_code=404,
            detail="Movie not found"
        )

    existing_review = db.query(Review).filter(
        Review.user_id == current_user.id,
        Review.movie_id == review_data.movie_id
    ).first()

    if existing_review:
        raise HTTPException(
            status_code=400,
            detail="You already reviewed this movie"
        )

    new_review = Review(
        user_id=current_user.id,
        movie_id=review_data.movie_id,
        rating=review_data.rating,
        review_text=review_data.review_text
    )

    db.add(new_review)

    db.commit()

    db.refresh(new_review)

    reviews = db.query(Review).filter(
        Review.movie_id == movie.id
    ).all()

    average_rating = sum(
        review.rating for review in reviews
    ) / len(reviews)

    movie.average_rating = round(
        average_rating,
        1
    )

    db.commit()

    return new_review


@router.get(
    "/movie/{movie_id}",
    response_model=list[ReviewResponse]
)
def get_movie_reviews(
    movie_id: int,
    db: Session = Depends(get_db)
):
    movie = db.query(Movie).filter(
        Movie.id == movie_id
    ).first()

    if not movie:
        raise HTTPException(
            status_code=404,
            detail="Movie not found"
        )

    reviews = db.query(Review).filter(
        Review.movie_id == movie_id
    ).all()

    return reviews


@router.delete(
    "/{review_id}",
    status_code=status.HTTP_200_OK
)
def delete_review(
    review_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    review = db.query(Review).filter(
        Review.id == review_id
    ).first()

    if not review:
        raise HTTPException(
            status_code=404,
            detail="Review not found"
        )

    if review.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Not authorized to delete this review"
        )

    movie = db.query(Movie).filter(
        Movie.id == review.movie_id
    ).first()

    db.delete(review)

    db.commit()

    remaining_reviews = db.query(Review).filter(
        Review.movie_id == movie.id
    ).all()

    if remaining_reviews:
        average_rating = sum(
            review.rating for review in remaining_reviews
        ) / len(remaining_reviews)

        movie.average_rating = round(
            average_rating,
            1
        )

    else:
        movie.average_rating = 0.0

    db.commit()

    return {
        "message": "Review deleted successfully"
    }