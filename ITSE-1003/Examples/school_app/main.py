# -------------------------------------------------
# File Name: main.py
# Author: Florentino
# Date: 5/2/26
# Description: FastAPI school app — lifespan, CORS, routers (patrón music_api)
# -------------------------------------------------

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine
import models  # noqa: F401 — registra tablas en Base.metadata antes de create_all

from routers import (
    courses_router,
    enrollments_router,
    instructors_router,
    students_router,
)
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="School Management API",
    description=(
        "FastAPI + SQLAlchemy + MySQL: estudiantes, instructores, cursos e inscripciones "
        "(alineado con school_db.sql). Lógica en `services/`, rutas en `routers/`."
    ),
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(students_router)
app.include_router(instructors_router)
app.include_router(courses_router)
app.include_router(enrollments_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to School Management API",
        "docs": "/docs",
        "endpoints": {
            "students": "/students",
            "instructors": "/instructors",
            "courses": "/courses",
            "enrollments": "/enrollments",
        },
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
