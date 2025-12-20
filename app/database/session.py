from sqlalchemy.orm import sessionmaker
from database import engine
Session = sessionmaker(bind=engine,
                       autocommit=True,
                       autoflush=False,
                       expire_on_commit=False)