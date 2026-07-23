from fastapi import APIRouter, UploadFile, File
from app.services.parser import extract_text
import shutil
import json

from app.services.extractor import (
    extract_email,
    extract_phone,
    extract_name,
    extract_skills,
    extract_education,
    extract_experience
)

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)


@router.get("/")
def upload_home():
    return {
        "message": "Upload Route Working Successfully"
    }


@router.post("/")
def upload_resume(file: UploadFile = File(...)):

    # Save uploaded file
    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text
    resume_text = extract_text(file_path)

    # Extract information
    email = extract_email(resume_text)
    phone = extract_phone(resume_text)
    name = extract_name(resume_text)
    skills = extract_skills(resume_text)
    education = extract_education(resume_text)
    experience = extract_experience(resume_text)

    # Create candidate dictionary
    candidate = {
        "name": name,
        "email": email,
        "phone": phone,
        "skills": skills,
        "education": education,
        "experience": experience
    }

    # Safe filename
    safe_name = name if name else "Unknown_Candidate"

    json_file = f"extracted_data/{safe_name.replace(' ', '_')}.json"

    # Save JSON
    with open(json_file, "w") as json_output:
        json.dump(candidate, json_output, indent=4)

    # Return response
    return {
        "filename": file.filename,
        "message": "Resume uploaded successfully",
        "saved_at": file_path,
        "candidate": candidate,
        "json_saved_at": json_file,
        "text_preview": resume_text[:500]
    }