import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pandas as pd
from flask import Flask, jsonify
import json

engine = create_engine('postgresql+psycopg2://postgres:5432@localhost/etl_project')


Base = automap_base()

Base.prepare(engine, reflect=True)


imdb_df = Base.classes.imdb_df

app = Flask(__name__)


@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Welcome to our movie database!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/imdb_movies<br/>"
        f"/api/v1.0/nyt_movies<br/>"
        f"/api/v1.0/rot_movies"
    )


@app.route("/api/v1.0/imdb_movies")
def imdb_movies():

    imdb_results = pd.read_sql_query('select * from imdb_df', con=engine)


    imdb_results = imdb_results.to_json(orient="records")
    parsed = json.loads(imdb_results)


    return jsonify(parsed)

@app.route("/api/v1.0/nyt_movies")
def nyt_movies():

    nyt_results = pd.read_sql_query('select * from nyt_df', con=engine)


    nyt_results = nyt_results.to_json(orient="records")
    parsed = json.loads(nyt_results)

    print("its running")
    return jsonify(parsed)

@app.route("/api/v1.0/rot_movies")
def rot_movies():

    rot_results = pd.read_sql_query('select * from rotten_df', con=engine)


    rot_results = rot_results.to_json(orient="records")
    parsed = json.loads(rot_results)

    print("its running")
    return jsonify(parsed)

if __name__ == '__main__':
    app.run(debug=True)
