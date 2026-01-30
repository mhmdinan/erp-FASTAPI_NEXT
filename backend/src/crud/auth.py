from pydantic import EmailStr
from crud.user import get_user_by_email
from core.security import verify_password
from sqlalchemy.orm import Session


def authenticate_user(db: Session, email: EmailStr, password: str):
    user = get_user_by_email(db, email)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user
