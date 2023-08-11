from sqlalchemy.dialects.postgresql import BIGINT, TEXT
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from db import Base


class ProhibitedDomain(Base):
    __tablename__ = 'prohibited_domains'

    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)
    domain: Mapped[str] = mapped_column(TEXT, nullable=False, unique=True)
