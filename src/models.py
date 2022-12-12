from datetime import datetime
from src import db

# Our object in the database


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)
    day = db.Column(db.DateTime, default=datetime.utcnow)

    # Getting objects ID from the database
    def __repr__(self):
        return '<Article %r>' % self.id
