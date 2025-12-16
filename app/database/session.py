from sqlalchemy.orm import sessionmaker
from database import engine
session = sessionmaker(bind=engine,engine=engine,autocommit=True,autoflush=False,expire_on_commit=False)