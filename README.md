# UserDemo - FastAPI User API

A beginner project to learn FastAPI basics: routes, Pydantic models, status codes and exception handling.

## Features
- Create and fetch users
- Request validation with Pydantic
- Response models (password is never returned)
- `HTTPException` for 404 errors

## Tech Stack
- Python 3
- FastAPI
- Uvicorn

## Setup
1. Clone the repo and open the folder
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `source venv/Scripts/activate` (Git Bash on Windows)
4. Install packages: `pip install fastapi uvicorn`
5. Run the app: `uvicorn main:app --reload`

Open `http://127.0.0.1:8000/docs` for the interactive Swagger UI.

## Endpoints
| Method | Route | Description |
|--------|-------|-------------|
| POST | `/create_user` | Create a new user (201) |
| GET | `/get_all_users` | List all users |
| GET | `/get_user/{user_id}` | Get one user by id |

## Sample Request
`POST /create_user`
```json
{
  "id": 1,
  "name": "Priyanka",
  "email": "prinks@example.com",
  "age": 23,
  "password": "StrongPass@123"
}
```

## Error Handling
| Case | Status |
|------|--------|
| User not found | 404 |
| Invalid (negative) id | 400 |
| Invalid request body | 422 (automatic) |
| Unexpected error | 500 |

## Notes
- Data is stored in a Python list, so it resets on every restart
- Passwords are stored as plain text here, which is for learning only

## Future Improvements
- Add a real database (SQLAlchemy)
- Hash passwords
- Add update and delete endpoints
- Add JWT authentication
- Write tests with `pytest`