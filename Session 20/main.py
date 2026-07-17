from fastapi import FastAPI, Depends, Request
from sqlalchemy.orm import Session
from database import handle_connect_DB, engine, Base
from routers import students_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Quản Lý Sinh Viên Theo Lớp Học")

app.include_router(students_router.router)

app.get("/")
def home():
    return{"message": "Lấy dữ liệu thành công"}

