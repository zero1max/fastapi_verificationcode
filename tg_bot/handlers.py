from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import httpx
import logging
#
from .keyboards import request_phone_keyboard


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


router = Router()

class UserState(StatesGroup):
    phone = State()
    code = State()

@router.message(CommandStart())
async def start_handler(msg: Message, state: FSMContext):
    logger.info(f"Received /start command from user {msg.from_user.id}")
    await msg.answer("Telefon raqamingizni kiriting (masalan, +998901234567):", reply_markup=request_phone_keyboard)
    await state.set_state(UserState.phone)

@router.message(UserState.phone, F.contact)
async def handle_phone_contact(message: Message, state: FSMContext):
    user_id = message.from_user.id
    phone_number = message.contact.phone_number
    logger.info(f"Received phone number via contact from user {user_id}: {phone_number}")

    # iOS ba'zida raqamni +998 bilan emas, 998 bilan yuboradi, to‘g‘rilaymiz:
    if not phone_number.startswith('+'):
        phone_number = '+' + phone_number

    await process_phone_number(message, state, user_id, phone_number)

@router.message(UserState.phone, F.text.regexp(r"^\+\d{10,15}$"))
async def handle_phone_text(message: Message, state: FSMContext):
    user_id = message.from_user.id
    phone_number = message.text
    logger.info(f"Received phone number via text from user {user_id}: {phone_number}")

    await process_phone_number(message, state, user_id, phone_number)

@router.message(UserState.phone)
async def invalid_phone(message: Message):
    logger.info(f"Invalid phone number received from user {message.from_user.id}: {message.text}")
    await message.answer("Noto'g'ri telefon raqami. Iltimos, quyidagi formatdan foydalaning: +998901234567 yoki 'Telefon raqamni yuborish' tugmasini bosing.")

async def process_phone_number(message: Message, state: FSMContext, user_id: int, phone_number: str):
    try:
        async with httpx.AsyncClient() as client:
            logger.info(f"Sending POST request to /register for user {user_id}")
            response = await client.post(
                "http://localhost:8000/register",
                json={"telegram_id": user_id, "phone_number": phone_number}
            )
            logger.info(f"Received response from /register: status={response.status_code}, body={response.json()}")

            if response.status_code == 200:
                await message.answer("Tasdiqlash kodi yuborildi. Iltimos, 6 raqamli kodni kiriting (masalan, 123456).")
                await state.set_state(UserState.code)
            else:
                error_detail = response.json().get('detail', 'Unknown error')
                await message.answer(f"Ro'yxatdan o'tishda xatolik: {error_detail}")
                await state.clear()
    except Exception as e:
        logger.error(f"Error during registration for user {user_id}: {str(e)}")
        await message.answer(f"Xatolik yuz berdi: {str(e)}")
        await state.clear()

@router.message(UserState.code, F.text.regexp(r"^\d{6}$"))
async def handle_code(message: Message, state: FSMContext):
    user_id = message.from_user.id
    code = message.text
    logger.info(f"Received verification code from user {user_id}: {code}")

    try:
        async with httpx.AsyncClient() as client:
            logger.info(f"Sending POST request to /verify with code {code}")
            response = await client.post(
                "http://localhost:8000/verify",
                json={"verification_code": code}
            )
            logger.info(f"Received response from /verify: status={response.status_code}, body={response.json()}")

            if response.status_code == 200:
                await message.answer("Muvaffaqiyatli tasdiqlandi!")
                await state.clear()
            else:
                error_detail = response.json().get('detail', 'Invalid or expired code')
                await message.answer(f"Xatolik: {error_detail}")
    except Exception as e:
        logger.error(f"Error during verification for user {user_id}: {str(e)}")
        await message.answer(f"Xatolik yuz berdi: {str(e)}")

@router.message(UserState.code)
async def invalid_code(message: Message):
    logger.info(f"Invalid code received from user {message.from_user.id}: {message.text}")
    await message.answer("Iltimos, 6 raqamli kodni kiriting")