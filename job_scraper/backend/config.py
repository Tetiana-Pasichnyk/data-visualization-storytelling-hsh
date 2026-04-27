"""
Configuration file for job scraper
Contains job categories and URL templates
"""

# Modular job categories array - can be easily modified
JOB_CATEGORIES = [
    "Business Intelligence",
    "Full-Stack",
    "Data Scientist",
    "Data Analyst",
    "System Administrator",
    "DevOps Engineer",
    "Backend Developer",
    "Frontend Developer",
    "Machine Learning Engineer",
    "Cloud Architect"
]

# Job types (Angebotsart)
JOB_TYPES = {
    "Arbeit": 1,  # Regular employment
    "Ausbildung": 34,  # Training/Apprenticeship
    "Selbstständigkeit": 4  # Self-employment
}

# Base URL for Arbeitsagentur job search
BASE_URL = "https://www.arbeitsagentur.de/jobsuche/suche"

# Additional search parameters for specific job types
ADDITIONAL_PARAMS = {
    "Praktikant Intern Business Intelligence": {
        "angebotsart": 34,
        "additional_search": "Praktikant Intern"
    },
    "Fachinformatiker Daten- und Prozessanalyse": {
        "angebotsart": 4,
        "berufsfeld": "Informatik",
        "beruf": "Fachinformatiker/in - Daten- und Prozessanalyse"
    }
}

# Data storage
DATA_FILE = "job_data.json"
HISTORY_FILE = "job_history.csv"

# Made with Bob
