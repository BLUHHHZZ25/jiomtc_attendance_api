from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from contextlib import contextmanager

from config_setting import setting
from config.log import logger as fastapi_logger


engine = create_engine(setting.DATABASE_URL, pool_size=10, max_overflow=20)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        fastapi_logger.info("get_db closed")
        db.close()

@contextmanager
def db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        fastapi_logger.info("db_session closed")
        db.close()