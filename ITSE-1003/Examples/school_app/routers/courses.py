# -------------------------------------------------
# Rutas HTTP: cursos
# -------------------------------------------------

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from database import get_db
from schemas import CourseCreate, CourseResponse, CourseUpdate
import services

router = APIRouter(prefix="/courses", tags=["Courses"])


@router.get("/", response_model=list[CourseResponse])
def list_courses(
    skip: int = 0,
    limit: int = Query(100, le=500),
    search: str | None = Query(None, description="Filtrar por nombre del curso"),
    instructor_id: int | None = Query(None, description="Solo cursos de este instructor"),
    db: Session = Depends(get_db),
):
    return services.get_courses(
        db, skip=skip, limit=limit, search=search, instructor_id=instructor_id
    )


@router.post("/", response_model=CourseResponse, status_code=status.HTTP_201_CREATED)
def create_course(data: CourseCreate, db: Session = Depends(get_db)):
    return services.create_course(db, data)


@router.get("/{course_id}", response_model=CourseResponse)
def retrieve_course(course_id: int, db: Session = Depends(get_db)):
    return services.get_course(db, course_id)


@router.put("/{course_id}", response_model=CourseResponse)
def update_course(course_id: int, data: CourseUpdate, db: Session = Depends(get_db)):
    return services.update_course(db, course_id, data)


@router.delete("/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    services.soft_delete_course(db, course_id)
    return {"message": "Course deleted successfully"}
