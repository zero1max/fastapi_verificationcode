from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

request_phone_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📞 Telefon raqamni yuborish", request_contact=True)]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

login_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Login")]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)