from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import func, ForeignKey
from db.db import Base
from typing import Optional
from .employee import Employee

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False, index=True)
    email: Mapped[str] = mapped_column(unique=True, nullable=False, index=True)
    password_hash: Mapped[str] = mapped_column(nullable=False)

    #Auth
    is_active: Mapped[bool] = mapped_column(default=True)
    is_staff: Mapped[bool] = mapped_column(default=False) #Outside employee or company hired employee
    is_superuser: Mapped[bool] = mapped_column(default=False)
    last_login: Mapped[Optional[datetime]] = mapped_column()

    #Historic Data
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

    #Employee mapping
    employee_id: Mapped[Optional[int]] = mapped_column(ForeignKey("employee.id"), unique=True)
    employee: Mapped[Optional["Employee"]] = relationship("Employee", back_populates="user")