from fastapi import APIRouter

from app.services.tmdb_service import (
    get_trending_movies,
    search_movies,
    get_movie_details
)


router = APIRouter()


@router.get("/trending")
def trending_movies():

    return get_trending_movies()


@router.get("/search")
def search_movie(query: str):

    return search_movies(query)


@router.get("/{movie_id}")
def movie_details(movie_id: int):

    return get_movie_details(movie_id)