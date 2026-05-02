# -------------------------------------------------
# Rutas HTTP: instructores
# -------------------------------------------------

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from database import get_db
from schemas import InstructorCreate, InstructorResponse, InstructorUpdate
import services

router = APIRouter(prefix="/instructors", tags=["Instructors"])


@router.get("/", response_model=list[InstructorResponse])
def list_instructors(
    skip: int = 0,
    limit: int = Query(100, le=500),
    search: str | None = Query(None, description="Filtrar por nombre (coincidencia parcial)"),
    db: Session = Depends(get_db),
):
    return services.get_instructors(db, skip=skip, limit=limit, search=search)


@router.post("/", response_model=InstructorResponse, status_code=status.HTTP_201_CREATED)
def create_instructor(data: InstructorCreate, db: Session = Depends(get_db)):
    return services.create_instructor(db, data)


@router.get("/{instructor_id}", response_model=InstructorResponse)
def retrieve_instructor(instructor_id: int, db: Session = Depends(get_db)):
    return services.get_instructor(db, instructor_id)


@router.put("/{instructor_id}", response_model=InstructorResponse)
def update_instructor(
    instructor_id: int, data: InstructorUpdate, db: Session = Depends(get_db)
):
    return services.update_instructor(db, instructor_id, data)


@router.delete("/{instructor_id}")
def delete_instructor(instructor_id: int, db: Session = Depends(get_db)):
    services.soft_delete_instructor(db, instructor_id)
    return {"message": "Instructor deleted successfully"}
