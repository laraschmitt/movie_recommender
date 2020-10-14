from flask import Flask, render_template, request
import ml_model

app = Flask(__name__)
# instantiating a flask application
# "__name__" is a reference to the current script (application.py)

# decorator function. It means trigger / execute the hello function
# any time somebody visits "mywebsite:port/home"


# @app.route('/')
# @app.route('/name/<name>')
# def hello(name):
#     text = f"""
#     <h1>Hello from {name}!</h1>
#     <br>
#     <p>This is a great recommender.</p>
#     <a href='/recommender'>Get a Movie Recommendation!</a>
#     """
#     return text

# HTTP request (e.g. clicking link) triggers route function, which renders HTML

@app.route('/')
def hello():
    return render_template('index.html')
    # automatically looking for templates/index.html


@app.route('/recommender')
def rec():

    user_input = dict(request.args)
    # WE CAN GET THE INFORMATION FROM THE FORM HERE^^^^

    # user_input is a dictionary -> {'html_name_attribute':'user value'}
    movie_titles = list(user_input.values())[::2]
    ratings = list(user_input.values())[1::2]
    # print(movie_titles)
    # print(ratings)

    # YOUR JOB is to take the user input and pass it into a function that does the recommendation

    # 1. Train the model (or we read in a pre-trained model)
    # 2. Process the input (e.g. convert everything to numbers, movie titles -> column numbers)
    # 3. Make the user input into an array of length len(df.columns)
    # 4. user_profile = nmf.transform(user_array)
    # 5. result = np.dot(user_profile, nmf.components_)
    # 6. Sort array, map the top 3 values to Movies.
    # 7. Return final movies

    # BONUS: INSERT new user data into database.

    # results = ml_model.nmf(movie_titles, ratings)

    results = ml_model.random_recommender(3)
    return render_template('recommender.html',
                           results_html=results,
                           movie_titles=movie_titles,
                           ratings=ratings)


if __name__ == '__main__':
    # if I literally run "python application.py" please run the following code.
    # BUT, do NOT execute any of the code below if I am IMPORTING application.py
    app.run(debug=True)
