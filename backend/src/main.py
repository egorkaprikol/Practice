from fastapi import FastAPI
from backend.src.visits import models
from backend.src.database.config import engine
from backend.src.patients.router import router as patients_router
from backend.src.doctors.router import router as doctors_router
from backend.src.visits.router import router as visits_router
from backend.src.auth.router import router as auth_router


app = FastAPI(
    title="PracticeApp"
)
models.Base.metadata.create_all(bind=engine)


app.include_router(patients_router)
app.include_router(doctors_router)
app.include_router(visits_router)
app.include_router(auth_router)
