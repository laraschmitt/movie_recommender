from flask import Flask, render_template, request, flash
from nmf_recommender import get_NMF_recommendations

app = Flask(__name__)
app.secret_key = b'need_this_for_message_flashing'


@ app.route('/')
@ app.route('/index')
def index():
    return render_template('index.html')


@ app.route('/recommender')
def recommender():
    return render_template('recommender.html')


@ app.route('/results')
def results():
    user_input = request.args

    movie_list = get_NMF_recommendations(user_input)
    return render_template('results.html', movies=movie_list)


if __name__ == '__main__':
    app.run()
