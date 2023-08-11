from dataclasses import dataclass

from environs import Env


@dataclass
class AppSettings:
    secret: str


@dataclass
class DBSettings:
    host: str
    port: str
    name: str
    user: str
    pswd: str


@dataclass
class Config:
    app_settings: AppSettings
    db_settings: DBSettings


def load_config():
    env = Env()
    env.read_env()

    return Config(
        app_settings=AppSettings(
            secret=env.str("FLASK_APP_SECRET")
        ),
        db_settings=DBSettings(
            host=env.str("DB_HOST"),
            port=env.str("DB_PORT"),
            name=env.str("DB_NAME"),
            user=env.str("DB_USER"),
            pswd=env.str("DB_PSWD"),
        )
    )
