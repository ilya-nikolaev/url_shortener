import logging

from flask import Flask
from sqlalchemy.orm import sessionmaker

from app.config_loader import load_config, Config
from app.db_api import create_all
from app.db_api.funcs import create_db_engine, create_db_factory
from app.middlewares.db_middleware import DBMiddleware
from app.views import index, redirect


def register_views(app: Flask):
    index.register_index(app)
    redirect.register_redirect(app)


def setup_middlewares(app: Flask, db_factory: sessionmaker):
    DBMiddleware(app, db_factory)


def create_app(config: Config, db_factory: sessionmaker) -> Flask:

    app = Flask(__name__)
    app.secret_key = config.app_settings.secret

    register_views(app)
    setup_middlewares(app, db_factory)

    return app


def main():
    logging.basicConfig(level=logging.INFO)

    config: Config = load_config()

    db_engine = create_db_engine(config.db_settings)
    db_factory = create_db_factory(db_engine)

    app = create_app(config, db_factory)

    create_all(db_engine)

    try:
        app.run(host="127.0.0.1", port=5000)
    except KeyboardInterrupt:
        db_factory.close_all()


if __name__ == '__main__':
    main()
