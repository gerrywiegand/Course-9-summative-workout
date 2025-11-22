from flask_sqlalchemy import SQLAlchemy  # noqa: I001
from sqlalchemy.orm import validates  # noqa: F401

db = SQLAlchemy()

# Define Models here


class Exercise(db.Model):
    __tablename__ = "exercise"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    category = db.Column(db.String(80), nullable=False)
    equipment_needed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Exercise {self.name}>"


class Workout(db.Model):
    __tablename__ = "workout"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text(200))

    def __repr__(self):
        return f"<Workout {self.date} - {self.duration_minutes} mins>"


class WorkoutExercise(db.Model):
    __tablename__ = "workout_exercise"
    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey("workout.id"), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey("exercise.id"), nullable=False)
    reps = db.Column(db.Integer, nullable=True)
    sets = db.Column(db.Integer, nullable=True)
    duration_seconds = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"<WorkoutExercise Workout ID: {self.workout_id}, Exercise ID: {self.exercise_id}>"
