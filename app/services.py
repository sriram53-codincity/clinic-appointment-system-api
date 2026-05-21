from app.database import (
    patients_collection,
    doctors_collection,
    appointments_collection
)

from fastapi import HTTPException

def generate_id(collection):
    last_record = collection.find_one(sort=[("id", -1)])

    if last_record:
        return last_record["id"] + 1

    return 1


def patient_exists(patient_id):
    patient = patients_collection.find_one({"id": patient_id})

    if not patient:
        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return patient


def doctor_exists(doctor_id):
    doctor = doctors_collection.find_one({"id": doctor_id})

    if not doctor:
        raise HTTPException(
            status_code=404,
            detail="Doctor not found"
        )

    return doctor