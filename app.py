from flask import Flask, render_template, request
from PyPDF2 import PdfReader
import os
import re

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

SKILLS = [
    "python",
    "java",
    "c",
    "c++",
    "javascript",
    "typescript",
    "html",
    "css",
    "react",
    "angular",
    "node.js",
    "express",
    "mongodb",
    "mysql",
    "sql",
    "flask",
    "django",
    "fastapi",
    "git",
    "github",
    "docker",
    "aws",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "data science",
    "pandas",
    "numpy",
    "tensorflow",
    "opencv"
]

def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def find_skills(text):
    text = text.lower()

    found_skills = []

    for skill in SKILLS:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, text):
            found_skills.append(skill)

    return found_skills


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    if "resume" not in request.files:
        return "Resume file is required"

    resume = request.files["resume"]
    job_description = request.form.get("job_description", "")

    if resume.filename == "":
        return "Please select a resume"

    if not resume.filename.lower().endswith(".pdf"):
        return "Only PDF files are supported"

    file_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        resume.filename
    )

    resume.save(file_path)

    resume_text = extract_text_from_pdf(file_path)

    resume_skills = find_skills(resume_text)
    job_skills = find_skills(job_description)

    matched_skills = [
        skill for skill in job_skills
        if skill in resume_skills
    ]

    missing_skills = [
        skill for skill in job_skills
        if skill not in resume_skills
    ]

    if len(job_skills) > 0:
        match_percentage = (
            len(matched_skills) / len(job_skills)
        ) * 100
    else:
        match_percentage = 0

    skill_gap_summary = {
        "total_missing": len(missing_skills),
        "focus_areas": missing_skills[:5],
        "is_gap_found": len(missing_skills) > 0,
    }

    return render_template(
        "index.html",
        match_percentage=round(match_percentage, 2),
        resume_skills=resume_skills,
        job_skills=job_skills,
        matched_skills=matched_skills,
        missing_skills=missing_skills,
        skill_gap_summary=skill_gap_summary,
    )


if __name__ == "__main__":
    app.run(debug=True)