# FastAPI Verification Code System

A FastAPI-based verification system that integrates with Telegram for user authentication and verification.

## Features

- User registration with phone number
- Telegram bot integration for verification code delivery
- Secure verification code generation and validation
- Async database operations using SQLAlchemy
- RESTful API endpoints for user management

## Tech Stack

- FastAPI - Web framework
- SQLAlchemy - Database ORM
- aiogram - Telegram bot framework
- asyncpg - Async PostgreSQL driver
- Pydantic - Data validation
- Python-dotenv - Environment variable management

## Prerequisites

- Python 3.8+
- PostgreSQL database
- Telegram Bot Token (from BotFather)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd fastapi_verificationcode
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file based on `.env.dist`:
```bash
cp .env.dist .env
```

5. Configure your environment variables in `.env`:
```
DB_URL=postgresql+asyncpg://user:password@localhost:5432/dbname
CODE_TOKEN_EXPIRE_MINUTES=15
BOT_TOKEN=your_telegram_bot_token
```

## Project Structure

```
.
├── main.py              # FastAPI application and routes
├── crud.py              # Database operations
├── models.py            # SQLAlchemy models
├── schemas.py           # Pydantic models
├── database.py          # Database configuration
├── config.py            # Application configuration
├── tg_bot/              # Telegram bot implementation
├── utils/               # Utility functions
└── requirements.txt     # Project dependencies
```

## API Endpoints

- `POST /register` - Register a new user and send verification code
- `POST /verify` - Verify user with the received code
- `GET /check_user` - Check if a user is verified

## Usage

1. Start the FastAPI server:
```bash
uvicorn main:app --reload
```

2. The server will be available at `http://localhost:8000`

3. Use the Telegram bot to interact with the verification system

## API Documentation

Once the server is running, you can access:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.