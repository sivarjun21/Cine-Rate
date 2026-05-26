from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_create_movie():
    response = client.post(
        "/api/v1/movies",
        json={
            "title": "Test Movie",
            "release_year": 2025,
            "description": "Test description",
            "poster_url": "https://example.com/poster.jpg"
        }
    )

    assert response.status_code in [201, 400]


def test_get_movies():
    response = client.get(
        "/api/v1/movies"
    )

    assert response.status_code == 200

    assert isinstance(
        response.json(),
        list
    )


def test_get_movie_by_id():
    response = client.get(
        "/api/v1/movies/1"
    )

    assert response.status_code in [200, 404]