from fastapi import FastAPI, APIRouter, Depends, HTTPException, Request, status
from database import handle_connect_DB, engine, Base
from sqlalchemy.orm import Session
from schemas.students_schema import StudentRequest, StudentResponse
from schemas.classrooms_schema import ClassroomResponse
from responses import success_response, error_response
from services import classrooms_service, students_service

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

@router.get("/", response_model=list[StudentResponse], status_code=status.HTTP_200_OK)
def get_all_data_student(db: Session = Depends(handle_connect_DB)):
    students = students_service.handle_get_all_data_student(db = db)
    return students

@router.post("/", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
def create_student(request: Request, payload: StudentRequest, db: Session = Depends(handle_connect_DB)):
    classroom_db = classrooms_service.handle_get_classroom_by_id(db=db, class_id=payload.class_id)
    if not classroom_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"message": "Không tìm thấy lớp học!", "error": "ERR-CLASS-01"}
        )

    existing_student = students_service.handle_get_student_by_code(db=db, student_code=payload.student_code)
    if existing_student:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"message": "Mã sinh viên đã tồn tại!", "error": "ERR-STUDENT-01"}
        )

    new_student_db = students_service.handle_create_student(db=db, payload=payload)
    data = StudentResponse.model_validate(new_student_db).model_dump()
    return success_response(status.HTTP_201_CREATED, "Thêm mới sinh viên thành công!", data, request.url.path)
