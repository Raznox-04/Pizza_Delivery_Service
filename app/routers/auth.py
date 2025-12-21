from fastapi import APIRouter,Depends,HTTPException,status
from app.database.session import get_database
from app.database.session import Session
from app.schemas.users_schema import SignUpModel,SignUpResponseModel
from app.services.user_services import UserGetService,UserCreateService,PasswordHasherService
auth_router = APIRouter(prefix="/api",tags=["auth_users"])


@auth_router.post("/signup", response_model=SignUpResponseModel,status_code=status.HTTP_201_CREATED)
async def signup(user_create: SignUpModel,db:Session = Depends(get_database)):
    user_service = UserCreateService(db)
    try:
        user = user_service.create_user(user_create)
        return user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

