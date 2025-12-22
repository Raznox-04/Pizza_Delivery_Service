from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.database.session import get_database
from app.core.security import token_service
from app.services.user_services import UserGetService
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/api/login")
async def get_current_user(token: str = Depends(oauth2_scheme),db: Session = Depends(get_database)):
    token_data = token_service.decode_access_token(token)
    if not token_data:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user_get_service = UserGetService(db)
    try:
        username = str(token_data.sub)
        user = user_get_service.get_user_by_username(username)
    except ValueError:
        user = user_get_service.get_user_by_email(token_data.sub)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User inactive",
        )
    return user

