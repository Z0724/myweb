import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)


app.config['SECRET_KEY']= 'ffsdfsddsbr'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False




