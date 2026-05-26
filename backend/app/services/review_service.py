from sqlalchemy.orm import Session

from fastapi import HTTPException
from fastapi import status

from app.models.review import Review
from app.models.movie import Movie
from app.models.user import User

from app.schemas.review_schema import ReviewCreate


def create_review_service(
    review_data: ReviewCreate,
    current_user: User,
    db: Session
):
    movie = db.query(Movie).filter(
        Movie.id == review_data.movie_id
    ).first()

    if not movie:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Movie not found"
        )

    existing_review = db.query(Review).filter(
        Review.user_id == current_user.id,
        Review.movie_id == review_data.movie_id
    ).first()

    if existing_review:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
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

    update_movie_rating_service(
        movie.id,
        db
    )

    return new_review


def get_movie_reviews_service(
    movie_id: int,
    db: Session
):
    movie = db.query(Movie).filter(
        Movie.id == movie_id
    ).first()

    if not movie:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Movie not found"
        )

    reviews = db.query(Review).filter(
        Review.movie_id == movie_id
    ).all()

    return reviews


def delete_review_service(
    review_id: int,
    current_user: User,
    db: Session
):
    review = db.query(Review).filter(
        Review.id == review_id
    ).first()

    if not review:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Review not found"
        )

    if review.user_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to delete this review"
        )

    movie_id = review.movie_id

    db.delete(review)

    db.commit()

    update_movie_rating_service(
        movie_id,
        db
    )

    return {
        "message": "Review deleted successfully"
    }


def update_movie_rating_service(
    movie_id: int,
    db: Session
):
    movie = db.query(Movie).filter(
        Movie.id == movie_id
    ).first()

    reviews = db.query(Review).filter(
        Review.movie_id == movie_id
    ).all()

    if reviews:
        average_rating = sum(
            review.rating for review in reviews
        ) / len(reviews)

        movie.average_rating = round(
            average_rating,
            1
        )

    else:
        movie.average_rating = 0.0

    db.commit()