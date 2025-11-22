#!/usr/bin/env python3
from datetime import date as dt_date

from app import app
from models import *

with app.app_context():
    # Clear existing data
    print("Clearing existing data...")
    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()

    # Seed Exercises
    print("Seeding exercises...")
    exercise1 = Exercise(
        name="Barbell Back Squat", category="Strength", equipment_needed=True
    )
    exercise2 = Exercise(name="Deadlift", category="Strength", equipment_needed=True)
    exercise3 = Exercise(name="Running", category="Cardio", equipment_needed=False)

    # Seed Workouts
    print("Seeding workouts...")
    workout1 = Workout(
        date=dt_date(2024, 1, 10), duration_minutes=60, notes="Leg day workout"
    )
    workout2 = Workout(
        date=dt_date(2024, 1, 12), duration_minutes=45, notes="Full body workout"
    )

    # add to session
    db.session.add_all([exercise1, exercise2, exercise3, workout1, workout2])
    db.session.commit()

    # link exercises to workouts
    print("Linking exercises to workouts...")
    we1 = WorkoutExercise(
        workout_id=workout1.id, exercise_id=exercise1.id, sets=4, reps=8
    )
    we2 = WorkoutExercise(
        workout_id=workout1.id, exercise_id=exercise2.id, sets=4, reps=6
    )
    we3 = WorkoutExercise(
        workout_id=workout2.id, exercise_id=exercise1.id, sets=3, reps=10
    )
    we4 = WorkoutExercise(
        workout_id=workout2.id, exercise_id=exercise3.id, sets=1, duration_seconds=1800
    )  # reps=0 for cardio

    db.session.add_all([we1, we2, we3, we4])
    db.session.commit()
    print("Seeding completed.")
