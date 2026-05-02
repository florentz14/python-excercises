# -------------------------------------------------
# Rutas HTTP: inscripciones
# -------------------------------------------------

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from database import get_db
from schemas import EnrollmentCreate, EnrollmentResponse, EnrollmentUpdate
import services

router = APIRouter(prefix="/enrollments", tags=["Enrollments"])


@router.get("/", response_model=list[EnrollmentResponse])
def list_enrollments(
    skip: int = 0,
    limit: int = Query(100, le=500),
    student_id: int | None = Query(None),
    course_id: int | None = Query(None),
    db: Session = Depends(get_db),
):
    return services.get_enrollments(
        db, skip=skip, limit=limit, student_id=student_id, course_id=course_id
    )


@router.post("/", response_model=EnrollmentResponse, status_code=status.HTTP_201_CREATED)
def create_enrollment(data: EnrollmentCreate, db: Session = Depends(get_db)):
    return services.create_enrollment(db, data)


@router.get("/{enrollment_id}", response_model=EnrollmentResponse)
def retrieve_enrollment(enrollment_id: int, db: Session = Depends(get_db)):
    return services.get_enrollment(db, enrollment_id)


@router.put("/{enrollment_id}", response_model=EnrollmentResponse)
def update_enrollment(
    enrollment_id: int, data: EnrollmentUpdate, db: Session = Depends(get_db)
):
    return services.update_enrollment(db, enrollment_id, data)


@router.delete("/{enrollment_id}")
def delete_enrollment(enrollment_id: int, db: Session = Depends(get_db)):
    services.soft_delete_enrollment(db, enrollment_id)
    return {"message": "Enrollment deleted successfully"}
