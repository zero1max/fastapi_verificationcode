from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import User
from utils.code_generator import generate_verification_code
from fastapi import HTTPException
from datetime import datetime

async def create_user(db: AsyncSession, telegram_id: int, phone_number: str):
    # Check for existing user
    result = await db.execute(select(User).filter(User.telegram_id == telegram_id))
    existing_user = result.scalars().first()
    if existing_user:
        if existing_user.is_verified:
            raise HTTPException(status_code=400, detail="User already verified")
        else:
            while True:
                code, expires_at = generate_verification_code()
                code_result = await db.execute(select(User).filter(User.verification_code == code))
                if not code_result.scalars().first():
                    break
            existing_user.phone_number = phone_number
            existing_user.verification_code = code
            existing_user.expires_at = expires_at
            await db.commit()
            await db.refresh(existing_user)
            return existing_user

    # Create new user with unique verification code
    while True:
        code, expires_at = generate_verification_code()
        code_result = await db.execute(select(User).filter(User.verification_code == code))
        if not code_result.scalars().first():
            break
    user = User(
        telegram_id=telegram_id,
        phone_number=phone_number,
        verification_code=code,
        expires_at=expires_at,
        is_verified=False
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

async def verify_user(db: AsyncSession, code: str):
    # Find user by verification code
    result = await db.execute(select(User).filter(User.verification_code == code))
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=404, detail="Invalid code")
    if user.is_verified:
        raise HTTPException(status_code=400, detail="User already verified")
    if user.expires_at < datetime.utcnow():
        raise HTTPException(status_code=400, detail="Expired code")
    
    user.is_verified = True
    user.verification_code = None
    user.expires_at = None
    await db.commit()
    return user