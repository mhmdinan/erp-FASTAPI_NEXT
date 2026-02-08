from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .employee import Employee

class Department(Base):
    __tablename__ = "department"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False, index=True)
    code: Mapped[str] = mapped_column(nullable=False)
    
    #employees inside department
    employees: Mapped[list["Employee"]] = relationship(
        "Employee", back_populates="department", cascade="save-update"
    )