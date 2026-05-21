# app/routes/summary_routes.py

from fastapi import APIRouter

from app.database import (
    appointments_collection
)

from app.services import patient_exists

router = APIRouter()


@router.get("/patients/{patient_id}/summary")
def patient_summary(patient_id: int):

    patient = patient_exists(patient_id)

    patient.pop("_id", None)

    appointments = list(
        appointments_collection.find(
            {"patient_id": patient_id}
        )
    )

    for appointment in appointments:
        appointment.pop("_id", None)

    return {
        "success": True,
        "message": "Patient summary fetched successfully",
        "data": {
            "patient": patient,
            "appointments": appointments
        }
    }