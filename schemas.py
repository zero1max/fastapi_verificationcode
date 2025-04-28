from pydantic import BaseModel, Field
from typing import Optional

class UserRegister(BaseModel):
    telegram_id: int
    phone_number: Optional[str] = Field(None, pattern=r"^\+\d{10,15}$")

class UserVerify(BaseModel):
    verification_code: str = Field(..., pattern=r"^\d{6}$")

class UserResponse(BaseModel):
    message: str