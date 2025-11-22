# Workout Tracker API

## Description

A backend API for tracking workouts and exercises. Built with Flask, SQLAlchemy, and Marshmallow, this application provides a RESTful API for creating and managing exercises, workouts, and linking exercises to workouts with specific sets, reps, or duration.

## Features

- Create and manage exercises with categories and equipment requirements
- Create and manage workouts with dates, duration, and notes
- Link exercises to workouts with specific metrics (reps/sets or duration)
- Comprehensive validation at database, model, and schema levels
- Full CRUD operations for exercises and workouts
- Relational database design with many-to-many relationships

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd Course-9-summative-workout
   ```

2. **Install dependencies:**

   ```bash
   pipenv install
   ```

3. **Activate the virtual environment:**

   ```bash
   pipenv shell
   ```

4. **Navigate to the server directory:**

   ```bash
   cd server
   ```

5. **Initialize and set up the database:**

   ```bash
   flask db upgrade
   ```

6. **Seed the database with sample data:**
   ```bash
   python seed.py
   ```

## Running the Application

1. **Start the Flask development server:**

   ```bash
   cd server
   python app.py
   ```

2. **The API will be available at:**
   ```
   http://localhost:5555
   ```

## API Endpoints

### Exercise Endpoints

#### `GET /exercises`

- **Description:** Retrieve all exercises
- **Response:** 200 status with array of exercise objects

#### `GET /exercises/<id>`

- **Description:** Retrieve a single exercise by ID
- **Response:** 200 status with exercise object, or 404 if not found

#### `POST /exercises`

- **Description:** Create a new exercise
- **Request Body:**
  ```json
  {
    "name": "Push-ups",
    "category": "Strength",
    "equipment_needed": false
  }
  ```
- **Response:** 201 Created with created exercise object

#### `DELETE /exercises/<id>`

- **Description:** Delete an exercise by ID
- **Response:** 204 No Content, or 404 if not found

---

### Workout Endpoints

#### `GET /workouts`

- **Description:** Retrieve all workouts
- **Response:** 200 status with array of workout objects

#### `GET /workouts/<id>`

- **Description:** Retrieve a single workout by ID
- **Response:** 200 status with workout object, or 404 if not found

#### `POST /workouts`

- **Description:** Create a new workout
- **Request Body:**
  ```json
  {
    "date": "2025-11-22",
    "duration_minutes": 60,
    "notes": "Morning workout session"
  }
  ```
- **Response:** 201 Created with created workout object

#### `DELETE /workouts/<id>`

- **Description:** Delete a workout by ID
- **Response:** 204 No Content, or 404 if not found

---

### Workout Exercise Endpoints

#### `POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises`

- **Description:** Add an exercise to a workout with specific metrics
- **Request Body (for strength exercises):**
  ```json
  {
    "reps": 10,
    "sets": 3
  }
  ```
- **Request Body (for cardio exercises):**
  ```json
  {
    "duration_seconds": 1800
  }
  ```
- **Response:** 201 Created with created workout-exercise relationship object
- **Note:** Must provide either reps/sets OR duration_seconds

## Validation Rules

### Exercise Validations

- Name must be at least 3 characters long
- Name must be unique
- Category must be at least 3 characters long

### Workout Validations

- Date cannot be in the future
- Duration must be a positive integer (greater than 0)
- Warning issued if duration exceeds 180 minutes (3 hours)

### Workout Exercise Validations

- Must provide either reps/sets OR duration_seconds
- If provided, reps, sets, and duration_seconds must be positive integers

## Database Schema

### Models

- **Exercise:** id, name, category, equipment_needed
- **Workout:** id, date, duration_minutes, notes
- **WorkoutExercise:** id, workout_id, exercise_id, reps, sets, duration_seconds

### Relationships

- Many-to-many relationship between Workouts and Exercises through WorkoutExercise join table
- Cascade deletes configured for related records

## Technologies Used

- **Flask:** Web framework
- **SQLAlchemy:** ORM for database management
- **Flask-Migrate:** Database migration management
- **Marshmallow:** Serialization/deserialization and validation
- **SQLite:** Database (development)

```

```
