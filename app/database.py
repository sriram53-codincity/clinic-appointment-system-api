from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME")

client = MongoClient(MONGO_URL)

db = client[DATABASE_NAME]

print(f"Connected to MongoDB at {MONGO_URL}, using database '{DATABASE_NAME}'")

patients_collection = db["patients"]
doctors_collection = db["doctors"]
appointments_collection = db["appointments"]