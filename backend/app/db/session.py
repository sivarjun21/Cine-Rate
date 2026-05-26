from app.core.database import SessionLocal


def get_database_session():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()