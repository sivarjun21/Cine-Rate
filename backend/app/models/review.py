from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import Text
from sqlalchemy import Float
from sqlalchemy import DateTime

from sqlalchemy.orm import relationship

from datetime import datetime

from app.core.database import Base


class Review(Base):
    __tablename__ = "reviews"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    movie_id = Column(
        Integer,
        ForeignKey("movies.id"),
        nullable=False
    )

    rating = Column(
        Float,
        nullable=False
    )

    review_text = Column(
        Text
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    user = relationship("User")

    movie = relationship("Movie")