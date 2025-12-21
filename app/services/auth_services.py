from sqlalchemy.orm import Session
from app.models.users import Users
from app.services.user_services import UserGetService
from app.schemas.users_schema import SignUpModel
from app.core.security import PasswordHasherService,pwd_context
class UserCreateService:
    def __init__(self, db: Session):
        self.db = db
        self.get_service = UserGetService(db)
        self.hasher = PasswordHasherService(pwd_context)

    def create_user(self, user_data : SignUpModel ) -> Users:#password should be hashed and not show plain
        if self.get_service.get_user_by_email(user_data.email):
            raise ValueError("This Email already Registered")
        elif self.get_service.get_user_by_username(user_data.username):
            raise ValueError("This Username already Registered")
        hashed_password = self.hasher.hash_password(user_data.password)
        db_user = Users(
            username=user_data.username,
            email=user_data.email,
            password=hashed_password,
            is_active=user_data.is_active,
            is_staff=user_data.is_staff,
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
