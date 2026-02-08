from fastapi import HTTPException, status
from jose import ExpiredSignatureError, JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone

pwd_context = CryptContext(schemes=["argon2"],
                            deprecated="auto")
SECRET_KEY = "that-which-shall-not-be-named"
ALGORITHM = "HS256"


def hash_password(password: str):
    return pwd_context.hash(str(password))


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=1)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, ALGORITHM)

def verify_password(login_password: str, hashed_password: str):
    return pwd_context.verify(login_password, hashed_password)

def decode_access_token(token: str) -> dict | None:
    try: 
        payload = jwt.decode(
            token=token,
            key=SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload
    except JWTError:
        return None
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired")