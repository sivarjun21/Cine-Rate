from sqlalchemy.orm import Session

from app.models.movie import Movie


def get_movie_by_title(
    title: str,
    db: Session
):
    return db.query(Movie).filter(
        Movie.title == title
    ).first()


def create_movie(
    movie: Movie,
    db: Session
):
    db.add(movie)

    db.commit()

    db.refresh(movie)

    return movie


def get_all_movies(
    db: Session
):
    return db.query(Movie).all()


def get_movie_by_id(
    movie_id: int,
    db: Session
):
    return db.query(Movie).filter(
        Movie.id == movie_id
    ).first()


def update_movie(
    db: Session
):
    db.commit()


def delete_movie(
    movie: Movie,
    db: Session
):
    db.delete(movie)

    db.commit()