from flask_sqlalchemy import SQLAlchemy, Date  # noqa: I001
from sqlalchemy.orm import validates  # noqa: F401

db = SQLAlchemy()

# Define Models here


class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    equipment_needed = db.Column(db.boolean, default=False)

    def __repr__(self):
        return f"<Exercise {self.name}>"


class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(Date, nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.String(200))
