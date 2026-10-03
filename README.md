# AI Resume Analyzer

A Flask web application that compares skills found in a PDF resume with skills mentioned in a job description. It reports a match score, matched skills, and missing skills to help identify areas to focus on.

## Features

- Upload a resume as a PDF.
- Paste a job description into the analyzer.
- Extract text from the PDF and look for recognized skills.
- View the resume skills, matched skills, missing skills, and match percentage.
- See up to five missing skills highlighted as focus areas.

The match percentage is calculated as the number of matched recognized job-description skills divided by the number of recognized job-description skills. Skill detection uses a built-in list and literal text matching; it does not infer equivalent terms or assess experience level. Scanned PDFs without selectable text may not produce usable results.

## Requirements

- Python 3
- pip

Python dependencies are listed in `requirements.txt` (Flask and PyPDF2).

## Run locally

From the project directory, create and activate a virtual environment, install the dependencies, and start Flask:

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

### macOS or Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser. The application creates an `uploads/` directory for submitted resumes; uploaded files are local and should be handled as sensitive data.

## Project structure

```text
app.py                 Flask routes and resume/skill analysis
requirements.txt       Python dependencies
templates/index.html   Analyzer form and results
static/style.css       Application styles
uploads/               Uploaded resumes (created at runtime; not committed)
```

## Privacy and deployment

Resumes are saved in the local `uploads/` directory. The included `.gitignore` excludes uploads, the virtual environment, Python cache files, and environment files from Git. The built-in Flask server runs in debug mode and is intended for local development only; use a production WSGI server and appropriate security controls before deploying publicly.
