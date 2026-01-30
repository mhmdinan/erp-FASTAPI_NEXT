from passlib.context import CryptContext

ctx = CryptContext(schemes=["argon2"])
p = "password1"
print(f"Hashed: {ctx.hash(p)}")