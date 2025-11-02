from datetime import date
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .department import Department
from engine import Base
from .user import User

class Employee(Base):
    __tablename__ = "employee"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    employee_id: Mapped[int] = mapped_column(unique=True, nullable=False, index=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[Optional[str]] = mapped_column(unique=True, index=True)
    hire_date: Mapped[date] = mapped_column(nullable=False)
    termination_date: Mapped[Optional[date]] = mapped_column()

    #Job data
    job_title: Mapped[str] = mapped_column(nullable=False)
    department_id: Mapped[int] = mapped_column(ForeignKey("department.id"))
    department: Mapped["Department"] = relationship(
        "Department", back_populates="employees"
    )

    #User if ERP access allowed
    user: Mapped[Optional[User]] = relationship(
        "User", back_populates="employee", uselist=False
    )
