__author__ = 'jayanthvenkataraman'

from flask import Flask

app = Flask(__name__)


@app.route('/', methods = ['GET'])
def index():
    return "Heroku Flask application Successfully deployed"

if __name__ == "__main__":
    app.run()