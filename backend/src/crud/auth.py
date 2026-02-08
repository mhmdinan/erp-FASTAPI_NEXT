from pydantic import EmailStr
from crud.user import get_user_by_email
from core.security import verify_password
from sqlalchemy.ext.asyncio import AsyncSession


async def authenticate_user(db: AsyncSession, email: EmailStr, password: str):
    user = await get_user_by_email(db, email)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user
