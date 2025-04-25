FastAPI Telegram Verification Bot
A modern FastAPI and aiogram 3.x project for user registration and verification via a Telegram bot. Users register by sharing their phone number, receive a 6-digit code, and verify by sending the code. Powered by PostgreSQL and async SQLAlchemy.
Features

📱 Register users via Telegram with phone number
🔒 Send and verify 6-digit codes
🗄️ Store user data in PostgreSQL
🚀 Async FastAPI with aiogram 3.x integration

Prerequisites

Python 3.11+
PostgreSQL
Telegram Bot Token (from @BotFather)

Setup

Clone the Repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name


Install Dependencies
pip install -r requirements.txt


Set Up PostgreSQL

Create a database named exam:psql -U postgres
CREATE DATABASE exam;




Configure Environment Variables

Create a .env file in the root directory:DB_URL=postgresql+asyncpg://postgres:your_password@localhost:5432/exam
ALGORITHM=HS256
CODE_TOKEN_EXPIRE_MINUTES=1
BOT_TOKEN=your_telegram_bot_token


Note: Do not commit .env to GitHub. Add it to .gitignore.


Run the FastAPI Server
uvicorn main:app --reload


Run the Telegram Bot

In a separate terminal:python -m telegram_bot.bot





Usage

Start the Telegram bot by sending /start.
Share your phone number (e.g., +998901234567).
Receive a 6-digit verification code.
Send the code to verify (e.g., 123456).

Project Structure

main.py: FastAPI application with /register and /verify endpoints.
telegram_bot/: aiogram bot logic (bot.py, handlers.py, keyboards.py).
crud.py: Database operations.
database.py: Async SQLAlchemy setup.
models.py: User model.
schemas.py: Pydantic schemas.
utils/: Code generation utility.

License
MIT License. See LICENSE for details.
Contributing
Feel free to open issues or submit pull requests!
