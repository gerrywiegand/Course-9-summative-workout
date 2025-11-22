from flask_sqlalchemy import SQLAlchemy  # noqa: I001
from sqlalchemy.orm import validates  # noqa: F401
from datetime import date as dt_date

db = SQLAlchemy()

# Define Models here


class Exercise(db.Model):
    __tablename__ = "exercise"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    category = db.Column(db.String(80), nullable=False)
    equipment_needed = db.Column(db.Boolean, default=False)

    workout_exercises = db.relationship(
        "WorkoutExercise", back_populates="exercise", cascade="all, delete-orphan"
    )
    workouts = db.relationship(
        "Workout",
        secondary="workout_exercise",
        back_populates="exercises",
        viewonly=True,
    )

    @validates("name")
    def validate_name(self, key, name):
        if not name or len(name) < 3:
            raise ValueError("Exercise name must be at least 3 characters long.")
        return name

    def __repr__(self):
        return f"<Exercise {self.name}>"


class Workout(db.Model):
    __tablename__ = "workout"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text, nullable=True)

    workout_exercises = db.relationship(
        "WorkoutExercise", back_populates="workout", cascade="all, delete-orphan"
    )
    exercises = db.relationship(
        "Exercise",
        secondary="workout_exercise",
        back_populates="workouts",
        viewonly=True,
    )

    @validates("date")
    def validate_date(self, key, date):

        if date > dt_date.today():
            raise ValueError("Workout date cannot be in the future.")
        return date

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

    workout = db.relationship("Workout", back_populates="workout_exercises")
    exercise = db.relationship("Exercise", back_populates="workout_exercises")

    @validates("reps", "sets", "duration_seconds")
    def validate_positive_integers(self, key, value):
        if value is not None and value < 0:
            raise ValueError(f"{key} must be a positive integer.")
        return value

    def __repr__(self):
        return f"<WorkoutExercise Workout ID: {self.workout_id}, Exercise ID: {self.exercise_id}>"
