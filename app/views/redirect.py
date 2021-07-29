from flask import Flask
from flask import redirect, make_response
from flask import g

from app.shortener_core.funcs import get_source


def go_link(shortened: str):
    source_link = get_source(shortened, g.get('db'))
    if source_link is None:
        return make_response('', 404)
    return redirect(source_link.source)


def register_redirect(app: Flask):
    app.add_url_rule('/<shortened>', view_func=go_link)
