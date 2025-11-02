from sqlalchemy.orm import Mapped, mapped_column, relationship
from .employee import Employee
from engine import Base

class Department(Base):
    __tablename__ = "department"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(nullable=False, index=True)
    
    #employees inside department
    employees: Mapped[list["Employee"]] = relationship(
        "Employee", back_populates="department", cascade="save-update"
    )