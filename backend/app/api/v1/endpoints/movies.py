from fastapi import APIRouter
import requests

from app.core.config import settings


router = APIRouter()


BASE_URL = "https://api.themoviedb.org/3"


@router.get("/trending")
def get_trending_movies():

    url = f"{BASE_URL}/trending/movie/week"

    params = {
        "api_key": settings.TMDB_API_KEY
    }

    response = requests.get(url, params=params)

    return response.json()


@router.get("/search")
def search_movies(query: str):

    url = f"{BASE_URL}/search/movie"

    params = {
        "api_key": settings.TMDB_API_KEY,
        "query": query
    }

    response = requests.get(url, params=params)

    return response.json()


@router.get("/{movie_id}")
def get_movie_details(movie_id: int):

    url = f"{BASE_URL}/movie/{movie_id}"

    params = {
        "api_key": settings.TMDB_API_KEY
    }

    response = requests.get(url, params=params)

    return response.json()