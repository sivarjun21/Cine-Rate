from app.core.database import SessionLocal

from app.models.movie import Movie


sample_movies = [
    {
        "title": "Interstellar",
        "release_year": 2014,
        "description": "A science fiction movie about space exploration.",
        "poster_url": "https://example.com/interstellar.jpg"
    },
    {
        "title": "Inception",
        "release_year": 2010,
        "description": "A mind-bending thriller about dreams.",
        "poster_url": "https://example.com/inception.jpg"
    },
    {
        "title": "The Dark Knight",
        "release_year": 2008,
        "description": "Batman faces the Joker in Gotham City.",
        "poster_url": "https://example.com/darkknight.jpg"
    }
]


def seed_movies():
    db = SessionLocal()

    try:
        for movie_data in sample_movies:

            existing_movie = db.query(Movie).filter(
                Movie.title == movie_data["title"]
            ).first()

            if not existing_movie:

                movie = Movie(
                    title=movie_data["title"],
                    release_year=movie_data["release_year"],
                    description=movie_data["description"],
                    poster_url=movie_data["poster_url"]
                )

                db.add(movie)

        db.commit()

        print("Movies seeded successfully")

    finally:
        db.close()


if __name__ == "__main__":
    seed_movies()