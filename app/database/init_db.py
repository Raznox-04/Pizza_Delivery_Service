from app.database.database import engine
from app.database.base import Base
from app.models.orders import Orders
from app.models.users import Users
Base.metadata.create_all(bind=engine)
