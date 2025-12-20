from pydantic import EmailStr
from sqlalchemy.orm import Session
from app.models.users import Users
from app.schemas.users_schema import SignUpModel
from passlib.context import  CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class PasswordHasherService:
    def __init__(self, password_hasher: CryptContext):
        self.password_hasher = password_hasher

    def hash_password(self, password: str) -> str:
        return self.password_hasher.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.password_hasher.verify(plain_password, hashed_password)


class UserGetService:
    def __init__(self, db: Session):
        self.db = db
    def get_user_by_username(self, user_username: str) -> Users:
        user = self.db.query(Users).filter(Users.username == user_username).first()
        return user

    def get_user_by_email(self, user_email: EmailStr):
        user = self.db.query(Users).filter(Users.email == user_email).first()
        return user


class UserCreateService:
    def __init__(self, db: Session):
        self.db = db
        self.get_service = UserGetService(db)
        self.hasher = PasswordHasherService(pwd_context)

    def create_user(self, user_data : SignUpModel ) -> Users:#password should be hashed and not show plain
        if self.get_service.get_user_by_email(user_data.email):
            raise ValueError("Email already registered")
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
