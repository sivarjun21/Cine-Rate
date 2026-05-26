from sqlalchemy.orm import Session

from app.models.user import User


def get_user_by_email(
    email: str,
    db: Session
):
    return db.query(User).filter(
        User.email == email
    ).first()


def get_user_by_id(
    user_id: int,
    db: Session
):
    return db.query(User).filter(
        User.id == user_id
    ).first()


def get_user_by_username(
    username: str,
    db: Session
):
    return db.query(User).filter(
        User.username == username
    ).first()


def create_user(
    user: User,
    db: Session
):
    db.add(user)

    db.commit()

    db.refresh(user)

    return user


def get_all_users(
    db: Session
):
    return db.query(User).all()


def delete_user(
    user: User,
    db: Session
):
    db.delete(user)

    db.commit()