import pandas as pd
import numpy as np
from fuzzywuzzy import process
import pickle

model_path = './NMF_model.sav'
df_path = './dev_ds_ratings_names_uniqueids.csv'


def get_NMF_recommendations(user_input):
    """ Function that outputs 3 movie recommendations based on the user input
    of 3 films that they have watched and the user's rating of these films"""

    # load df containing the movie names
    df = pd.read_csv(df_path)

    # load pretrained model from disk
    m = pickle.load(open(model_path, 'rb'))
    print('model loaded')

    # construct title dict
    title_dict = dict(zip(df.title, df.movieId_unique))

    # get title list
    title_list = df['title'].to_list()

    # USER INPUT PROCESSING:
    print('fuzzy matching of user input started ...')
    choices = []
    for title_fuzz in [user_input['movie1'], user_input['movie2'],
                       user_input['movie3']]:
        selection = process.extractOne(title_fuzz, title_list)
        choices.append(selection[0])

    print('fuzzy matching of user input finished!')

    keys = [title_dict.get(key) for key in choices]

    # create ratings dict
    d_fill = dict(zip(keys, [user_input['rating1'],
                             user_input['rating2'], user_input['rating3']]))

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
    rec = (list(zip(user_R, df.title.values)))[3:]

    # sort by rating
    sorted_top_3_rec = sorted(rec, key=lambda x: x[0], reverse=True)[:3]

    # return only movie names of the tuples
    return [x[1] for x in sorted_top_3_rec]
