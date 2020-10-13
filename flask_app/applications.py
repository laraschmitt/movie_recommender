from flask import Flask
from flask import render_template
app = Flask(__name__)
# instantiating a flask application
# "__name__" is a reference to the current script (application.py)

# decorator function. It means trigger/ execute the hello function
# any time somebody visits "mywebsite:port/home"


# @app.route('/')
# @app.route('/name/<name>')
# def hello(name):
#     text = """
#     <h1>Hello from {name}</h1>
#     <br>
#     <p>This is a great recommender.</p>
#     <a href='/recommender'>Get a Movie Recommendation!</a>
#     """
#     return text

# HTTP request (e.g. clicking link) triggers route function, which renders HTML


# @app.route('/recommender')
# def rec():
#     return """I recommend that you watch Toy story!
#     <a href='/'>Go back home!</a>
#     """

@app.route('/')
def hello():
    return render_template('index.hmtl')


@app.route('/recommender')
def rec():
    return render_template('recommender.hmtl')


if __name__ == "__main__":
    # if I literally run "python application.py" please tun the following code
    # BUT, do NOT execute any of the code below if I am IMPORTING application.py
    app.run(debug=True)
