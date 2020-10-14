import random

MOVIES = ['Toy Story 1',
          'Toy Story 2'
          'Toy Story 3',
          'Inception',
          'Shawshank Redemption',
          'Iron Sky',
          'Dark Sky',
          'Skyfall',
          'Vanilla Sky',
          'Sky City',
          'I love the Sky',
          'The Big LebowSKY']


def random_recommender(num):
    result = random.choices(MOVIES, k=num)
    return result


def nmf_recommender():
    pass


def other_recommender():
    pass
