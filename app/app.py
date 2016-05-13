__author__ = 'jayanthvenkataraman'

from flask import Flask
import os

app = Flask(__name__)


@app.route('/', methods = ['GET'])
def index():
    return "Heroku Flask application Successfully deployed"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)