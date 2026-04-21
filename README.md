# 🔐 Authentication Service

A production-ready authentication microservice built with FastAPI, SQLAlchemy, and JWT tokens. This service provides secure user registration, login, and JWT-based authentication.

## ✨ Features

- ✅ User registration with email validation
- ✅ Secure password hashing using bcrypt
- ✅ JWT token generation and verification
- ✅ SQLite database (easily swappable with PostgreSQL/MySQL)
- ✅ Automatic API documentation (Swagger UI & ReDoc)
- ✅ Modular architecture for scalability
- ✅ Type hints for better code quality

## 🏗️ Tech Stack

- **FastAPI** - Modern web framework
- **SQLAlchemy** - ORM for database operations
- **Pydantic** - Data validation
- **python-jose** - JWT token handling
- **passlib** - Password hashing with bcrypt
- **SQLite** - Database (development)

## 📁 Project Structure
auth-service/
│
├── app/
│ ├── init.py
│ ├── main.py # Application entry point
│ ├── database.py # Database configuration
│ ├── models.py # SQLAlchemy models
│ ├── schemas.py # Pydantic schemas
│ ├── services.py # Business logic
│ ├── auth.py # Authentication utilities
│ │
│ └── routers/
│ ├── init.py
│ └── auth.py # Authentication endpoints
│
├── requirements.txt # Python dependencies
└── README.md # Project documentation

text

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd auth-service
Create and activate virtual environment

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies

bash
pip install -r requirements.txt
Run the application

bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
Access the API

Main API: http://localhost:8000

Interactive Docs: http://localhost:8000/docs

Alternative Docs: http://localhost:8000/redoc

📚 API Endpoints
Health Check
http
GET /
Response:

json
{
    "message": "Auth Service running 🔐"
}
Register User
http
POST /auth/register
Content-Type: application/json

{
    "email": "user@example.com",
    "password": "securepass123"
}
Success Response (200):

json
{
    "message": "User created",
    "user_id": 1
}
Error Response (400):

json
{
    "detail": "Email already exists"
}
Login
http
POST /auth/login
Content-Type: application/json

{
    "email": "user@example.com",
    "password": "securepass123"
}
Success Response (200):

json
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "bearer"
}
Error Response (401):

json
{
    "detail": "Invalid credentials"
}
🧪 Testing with cURL
Register a user
bash
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"test123"}'
Login
bash
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"test123"}'
Use token in authenticated requests
bash
curl -X GET http://localhost:8000/protected-endpoint \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN_HERE"
🗄️ Database
The service uses SQLite by default. The database file auth.db will be created automatically in the project root.

Switching to PostgreSQL
Install psycopg2:

bash
pip install psycopg2-binary
Update database.py:

python
DATABASE_URL = "postgresql://user:password@localhost/dbname"
🔒 Environment Variables
Create a .env file in the project root:

env
# JWT Configuration
SECRET_KEY=your-super-secret-key-change-this-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

# Database Configuration
DATABASE_URL=sqlite:///./auth.db

# Environment
ENV=development
Update auth.py to use environment variables:


import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "default-secret-key")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))


# 📦 Dependencies
- Create requirements.txt with:

fastapi==0.104.1
uvicorn[standard]==0.24.0
sqlalchemy==2.0.23
pydantic==2.5.0
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-dotenv==1.0.0


# 🛡️ Security Best Practices
1. Never commit secrets - Use environment variables
2. Use strong secret keys - Generate with: openssl rand -hex 32
3. Always hash passwords - Never store plain text passwords
4. Use HTTPS in production - Never send tokens over HTTP
5. Short token expiration - Default 60 minutes, adjust based on needs
6. Rate limiting - Protect against brute force attacks
7. Input validation - All inputs are validated with Pydantic