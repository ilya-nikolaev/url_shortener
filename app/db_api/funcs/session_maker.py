from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker


def create_db_factory(db_engine: Engine) -> sessionmaker:
    return sessionmaker(
        bind=db_engine,
        expire_on_commit=False
    )
