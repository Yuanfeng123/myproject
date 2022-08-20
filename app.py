# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li
    :license: MIT, see LICENSE for more details.
"""
import click
from flask import Flask, render_template, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'asrtarstaursdlarsn'


# the minimal Flask application
@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'


# bind multiple URL for one view function
@app.route('/hi')
@app.route('/hello')
def say_hello():
    return '<h1>Hello, Flask!</h1>'


# dynamic route, URL variable default
@app.route('/greet', defaults={'name': 'Programmer'})
@app.route('/greet/<name>')
def greet(name):
    return '<h1>Hello, %s!</h1>' % name


# custom flask cli command
@app.cli.command()
def hello():
    """Just say hello."""
    click.echo('Hello, Human!')



user = {
    "username":"yuan",
    "bio":"A boy",
}

movies = [
    {
        "name": "My Neighbor Totoro",
        "year": "1988",
    },
    {
        "name": "My Neighbor Totoro",
        "year": "1958",
    },
    {
        "name": "My Neighbor Totoro",
        "year": "1928",
    },
    {
        "name": "My Neighbor Totoro",
        "year": "1918",
    },
    {
        "name": "My Neighbor Totoro",
        "year": "1978",
    },
    {
        "name": "My Neighbor Totoro",
        "year": "1999",
    }
]

@app.route("/watchlist")
def watchlist():
    return render_template("watchlist.html", user=user, movies=movies)

@app.route("/flash")
def just_flash():
    flash("dddd")
    return redirect(url_for("index"))