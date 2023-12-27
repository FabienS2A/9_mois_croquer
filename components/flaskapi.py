#First we imported the Flask class. An instance of this class will be our WSGI application.

from flask import Flask


#Next we create an instance of this class. The first argument is the name of the application’s module or package.

app = Flask(__name__)

#We then use the route() decorator to tell Flask what URL should trigger our function


@app.route("/")
def hello():
    return "<p>Hello, World!</p>"

