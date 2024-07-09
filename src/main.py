from fastapi import FastAPI
from src.visits import models
from src.database.config import engine
from src.patients.router import router as patients_router
from src.doctors.router import router as doctors_router
from src.visits.router import router as visits_router
from src.auth.router import router as auth_router


app = FastAPI(
    title="PracticeApp"
)
models.Base.metadata.create_all(bind=engine)


app.include_router(patients_router)
app.include_router(doctors_router)
app.include_router(visits_router)
app.include_router(auth_router)
