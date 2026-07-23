import re 
def extract_email(text):

    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return None

def extract_phone(text):

    pattern = r"(\+91[- ]?)?[6-9]\d{9}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return None

def extract_name(text):

    lines = text.split("\n")

    for line in lines:
        line = line.strip()

        if len(line) > 2 and line.isupper():
            return line

    return None

def extract_skills(text):

    skills_db = [
        "Python",
        "SQL",
        "Power BI",
        "Excel",
        "Pandas",
        "NumPy",
        "FastAPI",
        "Streamlit",
        "Machine Learning",
        "Generative AI",
        "OpenAI",
        "Git",
        "GitHub",
        "Tableau",
        "Statistics",
        "Data Analysis",
        "Data Visualization"
    ]

    found_skills = []

    text = text.lower()

    for skill in skills_db:
        if skill.lower() in text:
            found_skills.append(skill)

    return found_skills

def extract_education(text):

    education_keywords = [
        "B.Tech",
        "Bachelor of Technology",
        "B.E",
        "M.Tech",
        "MBA",
        "BCA",
        "MCA",
        "B.Sc",
        "M.Sc",
        "Diploma",
        "Computer Science",
        "Artificial Intelligence",
        "Data Science"
    ]

    found = []

    text = text.lower()

    for edu in education_keywords:
        if edu.lower() in text:
            found.append(edu)

    return found

def extract_experience(text):

    import re

    patterns = [
        r"\d+\+?\s*years?",
        r"\d+\+?\s*months?",
        r"\d+\+?\s*yrs?",
        r"\d+\+?\s*mos?"
    ]

    experiences = []

    for pattern in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)

        for match in matches:
            if match not in experiences:
                experiences.append(match)

    return experiences
