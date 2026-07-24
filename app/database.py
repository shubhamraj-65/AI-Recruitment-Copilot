import streamlit as st
import json
import os

st.set_page_config(
    page_title="AI Recruitment Copilot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Recruitment Copilot")
st.subheader("Candidate Dashboard")

folder = "extracted_data"

if not os.path.exists(folder):
    st.warning("No extracted data found.")
    st.stop()

files = [f for f in os.listdir(folder) if f.endswith(".json")]

if len(files) == 0:
    st.warning("No candidate data available.")
    st.stop()

selected = st.selectbox("Select Candidate", files)

with open(os.path.join(folder, selected), "r") as f:
    candidate = json.load(f)

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("👤 Personal Information")

    st.write("**Name:**", candidate.get("name"))
    st.write("**Email:**", candidate.get("email"))
    st.write("**Phone:**", candidate.get("phone"))

with col2:
    st.subheader("💼 Experience")

    experience = candidate.get("experience", [])

    for exp in experience:
        st.write("•", exp)

st.divider()

st.subheader("🎓 Education")

education = candidate.get("education", [])

for edu in education:
    st.write("•", edu)

st.divider()

st.subheader("💻 Skills")

skills = candidate.get("skills", [])

for skill in skills:
    st.success(skill)