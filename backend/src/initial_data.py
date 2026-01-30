from datetime import date
from sqlalchemy import select
from sqlalchemy.orm import Session
from core.security import hash_password
from db.db import SessionLocal
from db.models.department import Department
from db.models.employee import Employee
from db.models.user import User
from schemas.user import UserCreate


def init_db(db: Session) -> None:
    dept = db.execute(
        select(Department).where(Department.code == "ADMIN")
    ).scalar_one_or_none()
    if not dept:
        dept = Department(name="Administration", code="ADMIN")
        db.add(dept)
        db.flush()
        db.refresh(dept)
        print("Created Department: Admin")
    else:
        print("Admin Department already exists")

    employee = db.execute(
        select(Employee).where(Employee.employee_id == 1)
    ).scalar_one_or_none()
    if not employee:
        employee = Employee(
            employee_id=1,
            first_name="System",
            last_name="Admin",
            job_title="Superuser",
            department_id=dept.id,
            hire_date=date.today(),
            email="admin@erp.com",
        )
        db.add(employee)
        db.flush()
        db.refresh(employee)
        print("Create Employee: System Admin")
    else:
        print("System Admin employee already exists")

    user = db.execute(
        select(User).where(User.email == "admin@erp.com")
    ).scalar_one_or_none()
    if not user:
        user = User(
            username="admin",
            email="admin@erp.com",
            hashed_password=hash_password("password1"),
            is_staff=True,
            is_superuser=True,
            employee_id=employee.id,
        )
        db.add(user)
        print("Create User: admin")
    else:
        print("User already exists")

    db.commit()
    print("Database Initialization completed")


if __name__ == "__main__":
    with SessionLocal() as db:
        init_db(db)
