from sqlalchemy import BIGINT, TEXT
from sqlalchemy import Column

from db import Base


class Link(Base):
    __tablename__ = "links"

    id = Column(BIGINT, primary_key=True)
    source = Column(TEXT, unique=True, nullable=False)
