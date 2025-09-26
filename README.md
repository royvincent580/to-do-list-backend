# To-Do List Backend

A Flask REST API backend for a collaborative to-do list application with user authentication, task management, and tagging system.

## Features

- User authentication with JWT tokens
- Task CRUD operations
- Tag management
- User collaboration on tasks
- Admin functionality
- SQLite database with migrations

## Setup

### Prerequisites
- Python 3.7+
- pipenv

### Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pipenv install
   ```

3. Activate virtual environment:
   ```bash
   pipenv shell
   ```

4. Run database migrations:
   ```bash
   flask --app application.py db upgrade
   ```

5. (Optional) Seed the database:
   ```bash
   python seed.py
   ```

## Running the Application

1. Activate virtual environment:
   ```bash
   pipenv shell
   ```

2. Start the server:
   ```bash
   flask --app application.py run --debug
   ```

3. The API will be available at `http://localhost:5000`

## Accessing in Browser

Open Chrome/Firefox and visit:
- `http://localhost:5000/docs` - Swagger API documentation
- `http://localhost:5000/api/v1/users` - Users endpoint
- `http://localhost:5000/api/v1/tasks` - Tasks endpoint (requires JWT token)
- `http://localhost:5000/api/v1/tags` - Tags endpoint
- `http://localhost:5000/api/v1/auth/register` - Register endpoint
- `http://localhost:5000/api/v1/auth/login` - Login endpoint

## API Endpoints

### Authentication
- `POST /api/v1/auth/register` - Register new user
- `POST /api/v1/auth/login` - User login

### Users
- `GET /api/v1/users` - Get all users
- `GET /api/v1/users/{id}` - Get user by ID

### Tasks
- `GET /api/v1/tasks` - Get all tasks
- `POST /api/v1/tasks` - Create new task
- `GET /api/v1/tasks/{id}` - Get task by ID
- `PUT /api/v1/tasks/{id}` - Update task
- `DELETE /api/v1/tasks/{id}` - Delete task

### Tags
- `GET /api/v1/tags` - Get all tags
- `POST /api/v1/tags` - Create new tag

### User Tasks (Collaboration)
- Task assignment and collaboration endpoints

### Admin
- Admin-specific endpoints for user management

## Environment Variables

Create a `.env` file with:
```
JWT_SECRET_KEY=your_secret_key_here
```

## Project Structure

```
flaskr/
├── controllers/     # Business logic
├── models/         # Database models
├── routes/         # API route definitions
├── schemas/        # Request/response schemas
├── db.py          # Database configuration
├── extensions.py  # Flask extensions
└── utils.py       # Utility functions
```

## Technologies Used

- Flask
- Flask-Smorest (API documentation)
- Flask-SQLAlchemy (ORM)
- Flask-Migrate (Database migrations)
- Flask-JWT-Extended (Authentication)
- Flask-CORS (Cross-origin requests)
- SQLite (Database)
