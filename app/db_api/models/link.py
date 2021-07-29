from sqlalchemy import BIGINT, TEXT
from sqlalchemy import Column, ForeignKey

from app.db_api import Base


class Link(Base):
    __tablename__ = "links"

    id = Column(BIGINT, autoincrement=True)

    source = Column(TEXT, primary_key=True)
    cropped = Column(TEXT, unique=True, nullable=False)
