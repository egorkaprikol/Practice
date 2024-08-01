from fastapi import FastAPI
from backend.src.patients.router import router as patients_router
from backend.src.doctors.router import router as doctors_router
from backend.src.visits.router import router as visits_router
from backend.src.auth.router import router as auth_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="PracticeApp"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(patients_router)
app.include_router(doctors_router)
app.include_router(visits_router)
app.include_router(auth_router)
