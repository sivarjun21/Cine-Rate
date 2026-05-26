from dotenv import load_dotenv

import os


load_dotenv()


class Settings:

    TMDB_API_KEY = os.getenv("TMDB_API_KEY")

    TMDB_BASE_URL = os.getenv(
        "TMDB_BASE_URL"
    )


settings = Settings()