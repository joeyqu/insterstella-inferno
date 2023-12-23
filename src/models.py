import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime, func

db = SQLAlchemy()

class Score(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    time_created = db.Column(DateTime(timezone=True), server_default=func.now())
    time_updated = db.Column(DateTime(timezone=True), onupdate=func.now())

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return json.dumps(self.as_dict(), indent=4, sort_keys=True, default=str)
    

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String,nullable=False)
    subtitle = db.Column(db.String,nullable=False)
    img = db.Column(db.String,default="https://via.placeholder.com/300")
    type = db.Column(db.String,nullable=False) # company or game name _ seperated

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return json.dumps(self.as_dict(), indent=4, sort_keys=True, default=str)