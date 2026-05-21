# Clinic Appointment System

## Project Overview

The Clinic Appointment System is a backend API project developed using FastAPI and MongoDB Compass.

This system helps manage:

* Patients
* Doctors
* Doctor Slot Availability
* Appointments
* Consultation Notes
* Patient Visit Summary

The project follows a clean folder structure and includes proper validation, error handling, MongoDB integration, and REST API principles.

---

# Features

* Create patients
* Create doctors
* Add doctor available slots
* Book appointments
* Prevent double booking
* Check doctor availability
* Check patient and doctor existence
* Update appointment status
* Add consultation notes
* Filter doctors by specialization
* Generate patient visit summary
* Proper validation using Pydantic
* Proper HTTP status codes
* Clean JSON responses
* MongoDB Compass integration

---

# Technologies Used

* Python
* FastAPI
* Uvicorn
* MongoDB
* PyMongo
* Pydantic
* Python Dotenv

---

# Project Structure

```text id="cwfj6n"
clinic_appointment_system/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── services.py
│   │
│   └── routes/
│       ├── patient_routes.py
│       ├── doctor_routes.py
│       ├── appointment_routes.py
│       └── summary_routes.py
│
├── .env
├── .gitignore
├── requirements.txt
└── run.py
```

---

# Prerequisites

Before running the project, make sure the following are installed:

* Python
* MongoDB Compass
* Git

---

# Environment Variables

Create a `.env` file in the project root folder.

Add the following values:

```text id="h6alml"
MONGO_URL=mongodb://localhost:(your port number)
DATABASE_NAME=clinic_db
```

---

# Install Required Packages

```bash id="4f9qku"
pip install -r requirements.txt
```

---

# Run the Project

```bash id="e12u33"
python run.py
```

Server will run at:

```text id="j1qk3m"
http://127.0.0.1:8000
```

---

# Swagger API Documentation

FastAPI automatically generates Swagger UI.

Open:

```text id="v4lljp"
http://127.0.0.1:8000/docs
```

---

# API Endpoints

| Method | Endpoint                                      | Description               |
| ------ | --------------------------------------------- | ------------------------- |
| POST   | `/patients`                                   | Create patient            |
| GET    | `/patients/{patient_id}`                      | Get patient by ID         |
| POST   | `/doctors`                                    | Create doctor             |
| GET    | `/doctors/{doctor_id}`                        | Get doctor by ID          |
| GET    | `/doctors?specialization=Cardiology`          | Filter doctors            |
| POST   | `/doctors/{doctor_id}/slots`                  | Add doctor slot           |
| POST   | `/appointments`                               | Book appointment          |
| PUT    | `/appointments/{appointment_id}/status`       | Update appointment status |
| PUT    | `/appointments/{appointment_id}/consultation` | Add consultation notes    |
| GET    | `/patients/{patient_id}/summary`              | Get patient visit summary |

---

# Sample API Flow

## Step 1

Create Patient

---

## Step 2

Create Doctor

---

## Step 3

Add Doctor Slot

---

## Step 4

Book Appointment

---

## Step 5

Update Appointment Status

---

## Step 6

Add Consultation Notes

---

## Step 7

Get Patient Summary

---

# Validation Included

The project includes:

* Required field validation
* Age validation
* Experience validation
* Duplicate slot prevention
* Double booking prevention
* Doctor active status checking
* Appointment existence checking
* Patient existence checking
* Doctor existence checking

---

# Error Handling

The project uses FastAPI HTTPException for:

* Patient not found
* Doctor not found
* Appointment not found
* Invalid appointment status
* Doctor inactive
* Slot already booked
* Slot already exists

---

# HTTP Status Codes Used

| Status Code | Meaning               |
| ----------- | --------------------- |
| 200         | Success               |
| 201         | Created Successfully  |
| 400         | Bad Request           |
| 404         | Resource Not Found    |
| 500         | Internal Server Error |

---

# Important Notes

* MongoDB automatically generates `_id`
* `_id` is removed before returning response
* Sensitive values are stored in `.env`
* `.env` is ignored using `.gitignore`
* APIs are tested using Swagger UI

---

# API Testing

You can test APIs using:

* Swagger UI
* Postman

---

# GitHub Instructions

* Maintain proper commit history
* Do not upload `.env`
* Do not upload virtual environment folder
* Push complete project to GitHub repository

---

# Future Improvements

Possible future enhancements:

* JWT Authentication
* Role Based Access
* Email Notifications
* Pagination
* Search APIs
* Appointment Rescheduling
* Admin Dashboard
* Docker Support

---
