"""
Write a Python program that converts the two list
to the correct sentences and prints them.
"""

left = [
    'Outlier or anomaly detection is used',
    'Principal Component Analysis (PCA) is a method',
    'Principal Component Analysis (PCA) is frequently used',
    'There are many clustering methods',
    'Non-negative Matrix Factorization (NMF) is an algorithm',
    'Most clustering algorithms are based on a distance metric',
    'Gaussian Mixture Models (GMM) are a generative model',
    'Unsupervised learning is a family of machine learning methods',
    'The "curse of dimensionality" is a problem',
    't-SNE reduces data to two dimensions'
]

right = [
    'frequently used in recommender systems and customer segmentation.',
    'to visualize complex datasets.',
    'that becomes worse the more features you have.',
    'to identify credit card fraud.',
    'for dimensionality reduction.',
    'e.g. Euclidean or Manhatten distance.',
    'that do not require labled data.',
    'for detecting outliers.',
    'as part of a supervised learning pipeline.',
    'like K-means, DBSCAN or Ward.'
]

'Outlier or anomaly detection is used to identify credit card fraud.'

'Principal Component Analysis (PCA) is frequently used for dimensionality reduction.'

'There are many clustering methods like K-means, DBSCAN or Ward.'

'Non-negative Matrix Factorization (NMF) is an algorithm frequently used in recommender systems and customer segmentation.'

'Most clustering algorithms are based on a distance metric e.g. Euclidean or Manhatten distance.'

'Gaussian Mixture Models (GMM) are a generative model for detecting outliers.'

'Unsupervised learning is a family of machine learning methods that do not require labled data.'

'The "curse of dimensionality" is a problem that becomes worse the more features you have.'

't-SNE reduces data to two dimensions to visualize complex datasets.'


for i in range(10):
    print(i)
    print(left[i])
    print(right[i])
