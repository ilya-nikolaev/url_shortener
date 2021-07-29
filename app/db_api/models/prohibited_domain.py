from sqlalchemy import BIGINT, TEXT
from sqlalchemy import Column

from app.db_api import Base


class ProhibitedDomain(Base):
    __tablename__ = 'prohibited_domains'

    id = Column(BIGINT, primary_key=True)

    domain = Column(TEXT, unique=True, nullable=False)
