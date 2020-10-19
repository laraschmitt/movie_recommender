from scriptname import functionname


def test_result_string():
    """ Function to test whether the result is a list of strings"""
    recs = get_recommendations('Titanic (1999)')
    assert recs is ['Avatar (2011)']
