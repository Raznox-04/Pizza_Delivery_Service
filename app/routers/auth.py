from datetime import datetime
from fastapi import APIRouter,Depends,HTTPException,status
from app.models.users import Users
from app.schemas.users_schema import UserBase
from app.database.session import get_database
from fastapi.security import OAuth2PasswordRequestForm
from app.database.session import Session
from app.schemas.users_schema import SignUpModel,SignUpResponseModel,LoginModel
from app.services.auth_services import UserCreateService
from app.services.user_services import UserGetService
from app.core.security import PasswordHasherService, TokenService,pwd_context
from app.schemas.token_schema import TokenPayload
from app.routers.dependencies import get_current_user
from app.services.email_verification_services import EmailVerificationService
from app.schemas.verify_schema import VerifyEmailRequest

email_verify_service = EmailVerificationService(ttl_minutes=10)

auth_router = APIRouter(prefix="/api",tags=["auth_users"])

@auth_router.post("/signup", response_model=SignUpResponseModel,status_code=status.HTTP_201_CREATED)
async def signup(user_create: SignUpModel,db:Session = Depends(get_database)):
    user_service = UserCreateService(db)
    try:
        user = user_service.create_user(user_create)
        return user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@auth_router.post("/verify-email", status_code=status.HTTP_200_OK)
def verify_email(data: VerifyEmailRequest, db: Session = Depends(get_database)):
    user = db.query(Users).filter(Users.email == data.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user.is_active:
        return {"message": "Account already verified"}

    email_verify_service.verify_and_activate(db, user, data.code)
    return {"message": "Email verified successfully"}

@auth_router.post("/login",response_model=LoginModel,status_code=status.HTTP_200_OK)
async def login(data_form : OAuth2PasswordRequestForm = Depends(),db:Session = Depends(get_database)):
    user_service = UserGetService(db)
    token_service = TokenService()
    password_service = PasswordHasherService(pwd_context)
    user = user_service.get_user_by_username(data_form.username)
    if not user or not password_service.verify_password(data_form.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )
    token_payload = TokenPayload(sub=user.username,email=user.email)
    access_token = token_service.create_access_token(token_payload)
    return LoginModel(
        access_token=access_token,
        token_type="bearer",
        username=user.username,
        email=user.email,
    )

@auth_router.get("/me",response_model=UserBase,status_code=status.HTTP_200_OK)
async def get_current_user_details(current_user: Users = Depends(get_current_user)):
    current_user = {
        "user_id": current_user.id,
        "username": current_user.username,
        "email": current_user.email,
        "is_active": current_user.is_active,
    }
    return current_user