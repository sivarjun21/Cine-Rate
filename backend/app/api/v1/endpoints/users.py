from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from app.api.deps import get_current_user

from app.core.database import get_db

from app.models.user import User
from app.models.review import Review

from app.schemas.user_schema import UserResponse


router = APIRouter()


@router.get(
    "/me",
    response_model=UserResponse
)
def get_my_profile(
    current_user: User = Depends(get_current_user)
):
    return current_user


@router.get(
    "/{user_id}",
    response_model=UserResponse
)
def get_user_profile(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


@router.get(
    "/{user_id}/reviews"
)
def get_user_reviews(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    reviews = db.query(Review).filter(
        Review.user_id == user_id
    ).all()

    return reviews