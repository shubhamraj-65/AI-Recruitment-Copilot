from fastapi import FastAPI
from app.routes.upload import router as upload_router
from fastapi.responses import HTMLResponse
import json
import os

app = FastAPI()
app.include_router(upload_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Recruitment Copilot"
    }

@app.get("/dashboard", response_class=HTMLResponse)
def dashboard():

    folder = "extracted_data"
    cards = ""

    if os.path.exists(folder):

        for filename in os.listdir(folder):

            if filename.endswith(".json"):

                with open(os.path.join(folder, filename), "r") as f:
                    candidate = json.load(f)

                skills = ", ".join(candidate.get("skills", []))
                education = ", ".join(candidate.get("education", []))
                experience = ", ".join(candidate.get("experience", []))

                cards += f"""
                <div style="
                    background:white;
                    border-radius:10px;
                    padding:20px;
                    margin:20px;
                    box-shadow:0px 2px 8px rgba(0,0,0,0.2);
                ">
                    <h2>{candidate.get("name","N/A")}</h2>

                    <p><b>Email:</b> {candidate.get("email","N/A")}</p>

                    <p><b>Phone:</b> {candidate.get("phone","N/A")}</p>

                    <p><b>Education:</b> {education}</p>

                    <p><b>Experience:</b> {experience}</p>

                    <p><b>Skills:</b> {skills}</p>

                </div>
                """

    return f"""
    <html>

    <head>

        <title>AI Recruitment Copilot</title>

    </head>

    <body style="
        font-family:Arial;
        background:#f5f5f5;
        padding:30px;
    ">

        <h1 style="text-align:center;">
            AI Recruitment Copilot Dashboard
        </h1>

        {cards}

    </body>

    </html>
    """