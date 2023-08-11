from sqlalchemy.dialects.postgresql import BIGINT, TEXT
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from db import Base


class Link(Base):
    __tablename__ = "links"

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    source: Mapped[str] = mapped_column(TEXT, nullable=False, unique=True)
