from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date

class PatientModel(BaseModel):
    name: str = Field(..., min_length=2)
    age: int = Field(..., gt=0)
    phone_number: str = Field(..., min_length=10)
    city: str
    medical_notes: List[str]

class DoctorModel(BaseModel):
    name: str
    specialization: str
    experience: int = Field(..., ge=0)
    available_days: List[str]
    active_status: bool

class SlotModel(BaseModel):
    time_slot: str

class AppointmentModel(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_date: date
    time_slot: str
    reason_for_visit: str

class AppointmentStatusModel(BaseModel):
    status: str

class ConsultationModel(BaseModel):
    consultation_notes: List[str]