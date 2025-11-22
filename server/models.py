from flask_sqlalchemy import SQLAlchemy  # noqa: I001
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
