from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://HARRISONS-THINK/LendApp'
db = SQLAlchemy(app)

SQLALCHEMY_TRACK_MODIFICATIONS = False
from LendApp.views import *


if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=5000)

