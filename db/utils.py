from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker

from config.loader import DBSettings


def create_db_factory(db_engine: Engine) -> sessionmaker:
    return sessionmaker(bind=db_engine, expire_on_commit=False)


def create_db_engine(settings: DBSettings) -> Engine:
    return create_engine(get_db_url_from_settings(settings))


def get_db_url_from_settings(settings: DBSettings):
    return (
        f"postgresql+psycopg2://"
        f"{settings.user}:"
        f"{settings.pswd}@"
        f"{settings.host}:"
        f"{settings.port}/"
        f"{settings.name}"
    )
