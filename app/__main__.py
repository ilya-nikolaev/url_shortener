import logging

from flask import Flask
from sqlalchemy.orm import sessionmaker

from app.config_loader import load_config, Config
from db.funcs import create_db_engine, create_db_factory
from app.middlewares.db_middleware import DBMiddleware
from app.views import index, redirect


def register_views(app: Flask):
    index.register_index(app)
    redirect.register_redirect(app)


def setup_middlewares(app: Flask, db_factory: sessionmaker):
    DBMiddleware(app, db_factory)


def create_app() -> Flask:
    config: Config = load_config()

    db_engine = create_db_engine(config.db_settings)
    db_factory = create_db_factory(db_engine)

    app = Flask(__name__)
    app.secret_key = config.app_settings.secret

    register_views(app)
    setup_middlewares(app, db_factory)

    return app


def main():
    logging.basicConfig(level=logging.INFO)

    app = create_app()
    app.run(host="127.0.0.1", port=5000)


if __name__ == '__main__':
    main()
