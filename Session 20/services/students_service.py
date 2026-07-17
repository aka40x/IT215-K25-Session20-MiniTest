from sqlalchemy.orm import Session
from models import students_model
from schemas import students_schema


def handle_get_all_data_student(db: Session):
    return db.query(students_model.Student).all()


def handle_get_student_by_code(db: Session, student_code: str):
    return db.query(students_model.Student).filter(students_model.Student.student_code == student_code).first()


def handle_create_student(db: Session, payload: students_schema.StudentCreateRequest):
    new_student = students_model.Student(
        student_code=payload.student_code,
        full_name=payload.full_name,
        email=payload.email,
        class_id=payload.class_id,
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student
    