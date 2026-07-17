from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base

SQLAlCHEMY_DATABASE_URL = "mysql+pymysql://root:19576507Hh%40@localhost:3306/student_db"

engine = create_engine(SQLAlCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False ,autocommit=False, bind=engine)

Base = declarative_base()

def handle_connect_DB ():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()