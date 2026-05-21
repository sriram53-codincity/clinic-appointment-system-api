# app/routes/patient_routes.py

from fastapi import APIRouter, status
from app.models import PatientModel
from app.database import patients_collection
from app.services import generate_id, patient_exists

router = APIRouter()


@router.post("/patients", status_code=status.HTTP_201_CREATED)
def create_patient(patient: PatientModel):

    patient_data = patient.dict()

    patient_data["id"] = generate_id(patients_collection)

    patients_collection.insert_one(patient_data)

    patient_data.pop("_id", None)

    return {
        "success": True,
        "message": "Patient created successfully",
        "data": patient_data
    }


@router.get("/patients/{patient_id}")
def get_patient(patient_id: int):

    patient = patient_exists(patient_id)

    patient.pop("_id", None)

    return {
        "success": True,
        "message": "Patient fetched successfully",
        "data": patient
    }

@router.get("/patients")
def get_all_patients():

    patients = list(
        patients_collection.find()
    )

    for patient in patients:
        patient.pop("_id", None)

    return {
        "success": True,
        "message": "Patients fetched successfully",
        "data": patients
    }