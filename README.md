# 🤖 AI Recruitment Copilot

An AI-powered Recruitment Copilot built with **FastAPI** that automates resume parsing by extracting candidate information from PDF resumes and storing it in a structured JSON format.

---

## 🚀 Features

- 📄 Upload PDF Resume
- 📝 Extract Resume Text
- 👤 Extract Candidate Name
- 📧 Extract Email Address
- 📱 Extract Phone Number
- 💻 Extract Technical Skills
- 🎓 Extract Education Details
- 💼 Extract Experience
- 📂 Save Extracted Data as JSON
- 📖 Interactive API Documentation using Swagger

---

## 🛠️ Tech Stack

| Technology | Usage |
|------------|-------|
| Python | Backend |
| FastAPI | REST API |
| PyMuPDF | PDF Text Extraction |
| JSON | Data Storage |
| Git | Version Control |
| GitHub | Repository Hosting |

---

# 📂 Project Structure

```text
AI-Recruitment-Copilot
│
├── app
│   ├── main.py
│   │
│   ├── routes
│   │     └── upload.py
│   │
│   ├── services
│   │     ├── parser.py
│   │     └── extractor.py
│   │
│   ├── database.py
│   ├── models
│   ├── schemas
│   └── utils
│
├── uploads
│
├── extracted_data
│
├── requirements.txt
│
├── .gitignore
│
└── README.md
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/shubhamraj-65/AI-Recruitment-Copilot.git
```

Move into the project

```bash
cd AI-Recruitment-Copilot
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run FastAPI

```bash
uvicorn app.main:app --reload
```

---

# 📌 API Endpoints

## Home

```
GET /
```

Returns welcome message.

---

## Upload Resume

```
POST /upload/
```

Uploads a PDF resume and extracts candidate details.

---

# 📥 Sample Response

```json
{
  "name": "SHUBHAM RAJ",
  "email": "shubhamraj.1937@gmail.com",
  "phone": "+91-7070721937",
  "skills": [
    "Python",
    "SQL",
    "Power BI",
    "FastAPI"
  ],
  "education": [
    "Bachelor of Technology",
    "Computer Science"
  ],
  "experience": [
    "8 months"
  ]
}
```

---

# 📖 Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# 🎯 Milestone 1 Completed

✔ FastAPI Backend

✔ Resume Upload API

✔ PDF Text Extraction

✔ Candidate Information Extraction

✔ JSON Generation

✔ Swagger API

✔ GitHub Integration

---
