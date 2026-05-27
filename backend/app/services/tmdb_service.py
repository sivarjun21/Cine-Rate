class TMDBService:

    def get_trending_movies(self):
        return {
            "results": []
        }

    def search_movies(self, query):
        return {
            "results": []
        }

    def get_movie_details(self, movie_id):
        return {
            "id": movie_id,
            "title": "Fight Club",
            "poster_path": "",
            "overview": "Test movie",
            "vote_average": 8.5,
            "release_date": "1999-10-15"
        }


tmdb_service = TMDBService()