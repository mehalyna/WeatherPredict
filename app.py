import os
from functools import wraps
from flask import Flask, render_template, send_file, request, session, redirect, url_for

from user_database import CITIES, MONTHS, data, get_city_temperature, get_city_humidity
from user_database import db_session as db_session
from charts import get_main_image

app = Flask(__name__)


@app.route('/')
def main():
    """Entry point; the view for the main page"""
    cities = [(record.city_id, record.city_name) for record in data]
    return render_template('main.html', cities=cities)


@app.route('/main.png')
def main_plot():
    """The view for rendering the scatter chart"""
    img = get_main_image()
    return send_file(img, mimetype='image/png', cache_timeout=0)


if __name__ == '__main__':
    app.run()
