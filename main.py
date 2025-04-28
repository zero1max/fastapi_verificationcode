from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database import Base, engine, get_db
from schemas import UserRegister, UserVerify, UserResponse
from crud import create_user, verify_user
from tg_bot.bot import bot
import logging
from models import User

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("Database tables created")

async def send_verification_code(telegram_id: int, code: str):
    await bot.send_message(chat_id=telegram_id, text=f"Your verification code: {code}")

@app.get("/check_user")
async def check_user(telegram_id: int, db: AsyncSession = Depends(get_db)):
    from sqlalchemy.future import select
    result = await db.execute(select(User).filter(User.telegram_id == telegram_id))
    user = result.scalars().first()
    if user and user.is_verified:
        return {"is_verified": True}
    return {"is_verified": False}

@app.post("/register", response_model=UserResponse)
async def register_user(user: UserRegister, db: AsyncSession = Depends(get_db)):
    try:
        phone_number = user.phone_number
        if not phone_number:
            result = await db.execute(select(User).filter(User.telegram_id == user.telegram_id))
            existing_user = result.scalars().first()
            if existing_user:
                logger.info(f"User {user.telegram_id} found, using existing phone number: {existing_user.phone_number}")
                phone_number = existing_user.phone_number
            else:
                raise HTTPException(status_code=400, detail="User not found")

        db_user = await create_user(db, user.telegram_id, phone_number)
        await send_verification_code(user.telegram_id, db_user.verification_code)
        logger.info(f"User {user.telegram_id} processed, code sent")
        return {"message": "Verification code sent"}
    except Exception as e:
        logger.error(f"Error processing user {user.telegram_id}: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/verify", response_model=UserResponse)
async def verify_user_endpoint(user: UserVerify, db: AsyncSession = Depends(get_db)):
    try:
        await verify_user(db, user.verification_code)
        logger.info(f"User verified successfully with code {user.verification_code}")
        return {"message": "User successfully verified"}
    except Exception as e:
        logger.error(f"Error verifying user with code {user.verification_code}: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))