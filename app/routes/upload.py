from fastapi import APIRouter, UploadFile, File
from app.services.parser import extract_text
import shutil
from app.services.extractor import extract_email
from app.services.extractor import extract_email, extract_phone,extract_name,extract_skills,extract_education,extract_experience

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

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    resume_text = extract_text(file_path)
    email = extract_email(resume_text)
    phone = extract_phone(resume_text)
    name = extract_name(resume_text)
    skills = extract_skills(resume_text)
    education = extract_education(resume_text)
    experience = extract_experience(resume_text)

    return {
    "filename": file.filename,
    "message": "Resume uploaded successfully",
    "saved_at": file_path,
    "name":name,
    "email":email,
    "phone": phone,
    "skills":skills,
    "education": education,
    "experience":experience,
    "text_preview": resume_text[:500]
}