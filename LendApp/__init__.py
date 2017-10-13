from flask import Flask
app = Flask(__name__)
from LendApp.views import *


if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=5000)

