from sqlalchemy import Column, Integer, BigInteger, String, Boolean, DateTime
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(BigInteger, unique=True, index=True, nullable=False)
    phone_number = Column(String, nullable=False)
    verification_code = Column(String, nullable=True)
    expires_at = Column(DateTime, nullable=True)
    is_verified = Column(Boolean, default=False)