import asyncio
from datetime import date
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.security import hash_password
from db.db import SessionLocal, engine
from db.models.department import Department
from db.models.employee import Employee
from db.models.user import User
from db.models.role import Role

roles = [
        {"name": "admin", "description": "Full access"},
        {"name": "manager", "description": "Manage Content"},
        {"name": "viewer", "description": "Read-only"}
        ]

async def init_db(db: AsyncSession) -> None:
    
    for role_data in roles:
        result = await db.execute(
            select(Role).where(Role.name == role_data["name"])
        )
        existing_role = result.scalar_one_or_none()

        if not existing_role:
            new_role = Role(**role_data)
            db.add(new_role)
            print(f"Created new role: {role_data['name']}" )
        else:
            print(f"Role already exists: {role_data['name']}")
    await db.flush()

    result = await db.execute(
        select(Department).where(Department.code == "ADMIN")
    )
    dept = result.scalar_one_or_none()
    if not dept:
        dept = Department(name="Administration", code="ADMIN")
        db.add(dept)
        await db.flush()
        await db.refresh(dept)
        print("Created Department: Admin")
    else:
        print("Admin Department already exists")

    result = await db.execute(
        select(Employee).where(Employee.employee_id == 1)
    )
    employee = result.scalar_one_or_none()
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
        await db.flush()
        await db.refresh(employee)
        print("Create Employee: System Admin")
    else:
        print("System Admin employee already exists")

    result = await db.execute(
        select(User).where(User.email == "admin@erp.com")
    )
    user = result.scalar_one_or_none()
    if not user:
        result = await db.execute(
            select(Role).where(Role.name == "admin")
        )
        admin_role = result.scalar_one_or_none()
        user = User(
            username="admin",
            email="admin@erp.com",
            hashed_password=hash_password("password1"),
            is_staff=True,
            is_superuser=True,
            employee_id=employee.id,
        )
        user.roles.append(admin_role)
        db.add(user)
        print("Create User: admin")
    else:
        print("User already exists")

    await db.commit()
    print("Database Initialization completed")

async def main():
    async with SessionLocal() as db:
        await init_db(db)
    await engine.dispose()

if __name__ == "__main__":
    asyncio.run(main())

