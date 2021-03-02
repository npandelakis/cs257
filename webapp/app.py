#!/usr/bin/env python3
'''
    app.py
    Grace de Benedetti and Nick Pandelakis
    22 February 2021

    A Flask web application to display global terrorism data.
'''

import sys
import argparse
import flask
import api

app = flask.Flask(__name__, static_folder='static', template_folder='templates')
app.register_blueprint(api.api, url_prefix='/api')


@app.route('/')
def home():
    return flask.render_template('world-map.html')


@app.route('/countries/<country_code>')
def country_page(country_code):
    return flask.render_template('country_template.html', country_code = country_code)

if __name__ == '__main__':
    parser = argparse.ArgumentParser('A tiny Flask application, including API')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)
