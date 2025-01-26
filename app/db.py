from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# load from .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://test:test@localhost/test")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base: DeclarativeMeta = declarative_base()


def init_db():
    import app.models  # models import
    Base.metadata.create_all(bind=engine)


# Dependency to connect to DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
