from flask import Flask
from flask import g
from flask import redirect, abort

from app.shortener_core.funcs import get_source


def go_link(shortened: str):
    link = get_source(shortened, g.get('db'))
    if link is None:
        return abort(404)
    return redirect(link.source)


def register_redirect(app: Flask):
    app.add_url_rule('/<shortened>', view_func=go_link)
