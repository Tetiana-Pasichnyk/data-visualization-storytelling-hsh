#!/bin/bash
# Quick start script for Streamlit app

echo "🚀 Starting Arbeitsagentur Job Scraper (Streamlit)"
echo "=================================================="
echo ""
echo "Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "Starting Streamlit app..."
echo "The app will open in your browser at http://localhost:8501"
echo ""
streamlit run streamlit_app.py

# Made with Bob
