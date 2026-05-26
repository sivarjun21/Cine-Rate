import requests

from app.core.config import settings

import requests

from app.core.config import settings

print(settings.TMDB_API_KEY)

def get_trending_movies():

    url = f"{settings.TMDB_BASE_URL}/trending/movie/week"

    params = {
        "api_key": settings.TMDB_API_KEY
    }

    response = requests.get(
        url,
        params=params,
        timeout=30
    )

    return response.json()


def search_movies(query: str):

    url = f"{settings.TMDB_BASE_URL}/search/movie"

    params = {
        "api_key": settings.TMDB_API_KEY,
        "query": query
    }

    response = requests.get(
        url,
        params=params,
        timeout=30
    )

    return response.json()


def get_movie_details(movie_id: int):

    url = f"{settings.TMDB_BASE_URL}/movie/{movie_id}"

    params = {
        "api_key": settings.TMDB_API_KEY
    }

    response = requests.get(
        url,
        params=params,
        timeout=30
    )

    response.raise_for_status()

    return response.json()