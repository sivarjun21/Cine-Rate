from sqlalchemy.orm import Session

from app.models.review import Review


def get_review_by_id(
    review_id: int,
    db: Session
):
    return db.query(Review).filter(
        Review.id == review_id
    ).first()


def get_user_movie_review(
    user_id: int,
    movie_id: int,
    db: Session
):
    return db.query(Review).filter(
        Review.user_id == user_id,
        Review.movie_id == movie_id
    ).first()


def create_review(
    review: Review,
    db: Session
):
    db.add(review)

    db.commit()

    db.refresh(review)

    return review


def get_reviews_by_movie(
    movie_id: int,
    db: Session
):
    return db.query(Review).filter(
        Review.movie_id == movie_id
    ).all()


def get_reviews_by_user(
    user_id: int,
    db: Session
):
    return db.query(Review).filter(
        Review.user_id == user_id
    ).all()


def delete_review(
    review: Review,
    db: Session
):
    db.delete(review)

    db.commit()