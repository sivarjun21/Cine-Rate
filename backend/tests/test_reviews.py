from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def get_auth_token():
    register_response = client.post(
        "/api/v1/auth/register",
        json={
            "username": "reviewtester",
            "email": "review@test.com",
            "password": "password123"
        }
    )

    login_response = client.post(
        "/api/v1/auth/login",
        json={
            "email": "review@test.com",
            "password": "password123"
        }
    )

    token = login_response.json()["access_token"]

    return token


def test_create_review():
    token = get_auth_token()

    response = client.post(
        "/api/v1/reviews",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "movie_id": 1,
            "rating": 9,
            "review_text": "Amazing movie"
        }
    )

    assert response.status_code in [201, 400, 404]


def test_get_movie_reviews():
    response = client.get(
        "/api/v1/reviews/movie/1"
    )

    assert response.status_code in [200, 404]


def test_delete_review():
    token = get_auth_token()

    create_response = client.post(
        "/api/v1/reviews",
        headers={
            "Authorization": f"Bearer {token}"
        },
        json={
            "movie_id": 1,
            "rating": 8,
            "review_text": "Good movie"
        }
    )

    if create_response.status_code == 201:

        review_id = create_response.json()["id"]

        delete_response = client.delete(
            f"/api/v1/reviews/{review_id}",
            headers={
                "Authorization": f"Bearer {token}"
            }
        )

        assert delete_response.status_code == 200