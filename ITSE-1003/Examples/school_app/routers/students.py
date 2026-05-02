# -------------------------------------------------
# Rutas HTTP: estudiantes
# -------------------------------------------------

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from database import get_db
from schemas import StudentCreate, StudentResponse, StudentUpdate
import services

router = APIRouter(prefix="/students", tags=["Students"])


@router.get("/", response_model=list[StudentResponse])
def list_students(
    skip: int = 0,
    limit: int = Query(100, le=500),
    search: str | None = Query(None, description="Filtrar por nombre (coincidencia parcial)"),
    db: Session = Depends(get_db),
):
    return services.get_students(db, skip=skip, limit=limit, search=search)


@router.post("/", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
def create_student(data: StudentCreate, db: Session = Depends(get_db)):
    return services.create_student(db, data)


@router.get("/{student_id}", response_model=StudentResponse)
def retrieve_student(student_id: int, db: Session = Depends(get_db)):
    return services.get_student(db, student_id)


@router.put("/{student_id}", response_model=StudentResponse)
def update_student(
    student_id: int, data: StudentUpdate, db: Session = Depends(get_db)
):
    return services.update_student(db, student_id, data)


@router.delete("/{student_id}")
def delete_student(student_id: int, db: Session = Depends(get_db)):
    services.soft_delete_student(db, student_id)
    return {"message": "Student deleted successfully"}
