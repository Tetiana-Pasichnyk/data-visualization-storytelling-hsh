"""
Flask backend API for HTML/JS frontend
"""

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from scraper import JobScraper
from config import JOB_CATEGORIES, DATA_FILE, HISTORY_FILE
import json
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend

scraper = JobScraper()


@app.route('/api/scrape', methods=['POST'])
def scrape():
    """Trigger scraping"""
    try:
        data = request.get_json()
        categories = data.get('categories', JOB_CATEGORIES)
        
        results = scraper.scrape_all_categories(categories)
        df = scraper.save_results(results)
        
        return jsonify({
            'success': True,
            'count': len(results),
            'message': 'Scraping completed successfully'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/data', methods=['GET'])
def get_data():
    """Get all historical data"""
    try:
        df = scraper.load_history()
        
        if df.empty:
            return jsonify([])
        
        # Convert to list of dicts
        data = df.to_dict('records')
        return jsonify(data)
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500


@app.route('/api/categories', methods=['GET'])
def get_categories():
    """Get current job categories"""
    return jsonify(JOB_CATEGORIES)


@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get summary statistics"""
    try:
        df = scraper.load_history()
        
        if df.empty:
            return jsonify({
                'total_entries': 0,
                'unique_categories': 0,
                'unique_dates': 0,
                'latest_total': 0
            })
        
        # Get latest data
        latest_date = df['date'].max()
        latest_data = df[df['date'] == latest_date]
        
        stats = {
            'total_entries': len(df),
            'unique_categories': df['category'].nunique(),
            'unique_dates': df['date'].nunique(),
            'latest_total': int(latest_data['count'].sum()),
            'latest_date': latest_date
        }
        
        return jsonify(stats)
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500


@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'api_version': '1.0.0'
    })


if __name__ == '__main__':
    print("🚀 Starting Flask API server...")
    print("📡 API will be available at http://localhost:5000")
    print("📊 Endpoints:")
    print("   POST /api/scrape - Trigger scraping")
    print("   GET  /api/data - Get all data")
    print("   GET  /api/categories - Get job categories")
    print("   GET  /api/stats - Get statistics")
    print("   GET  /api/health - Health check")
    print("\nPress Ctrl+C to stop\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)

# Made with Bob
