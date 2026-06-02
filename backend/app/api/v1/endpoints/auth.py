print("AUTH 1")
from fastapi import APIRouter

print("AUTH 2")
from fastapi import Depends

print("AUTH 3")
from fastapi import HTTPException

print("AUTH 4")
from fastapi import status

print("AUTH 5")
from fastapi.security import OAuth2PasswordRequestForm

print("AUTH 6")
from sqlalchemy.orm import Session

print("AUTH 7")
from app.core.database import get_db

print("AUTH 8")
from app.core.security import hash_password

print("AUTH 9")
from app.core.security import verify_password

print("AUTH 10")
from app.core.security import create_access_token

print("AUTH 11")
from app.models.user import User

print("AUTH 12")
from app.schemas.auth_schema import RegisterRequest

print("AUTH 13")
from app.schemas.token_schema import Token

print("AUTH 14")

router = APIRouter()


@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED
)
def register_user(
    user_data: RegisterRequest,
    db: Session = Depends(get_db)
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


@router.post(
    "/login",
    response_model=Token
)
def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.email == form_data.username
    ).first()

    if not user:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    valid_password = verify_password(
        form_data.password,
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

        "token_type": "bearer",

        "username": user.username
    }