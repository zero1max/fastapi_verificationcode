import random
import string
from datetime import datetime, timedelta
from config import settings


def generate_verification_code() -> tuple[str, datetime]:
    code = ''.join(random.choices(string.digits, k=6))
    expires_at = datetime.utcnow() + timedelta(minutes=settings.CODE_TOKEN_EXPIRE_MINUTES)
    return code, expires_at