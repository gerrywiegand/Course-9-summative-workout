from flask import Flask, make_response, request  # noqa: F401, I001
from flask_migrate import Migrate
from marshmallow import ValidationError  # noqa: F401

from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

migrate = Migrate(app, db)

db.init_app(app)

# Define Routes here


@app.route("/")
def home():
    return make_response("<h1>Welcome to the Workout Tracker API</h1>", 200)


@app.route("/exercises", methods=["GET"])
def get_exercises():
    exercises = Exercise.query.all()
    schema = ExerciseSchema(many=True)
    body = schema.dump(exercises)
    return make_response(body, 200)


@app.route("/exercises/<int:id>", methods=["GET"])
def get_exercise(id):
    schema = ExerciseDetailSchema()
    exercise = Exercise.query.filter_by(id=id).first()
    if exercise:
        body = schema.dump(exercise)
        return make_response(body, 200)
    else:
        return make_response({"error": "Exercise not found"}, 404)


@app.route("/exercises", methods=["POST"])
def create_exercise():
    schema = ExerciseSchema()
    try:
        data = schema.load(request.get_json())
        new_exercise = Exercise(**data)
        db.session.add(new_exercise)
        db.session.commit()
        body = schema.dump(new_exercise)
        return make_response(body, 201)
    except ValidationError as e:
        return make_response({"errors": e.messages}, 400)


@app.route("/exercises/<int:id>", methods=["DELETE"])
def delete_exercise(id):
    exercise = Exercise.query.filter_by(id=id).first()
    if exercise:
        db.session.delete(exercise)
        db.session.commit()
        return make_response("", 204)
    else:
        return make_response({"error": "Exercise not found"}, 404)


@app.route("/workouts", methods=["GET"])
def get_workouts():
    workouts = Workout.query.all()
    schema = WorkoutSchema(many=True)
    body = schema.dump(workouts)
    return make_response(body, 200)


@app.route("/workouts/<int:id>", methods=["GET"])
def get_workout(id):
    schema = WorkoutDetailSchema()
    workout = Workout.query.filter_by(id=id).first()
    if workout:
        body = schema.dump(workout)
        return make_response(body, 200)
    else:
        return make_response({"error": "Workout not found"}, 404)


@app.route("/workouts", methods=["POST"])
def create_workout():
    schema = WorkoutSchema()
    try:
        data = schema.load(request.get_json())
        new_workout = Workout(**data)
        db.session.add(new_workout)
        db.session.commit()
        body = schema.dump(new_workout)
        return make_response(body, 201)
    except ValidationError as e:
        return make_response({"errors": e.messages}, 400)


@app.route("/workouts/<int:id>", methods=["DELETE"])
def delete_workout(id):
    workout = Workout.query.filter_by(id=id).first()
    if workout:
        db.session.delete(workout)
        db.session.commit()
        return make_response("", 204)
    else:
        return make_response({"error": "Workout not found"}, 404)


@app.route(
    "/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises",
    methods=["POST"],
)
def add_exercise_to_workout(workout_id, exercise_id):
    schema = WorkoutExerciseSchema()
    try:
        workout = Workout.query.filter_by(id=workout_id).first()
        exercise = Exercise.query.filter_by(id=exercise_id).first()
        if not workout:
            return make_response({"error": "Workout not found"}, 404)
        if not exercise:
            return make_response({"error": "Exercise not found"}, 404)
        data = schema.load(request.get_json())
        workout_exercise = WorkoutExercise(
            workout_id=workout.id,
            exercise_id=exercise.id,
            reps=data.get("reps"),
            sets=data.get("sets"),
            duration_seconds=data.get("duration_seconds"),
        )
        db.session.add(workout_exercise)
        db.session.commit()
        body = schema.dump(workout_exercise)
        return make_response(body, 201)
    except ValidationError as e:
        return make_response({"errors": e.messages}, 400)


if __name__ == "__main__":
    app.run(port=5555, debug=True)
