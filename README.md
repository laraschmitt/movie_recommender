# movie_recommender
🎬 🍿unsupervised_learning


* dataset: [movielens dataset](https://grouplens.org/datasets/movielens/) 

This repo includes the pieces to build a movie recommender with a web interface.
1. [Exploratory data analysis](https://github.com/laraschmitt/movie_recommender/blob/main/EDA/EDA_movie_lens_100k_complete.ipynb) and data wrangling (for the small movielens dataset) in jupyter notebook.
2. [Python script](https://github.com/laraschmitt/movie_recommender/blob/main/data_wrangling.py) to create cleaned up dataset.
3. [SQL script](https://github.com/laraschmitt/movie_recommender/blob/main/DB_setup/import_tables.sql) to load the cleaned up MovieLens data into a Postgres database. 
4. [NMF model training] (https://github.com/laraschmitt/movie_recommender/blob/main/nmf_model_training.py). 
5. [Recommender function](https://github.com/laraschmitt/movie_recommender/blob/main/flask-app-bootstrap/nmf_recommender.py) based on user input (3 movies) and NMF model.
6. Write a Flask web interface for the recommender. (LINK MISSING)
    
