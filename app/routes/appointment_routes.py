# app/routes/appointment_routes.py

from fastapi import APIRouter, status, HTTPException

from app.models import (
    AppointmentModel,
    AppointmentStatusModel,
    ConsultationModel
)

from app.database import (
    doctors_collection,
    appointments_collection
)

from app.services import (
    generate_id,
    patient_exists,
    doctor_exists
)

router = APIRouter()

VALID_STATUS = [
    "booked",
    "completed",
    "cancelled",
    "missed"
]


@router.post("/appointments", status_code=status.HTTP_201_CREATED)
def book_appointment(appointment: AppointmentModel):

    patient_exists(appointment.patient_id)

    doctor = doctor_exists(appointment.doctor_id)

    if doctor["active_status"] is False:
        raise HTTPException(
            status_code=400,
            detail="Doctor is inactive"
        )

    if appointment.time_slot not in doctor["slots"]:
        raise HTTPException(
            status_code=400,
            detail="Selected slot not available"
        )

    existing_appointment = appointments_collection.find_one({
        "doctor_id": appointment.doctor_id,
        "appointment_date": str(appointment.appointment_date),
        "time_slot": appointment.time_slot
    })

    if existing_appointment:
        raise HTTPException(
            status_code=400,
            detail="Slot already booked"
        )

    appointment_data = appointment.dict()

    appointment_data["id"] = generate_id(
        appointments_collection
    )

    appointment_data["status"] = "booked"

    appointment_data["consultation_notes"] = []

    appointment_data["appointment_date"] = str(
        appointment_data["appointment_date"]
    )

    appointments_collection.insert_one(
        appointment_data
    )

    appointment_data.pop("_id", None)

    return {
        "success": True,
        "message": "Appointment booked successfully",
        "data": appointment_data
    }


@router.put("/appointments/{appointment_id}/status")
def update_status(
    appointment_id: int,
    appointment_status: AppointmentStatusModel
):

    appointment = appointments_collection.find_one(
        {"id": appointment_id}
    )

    if not appointment:
        raise HTTPException(
            status_code=404,
            detail="Appointment not found"
        )

    if appointment_status.status not in VALID_STATUS:
        raise HTTPException(
            status_code=400,
            detail="Invalid status"
        )

    appointments_collection.update_one(
        {"id": appointment_id},
        {
            "$set": {
                "status": appointment_status.status
            }
        }
    )

    return {
        "success": True,
        "message": "Appointment status updated successfully"
    }


@router.put("/appointments/{appointment_id}/consultation")
def add_consultation_notes(
    appointment_id: int,
    consultation: ConsultationModel
):

    appointment = appointments_collection.find_one(
        {"id": appointment_id}
    )

    if not appointment:
        raise HTTPException(
            status_code=404,
            detail="Appointment not found"
        )

    if appointment["status"] != "completed":
        raise HTTPException(
            status_code=400,
            detail="Consultation notes can only be added after completion"
        )

    appointments_collection.update_one(
        {"id": appointment_id},
        {
            "$set": {
                "consultation_notes": consultation.consultation_notes
            }
        }
    )

    return {
        "success": True,
        "message": "Consultation notes added successfully"
    }


@router.get("/appointments")
def get_all_appointments():

    appointments = list(
        appointments_collection.find()
    )

    for appointment in appointments:
        appointment.pop("_id", None)

    return {
        "success": True,
        "data": appointments
    }
