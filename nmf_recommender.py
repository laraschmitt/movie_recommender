import pandas as pd
from sklearn.decomposition import NMF
import numpy as np
from fuzzywuzzy import process
import pickle

# Example:
# result = get_NMF_recommendations('Titanic', 'Toy Story', 'Star Wars', 3, 4, 5)


def get_NMF_recommendations(title1, title2, title3, rat1, rat2, rat3):
    """ Function that outputs 3 movie recommendations based on the user input 
    of 3 films that they have watched and the user's rating of these films"""

    # load df containing the movie names
    df = pd.read_csv(
        './data/ml-latest-small/dev_ds_ratings_names_uniqueids.csv')

    # load pretrained model from disk
    m = pickle.load(open('NMF_model.sav', 'rb'))
    print('model loaded')

    # construct title dict
    title_dict = dict(zip(df.title, df.movieId_unique))

    # get title list
    title_list = df['title'].to_list()

    # USER INPUT PROCESSING:
    print('fuzzy matching of user input started ...')
    choices = []
    for title_fuzz in [title1, title2, title3]:
        selection = process.extractOne(title_fuzz, title_list)
        choices.append(selection[0])

    print('fuzzy matching of user input finished!')

    keys = [title_dict.get(key) for key in choices]

    # create ratings dict
    d_fill = dict(zip(keys, [rat1, rat2, rat3]))

    # create dictionary for user
    dict_new_user = dict.fromkeys(df.movieId_unique, 0)
    dict_new_user.update(d_fill)

    # transform into an array/ vector of the values and reshape
    user_arr = (np.array(list(dict_new_user.values()))).reshape(1, 9719)

    # generate user_profile via nmf.transform(user_array)
    user_P = m.transform(user_arr)

    # PREDICTION:
    print('Start prediction for user')

    Q = m.components_
    # constract ratings matrix for this user
    # np.dot(user_profile, nmf.components_)
    user_R = (np.dot(user_P, Q))[0]

    # zip into tuples of rating and film title
    # remove the first three ones (the films that the user has already seen):
    recs = list(zip(user_R, df.title.values))

    # remove the first three ones (the films that the user has already seen):
    rec = (list(zip(user_R, df.title.values)))[3:]

    # sort by rating
    sorted_top_3_rec = sorted(rec, key=lambda x: x[0], reverse=True)[:3]

    # return only movie names of the tuples
    return [x[1] for x in sorted_top_3_rec]


result = get_NMF_recommendations('Titanic', 'Toy Story', 'Star Wars', 3, 4, 5)
print(result)
