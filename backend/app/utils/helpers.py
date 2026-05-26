from statistics import mean

from app.models.review import Review


def calculate_average_rating(
    reviews: list[Review]
):
    if not reviews:
        return 0.0

    ratings = [
        review.rating
        for review in reviews
    ]

    return round(
        mean(ratings),
        1
    )


def format_success_response(
    message: str,
    data=None
):
    return {
        "success": True,
        "message": message,
        "data": data
    }


def format_error_response(
    message: str
):
    return {
        "success": False,
        "message": message
    }