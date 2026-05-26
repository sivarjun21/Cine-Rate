from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import Float
from sqlalchemy import DateTime

from datetime import datetime

from app.core.database import Base


class Movie(Base):
    __tablename__ = "movies"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String,
        nullable=False,
        index=True
    )

    release_year = Column(
        Integer
    )

    description = Column(
        Text
    )

    poster_url = Column(
        String
    )

    average_rating = Column(
        Float,
        default=0.0
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )