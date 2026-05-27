from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

reviews_db = []


class ReviewCreate(BaseModel):
    movie_id: int
    movie_title: str
    rating: int
    review_text: str
    username: str


@router.post("/")
def create_review(review: ReviewCreate):

    # prevent same user reviewing same movie twice
    for existing_review in reviews_db:

        if (
            existing_review["movie_id"] == review.movie_id
            and existing_review["username"] == review.username
        ):
            return {
                "message": "You already reviewed this movie"
            }

    new_review = {
        "id": len(reviews_db) + 1,
        "movie_id": review.movie_id,
        "movie_title": review.movie_title,
        "rating": review.rating,
        "review_text": review.review_text,
        "username": review.username
    }

    reviews_db.append(new_review)

    return new_review


@router.get("/movie/{movie_id}")
def get_reviews(movie_id: int):

    movie_reviews = []

    for review in reviews_db:

        if review["movie_id"] == movie_id:
            movie_reviews.append(review)

    return movie_reviews


@router.get("/all")
def get_all_reviews():

    return reviews_db