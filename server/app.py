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
    schema = ExerciseSchema()
    exercise = Exercise.query.filter_by(id)
    if exercise:
        body = schema.dump(exercise)
        return make_response(body, 200)
    else:
        return make_response({"error": "Exercise not found"}, 404)


@app.route("/exercises", methods=["POST"])
def create_exercise():
    pass  # Implementation goes here


@app.route("/exercises/<int:id>", methods=["DELETE"])
def delete_exercise(id):
    pass  # Implementation goes here


@app.route("/workouts", methods=["GET"])
def get_workouts():
    pass  # Implementation goes here


@app.route("/workouts/<int:id>", methods=["GET"])
def get_workout(id):
    pass  # Implementation goes here


@app.route("/workouts", methods=["POST"])
def create_workout():
    pass  # Implementation goes here


@app.route("/workouts/<int:id>", methods=["DELETE"])
def delete_workout(id):
    pass  # Implementation goes here


@app.route(
    "/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises",
    methods=["POST"],
)
def add_exercise_to_workout(workout_id, exercise_id):
    pass  # Implementation goes here


if __name__ == "__main__":
    app.run(port=5555, debug=True)
