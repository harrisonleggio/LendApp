from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:k7v912zq6y@localhost/LendAFriend'
db = SQLAlchemy(app)

SQLALCHEMY_TRACK_MODIFICATIONS = False
from LendApp.views import *
from LendApp.models import *


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, threaded=True, port=5000)

