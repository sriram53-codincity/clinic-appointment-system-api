# app/routes/doctor_routes.py

from typing import Optional

from fastapi import APIRouter, status, HTTPException
from app.models import DoctorModel, SlotModel
from app.database import doctors_collection
from app.services import generate_id, doctor_exists

router = APIRouter()

# Create a new doctor
@router.post("/doctors", status_code=status.HTTP_201_CREATED)
def create_doctor(doctor: DoctorModel):

    doctor_data = doctor.dict()

    doctor_data["id"] = generate_id(doctors_collection)

    doctor_data["slots"] = []

    doctors_collection.insert_one(doctor_data)

    doctor_data.pop("_id", None)

    return {
        "success": True,
        "message": "Doctor created successfully",
        "data": doctor_data
    }

# Get doctor details by ID
@router.get("/doctors/{doctor_id}")
def get_doctor(doctor_id: int):

    doctor = doctor_exists(doctor_id)

    doctor.pop("_id", None)

    return {
        "success": True,
        "message": "Doctor fetched successfully",
        "data": doctor
    }

from typing import Optional

# finding doctors by specialization or return all doctors
@router.get("/doctors")
def filter_doctors(specialization: Optional[str] = None):

    query = {}
    if specialization:
        query["specialization"] = specialization

    doctors = list(
        doctors_collection.find(query)
    )

    for doctor in doctors:
        doctor.pop("_id", None)

    return {
        "success": True,
        "message": "Doctors fetched successfully",
        "data": doctors
    }

# Add available slot for a doctor
@router.post("/doctors/{doctor_id}/slots")
def add_slot(doctor_id: int, slot: SlotModel):

    doctor = doctor_exists(doctor_id)

    if slot.time_slot in doctor["slots"]:
        raise HTTPException(
            status_code=400,
            detail="Slot already exists"
        )

    doctors_collection.update_one(
        {"id": doctor_id},
        {
            "$push": {
                "slots": slot.time_slot
            }
        }
    )

    return {
        "success": True,
        "message": "Slot added successfully"
    }