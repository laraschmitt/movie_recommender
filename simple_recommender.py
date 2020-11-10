# Simple recommender
# calculation of an ordered top list with
# regards to the average rating of movies

import pandas as pd
import numpy as np
from sklearn.decomposition import NMF

# load clean dataset
df = pd.read_csv('./data/ml-latest-small/dev_ds_ratings_names_uniqueids.csv',
                 index_col=0)

R = df.pivot_table(index='userId',
                   columns='movieId_unique',
                   values='rating',
                   dropna=False)

# count the number of ratings per film:
R.loc['rating_count'] = R.count(axis=0)

# filter for movieIds with more than 50 ratings
R_gt_50 = R[R.columns[R.loc['rating_count'] > 50]]
# drop rating count row again
R = R_gt_50.drop(['rating_count'])

# create rating matrix R
R.fillna(0, inplace=True)  # not: (R.median().median())

# instantiate Non negative matrix factorization
m = NMF(n_components=20)
m.fit(R)

# get Predictors (p) - users and quantities (Q) - components
Q = m.components_
P = m.transform(R)

# calculate new rating matrix and put into dataframe
new_R = np.dot(P, Q)
new_R_df = pd.DataFrame(new_R.round(1), columns=R.columns, index=R.index)

# find movies with overall top ratings: calculate the sum of every column
# Only consider movies that are rated by a number of
# users above a certain threshold. Try out different theshold values.
new_R_df.loc['rating_sum'] = new_R_df.sum(axis=0)

# show 100 movie_ids with the highest ratings
top_100_df = new_R_df.sort_values(by='rating_sum',
                                  axis=1, ascending=False).iloc[-1:, 0:100]
top_100_list = top_100_df.columns.to_list()


def recommend_top_films_unwatched(user_id, top_list, r_df, k):
    """ Function that returns a top list of the
    overall highest rated films the specific user has not seen yet

    Parameters:
    - user_id
    - the top list of movies
    - and the ratings table
    - k movie_title the user wants to get recommended

    """

    # get movie_ids of the films the user has already seen
    movies_seen = r_df.iloc[user_id][r_df.iloc[user_id] != 0].index.to_list()

    # remove them from the top100_list
    top_films_to_watch = list(set(top_list) - set(movies_seen))
    print('remaining top films for this user to watch:',
          len(top_films_to_watch))

    # map movieIds to movie names
    rec_names = []
    for movie_id in top_films_to_watch:
        m_nam = df.loc[df['movieId_unique'] == movie_id]['title'].unique()[0]
        rec_names.append(m_nam)

    # return top 5 (if 5 film lelft to watch)
    return rec_names[:k]


# prediction -test
print(recommend_top_films_unwatched(2, top_100_list, new_R_df, 3))
print(recommend_top_films_unwatched(34, top_100_list, new_R_df, 5))
