from pydantic import EmailStr
from core.security import hash_password
from db.models.user import User
from sqlalchemy.orm import Session
from sqlalchemy import select
from schemas import user as user_schema


def get_user_by_email(db: Session, email: EmailStr) -> User | None:
    query = select(User).where(User.email == email)
    result = db.execute(query)
    return result.scalar_one_or_none()

def create_user(db: Session, user_input: user_schema.UserCreate) -> User:
    db_user = User(
        email = user_input.email,
        hashed_password = hash_password(user_input.password),
        is_active = True,
        is_superuser = user_input.is_superuser
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
