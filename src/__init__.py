from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Creating main app and SQLite database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)

from src import models, routes