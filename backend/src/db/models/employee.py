from datetime import date
from typing import Optional, TYPE_CHECKING
from sqlalchemy import ForeignKey, func
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

if TYPE_CHECKING:
    from db.models.department import Department
    from db.models.user import User


class Employee(Base):
    __tablename__ = "employee"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    employee_id: Mapped[int] = mapped_column(unique=True, nullable=False, index=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[Optional[str]] = mapped_column(unique=True, index=True)
    hire_date: Mapped[date] = mapped_column(nullable=False, server_default=func.now())
    termination_date: Mapped[Optional[date]] = mapped_column()

    #Job data
    job_title: Mapped[str] = mapped_column(nullable=False)
    department_id: Mapped[int] = mapped_column(ForeignKey("department.id"))
    department: Mapped["Department"] = relationship(
        "Department", back_populates="employees"
    )

    #User if ERP access allowed
    user: Mapped[Optional["User"]] = relationship(
        "User", back_populates="employee", uselist=False
    )
