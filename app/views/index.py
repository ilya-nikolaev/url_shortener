from flask import Flask
from flask import render_template, make_response
from flask import request, g

from app.shortener_core.funcs import get_shortened_link


def index():
    if request.method == 'GET':
        link = request.args.get('url', "")
        shortened, message = get_shortened_link(link, g.get('db'))
        return render_template('index.html', shortened_url=shortened, message=message)
    else:
        return make_response('', 503)


def register_index(app: Flask):
    app.add_url_rule('/index', view_func=index, endpoint='index')
    app.add_url_rule('/', view_func=index, endpoint='index')
