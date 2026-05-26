from sqlalchemy.orm import Session

from fastapi import HTTPException
from fastapi import status

from app.models.user import User

from app.schemas.auth_schema import RegisterRequest
from app.schemas.auth_schema import LoginRequest

from app.core.security import hash_password
from app.core.security import verify_password
from app.core.security import create_access_token


def register_user_service(
    user_data: RegisterRequest,
    db: Session
):
    existing_user = db.query(User).filter(
        User.email == user_data.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    new_user = User(
        username=user_data.username,
        email=user_data.email,
        password_hash=hash_password(
            user_data.password
        )
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {
        "message": "User registered successfully"
    }


def login_user_service(
    login_data: LoginRequest,
    db: Session
):
    user = db.query(User).filter(
        User.email == login_data.email
    ).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    valid_password = verify_password(
        login_data.password,
        user.password_hash
    )

    if not valid_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        data={
            "user_id": user.id
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }