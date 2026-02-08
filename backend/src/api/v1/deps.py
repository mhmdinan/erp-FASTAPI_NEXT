from typing import Sequence
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from crud.user import get_user_by_email
from core.security import decode_access_token
from db.db import get_db
from sqlalchemy.orm import Session
from db.models.user import User

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

def require_roles(required_roles: str | Sequence[str]):

    if isinstance(required_roles, str):
        required_roles = [required_roles]

    required_set = set(r.lower() for r in required_roles)

    async def role_checker(current_user: User = Depends(get_current_user)) -> User:
        user_roles = {role.name.lower() for role in current_user.roles}

        if not required_set.intersection(user_roles):
            raise HTTPException()
        
        return current_user
    
    return role_checker

# aliases for role requirements
require_admin = require_roles("admin")
require_manager_or_higher = require_roles(["manager", "admin"])
require_viewer_or_higher = require_roles(["viewer", "manager", "admin"])