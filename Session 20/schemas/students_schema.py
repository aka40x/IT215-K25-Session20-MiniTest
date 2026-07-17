from pydantic import BaseModel, EmailStr, Field
from schemas.classrooms_schema import ClassroomResponse


class StudentRequest(BaseModel):
    student_code: str = Field(..., min_length=3, max_length=20)
    full_name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr = Field(...)
    class_id: int = Field(..., ge=1)


class StudentResponse(BaseModel):
    id: int
    student_code: str
    full_name: str
    email: str
    classroom: ClassroomResponse

    class Config:
        from_attributes = True