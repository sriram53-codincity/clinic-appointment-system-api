from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.patient_routes import router as patient_router
from app.routes.doctor_routes import router as doctor_router
from app.routes.appointment_routes import router as appointment_router
from app.routes.summary_routes import router as summary_router

app = FastAPI(
    title="Clinic Appointment System"
)

# Allow cross-origin requests from the frontend development server(s)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        # "http://127.0.0.1:5173",
        # "http://localhost:3000",
        # "http://127.0.0.1:3000",
        # "http://localhost:5174",
        # "http://127.0.0.1:5174",
        # "http://[::1]:5173",
        # "http://[::1]:5174",
        # "http://[::1]:5175",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(patient_router)
app.include_router(doctor_router)
app.include_router(appointment_router)
app.include_router(summary_router)


@app.get("/")
def home():

    return {
        "success": True,
        "message": "Clinic Appointment System API Running"
    }