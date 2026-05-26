from sqlalchemy.orm import Session

from fastapi import HTTPException
from fastapi import status

from app.models.movie import Movie

from app.schemas.movie_schema import MovieCreate


def create_movie_service(
    movie_data: MovieCreate,
    db: Session
):
    existing_movie = db.query(Movie).filter(
        Movie.title == movie_data.title
    ).first()

    if existing_movie:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Movie already exists"
        )

    new_movie = Movie(
        title=movie_data.title,
        release_year=movie_data.release_year,
        description=movie_data.description,
        poster_url=movie_data.poster_url
    )

    db.add(new_movie)

    db.commit()

    db.refresh(new_movie)

    return new_movie


def get_movies_service(
    db: Session
):
    movies = db.query(Movie).all()

    return movies


def get_movie_by_id_service(
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

    return movie