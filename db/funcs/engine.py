from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from app.config_loader import DBSettings


def create_db_engine(settings: DBSettings) -> Engine:
    return create_engine(
        f"postgresql+psycopg2://"
        f"{settings.user}:"
        f"{settings.pswd}@"
        f"{settings.host}:"
        f"{settings.port}/"
        f"{settings.name}"
    )
