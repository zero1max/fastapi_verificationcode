# 🚀 FastAPI Telegram Verification Bot

A modern **FastAPI** and **aiogram 3.x** project for user registration and verification via a **Telegram bot**.  
Users register by sharing their phone number, receive a 6-digit code, and verify by sending the code.  
Powered by **PostgreSQL** and **async SQLAlchemy**.

---

## ✨ Features

- 📱 Register users via Telegram with phone number  
- 🔒 Send and verify 6-digit codes  
- 🗄️ Store user data in PostgreSQL  
- ⚡ Async FastAPI with aiogram 3.x integration  

---

## ✅ Prerequisites

- Python 3.11+
- PostgreSQL
- Telegram Bot Token (from [@BotFather](https://t.me/BotFather))

---

## ⚙️ Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

### 2. Install Dependencies

```bash
pip install -r requirements.txt

### 3. Set Up PostgreSQL

Create a database named exam:

```bash
psql -U postgres
CREATE DATABASE exam;

## 🚀 Running the App
Run the FastAPI Server

```bash
uvicorn main:app --reload

Run the Telegram Bot

In a separate terminal:

```bash
python -m telegram_bot.bot

## 💬 Usage

    Start the bot on Telegram with /start.

    Share your phone number (e.g., +998901234567).

    Receive a 6-digit verification code.

    Send the code to verify (e.g., 123456).

## 🗂 Project Structure
.
├── main.py                # FastAPI application with /register and /verify endpoints
├── telegram_bot/
│   ├── bot.py             # Bot entrypoint
│   ├── handlers.py        # Handlers for bot messages and actions
│   └── keyboards.py       # Custom keyboards (e.g., for contact request)
├── crud.py                # Database operations
├── database.py            # Async SQLAlchemy setup
├── models.py              # User model
├── schemas.py             # Pydantic schemas
└── utils/                 # Code generation utility

📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to open issues or submit pull requests.