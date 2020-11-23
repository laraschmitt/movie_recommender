![Continuous Integration](https://github.com/laraschmitt/movie_recommender/workflows/Continuous%20Integration/badge.svg)

# movie_recommender
🎬 🍿unsupervised_learning


* dataset: [movielens dataset](https://grouplens.org/datasets/movielens/) 

A Website to recommend movies based on user input. Non-negative Matrix Factorization returns movie recommendations based on three given movie titles.

![example_image](browser_preview.png =100x150)

## How to use:
* Clone the repository 
* install dependencies: `cd app && pip3 install -r requirements.txt`
* run the app: `cd app && env FLASK_APP=application.py flask run`
* open a browser on the specified location



## This repo includes:
* [Exploratory data analysis](https://github.com/laraschmitt/movie_recommender/blob/main/EDA/EDA_movie_lens_100k_complete.ipynb) and data wrangling (for the small movielens dataset) in jupyter notebook
* [Python script](https://github.com/laraschmitt/movie_recommender/blob/main/data_wrangling.py) to create cleaned up dataset
* [SQL script](https://github.com/laraschmitt/movie_recommender/blob/main/DB_setup/import_tables.sql) to load the cleaned up MovieLens data into a Postgres database
* [NMF model training](https://github.com/laraschmitt/movie_recommender/blob/main/nmf_model_training.py) with sklearn
* [Recommender function](https://github.com/laraschmitt/movie_recommender/blob/main/flask-app-bootstrap/nmf_recommender.py) based on user input (3 movies) and NMF model
* [Flask web interface](https://github.com/laraschmitt/movie_recommender/blob/main/flask-app-bootstrap/application.py) for the recommender
    
