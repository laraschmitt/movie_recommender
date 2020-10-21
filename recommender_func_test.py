from nmf_recommender import get_NMF_recommendations


def test_nmf_model():
    """ Function to test whether the result is a list of strings"""
    recs = get_NMF_recommendations(
        'Titanic', 'Toy Story', 'Star Wars', 3, 4, 5)
    assert recs == [
        'Payback (1999)', 'Lady and the Tramp (1955)', 'Exit to Eden (1994)']
