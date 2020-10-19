import pandas as pd
from sklearn.decomposition import NMF
import numpy as np
import pickle

# load cleaned up dataset
df = pd.read_csv('./data/ml-latest-small/dev_ds_ratings_names_uniqueids.csv')

# creating ratings matrix (R)
R = df.pivot_table(index='userId', columns='movieId_unique',
                   values='rating', dropna=False)

# fill nan values with median
med_values = R.median().median()
R.fillna(med_values, inplace=True)

# instantiate NMF model
m = NMF(n_components=20)

# fit model
m.fit(R)

# save the model to disk
filename = 'NMF_model.sav'
pickle.dump(m, open(filename, 'wb'))

print('NMF model sucessfully trained and saved to disk')
