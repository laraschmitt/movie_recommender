from nmf_recommender import get_NMF_recommendations


def test_nmf_model():
    """ Function to test whether the result is a list of strings"""
    recs = get_NMF_recommendations({
        'movie1': 'Titanic',
        'movie2': 'Toy Story',
        'movie3': 'Star Wars',
        'rating1': 4,
        'rating2': 4,
        'rating3': 5,
    })
    assert recs == [
        'Payback (1999)', 'Lady and the Tramp (1955)', 'Exit to Eden (1994)']
