from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    username: str
    hashed_password: str
    is_active: bool = True
    is_staff: bool = True
    is_superuser: bool = False
    employee_id: int
