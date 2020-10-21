/* script to import the movies.csv and ratings.csv from the 
MovieLens Latest Datasets - full (https://grouplens.org/datasets/movielens/latest/) */

-- to execute file in commandline:
-- psql -h localhost -U postgres -d movielens -f ~/repos/movie_recommender/import_tables.sql

DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS ratings;

CREATE TABLE ratings(
    id SERIAL PRIMARY KEY,
    userId INT NOT NULL,
    movieId INT NOT NULL,
    rating DECIMAL NOT NULL,
    timestamp VARCHAR
);

-- copy csv content
COPY ratings(userId, movieId, rating, timestamp)
FROM '/Users/lara/repos/movie_recommender/data/ml-latest/ratings.csv'
DELIMITER ','
CSV HEADER;


CREATE TABLE movies(
    id SERIAL PRIMARY KEY,
    movieId INT NOT NULL,
    title VARCHAR NOT NULL,
    genres VARCHAR NOT NULL
);

-- copy csv content
COPY movies(movieId, title, genres)
FROM '/Users/lara/repos/movie_recommender/data/ml-latest/movies.csv'
DELIMITER ','
CSV HEADER;
