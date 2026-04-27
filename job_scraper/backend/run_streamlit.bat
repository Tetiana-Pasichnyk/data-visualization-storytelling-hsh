@echo off
REM Quick start script for Streamlit app (Windows)

echo 🚀 Starting Arbeitsagentur Job Scraper (Streamlit)
echo ==================================================
echo.
echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Starting Streamlit app...
echo The app will open in your browser at http://localhost:8501
echo.
streamlit run streamlit_app.py

@REM Made with Bob
