from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from crud.user import get_user_by_email
from core.security import decode_access_token
from db.db import get_db
from sqlalchemy.orm import Session

oauth = OAuth2PasswordBearer(tokenUrl="api/v1/auth/login")

def get_current_user(
        db: Session = Depends(get_db),
        token: str = Depends(oauth)
):
    payload =  decode_access_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials"
        )
    
    email: str =  payload.get("sub")
    user = get_user_by_email(db, email)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    if  not user.is_active:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User is inactive")
    
    return user