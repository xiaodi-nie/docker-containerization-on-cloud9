#!/usr/bin/env python
from flask import Flask
from flask import jsonify
from pandas import pandas as pd


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/greeting')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello Fellas continuous deployment on GCP rox yeeeeeheee!'

@app.route('/name/<value>')
def name(value):
    val = {"value": value}
    return jsonify(val)

@app.route('/')
def html():
    """Returns some custom HTML"""
    return """
    <title>This is a Hello World World Page</title>
    <h3>Hello</h3>
    <br>
    <p><b>This is a simple flask web page</b></p>
    <p>Wrapped inside a Docker container and running on cloud9</p>
    """

@app.route('/pandas')
def pandas_sugar():
    df = pd.read_csv("https://raw.githubusercontent.com/noahgift/sugar/master/data/education_sugar_cdc_2003.csv")
    return jsonify(df.to_dict())

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='0.0.0.0', port=8080, debug=True)