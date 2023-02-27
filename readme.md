# URL SHORTENER

## Install
+ Create PostgreSQL database
+ Create and fill .env using .env.example
+ Create venv by command `python3.9 -m venv venv`
+ Activate venv by command `source venv/bin/activate`
+ Install requirements by command `python3.9 -m pip install -r requirements.txt`

The required python version is 3.9

## Local run
+ `python3.9 wsgi.py`

## Production run
+ Follow the [guide](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-22-04)

## TODO
+ Add link statistics
+ Improve UI
