from sqlalchemy.orm import Session

from fastapi import HTTPException
from fastapi import status

from app.models.user import User
from app.models.review import Review


def get_current_user_profile_service(
    current_user: User
):
    return current_user


def get_user_profile_service(
    user_id: int,
    db: Session
):
    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user


def get_user_reviews_service(
    user_id: int,
    db: Session
):
    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    reviews = db.query(Review).filter(
        Review.user_id == user_id
    ).all()

    return reviews