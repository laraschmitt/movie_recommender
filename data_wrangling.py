# script to deal with non unique movieIds for certain films
# 1. replace the second occuring movieId for a film with the first occuring one
# 2. left join the titles on the ratings df
# (some movies do not have a rating, drop these)


import pandas as pd

# for the dev dataset
path_to_movies_csv = './data/ml-latest-small/movies.csv'
path_to_ratings_csv = './data/ml-latest-small/ratings.csv'

# for the big dataset
# path_to_movies_csv = './data/ml-latest/movies.csv'
# path_to_ratings_csv = './data/ml-latest/ratings.csv'

df_movie_names = pd.read_csv(path_to_movies_csv)
df_ratings = pd.read_csv(path_to_ratings_csv)

duplicateRowsDF = df_movie_names[df_movie_names.duplicated(subset=['title'])]
dup_titles = duplicateRowsDF['title'].tolist()
print(dup_titles)

dup = df_movie_names[df_movie_names['title'].isin(dup_titles)]
sort_dup = dup.sort_values(by='title', ascending=True)
print(sort_dup.head(20))

dup_id_list = sort_dup['movieId'].to_list()

print('duplicates found')

# put the valid ids and the second 2nd ids in list and zip them into a dict
every_valid_id = dup_id_list[::2]
every_sec_id = dup_id_list[1::2]

id_dictionary = dict(zip(every_sec_id, every_valid_id))


# Create new column 'movieId_unique' for dataframe
# 1. copy the existing ids
df_ratings['movieId_unique'] = df_ratings['movieId']
df_movie_names['movieId_unique'] = df_movie_names['movieId']

print('first occuring movie IDs values mapped to duplicates')

print('unique movie ID created')

# Remap the values of the dataframe
df_ratings = df_ratings.replace({"movieId_unique": id_dictionary})
df_movie_names = df_movie_names.replace({"movieId_unique": id_dictionary})

# left merge to keep only movies with existing ratings
df = pd.merge(df_ratings, df_movie_names, on='movieId_unique', how='left')
# check for number of unique ids
df['movieId_unique'].nunique()

print('dataframes merged')

# export cleaned up combined dateframe
# dev dataset
df.to_csv('./data/ml-latest-small/dev_ds_ratings_names_uniqueids.csv')

# big dataset
# df.to_csv('./data/ml-latest/large_ds_ratings_names_uniqueids.csv')

print('export of cleaned up table done')
