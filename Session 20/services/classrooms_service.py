from sqlalchemy.orm import Session
from models import classrooms_model


def handle_get_classroom_by_id(db: Session, class_id: int):
    return db.query(classrooms_model.Classroom).filter(classrooms_model.Classroom.id == class_id).first()