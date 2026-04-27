"""
Standalone Flask backend for webapp
Includes all necessary functionality + advanced features
"""

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import requests
import json
import pandas as pd
from datetime import datetime
import time
import os
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
import math
import re

app = Flask(__name__)
CORS(app)

# Configuration
API_KEY = "jobboerse-jobsuche"
BASE_URL = "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service"
DATA_FILE = "job_data.json"
HISTORY_FILE = "job_history.csv"
DETAILED_DATA_FILE = "job_details.json"
COMPANIES_FILE = "companies_data.json"
LOCATIONS_FILE = "locations_data.json"

# Default job categories
DEFAULT_CATEGORIES = [
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

JOB_TYPES = {
    "Arbeit": 1,
    "Ausbildung/Duales Studium": 34,
    "Selbstständigkeit": 4
}

# Praktikum uses same API parameter as Ausbildung but is treated separately
PRAKTIKUM_KEYWORDS = ['praktikum', 'praktikant', 'intern', 'internship']


class JobScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'X-API-Key': API_KEY,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def search_jobs(self, job_category, angebotsart=1, page=1, size=100):
        """Search for jobs using the Arbeitsagentur API"""
        endpoint = f"{BASE_URL}/pc/v4/app/jobs"
        
        params = {
            'was': job_category,
            'angebotsart': angebotsart,
            'page': page,
            'size': size
        }
        
        try:
            response = self.session.get(endpoint, params=params, timeout=15)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"  Error searching jobs: {e}")
            return None
    
    def get_job_count(self, job_category, angebotsart=1):
        """Get total count of jobs for a category and job type"""
        result = self.search_jobs(job_category, angebotsart, page=1, size=1)
        
        if result and 'maxErgebnisse' in result:
            count = int(result['maxErgebnisse'])
            print(f"  Found {count} jobs for '{job_category}' (Angebotsart: {angebotsart})")
            return count
        
        return 0
    
    def scrape_all_categories(self, job_categories):
        """Scrape job counts for all categories and job types"""
        results = []
        timestamp = datetime.now().isoformat()
        
        print(f"\nStarting scrape at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        for category in job_categories:
            print(f"Scraping: {category}")
            
            for job_type_name, job_type_id in JOB_TYPES.items():
                count = self.get_job_count(category, job_type_id)
                
                results.append({
                    'timestamp': timestamp,
                    'date': datetime.now().strftime('%Y-%m-%d'),
                    'category': category,
                    'job_type': job_type_name,
                    'job_type_id': job_type_id,
                    'count': count
                })
                
                time.sleep(0.5)
        
        print(f"Scraping completed: {len(results)} entries\n")
        return results
    
    def save_results(self, results):
        """Save results to JSON and CSV"""
        # Save to JSON
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                existing_data = json.load(f)
        except FileNotFoundError:
            existing_data = []
        
        existing_data.extend(results)
        
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(existing_data, f, indent=2, ensure_ascii=False)
        
        # Save to CSV
        df = pd.DataFrame(results)
        
        try:
            existing_df = pd.read_csv(HISTORY_FILE)
            df = pd.concat([existing_df, df], ignore_index=True)
        except FileNotFoundError:
            pass
        
        df.to_csv(HISTORY_FILE, index=False, encoding='utf-8')
        return df
    
    def load_history(self):
        """Load historical data"""
        try:
            df = pd.read_csv(HISTORY_FILE)
            return df
        except FileNotFoundError:
            return pd.DataFrame()
    
    def scrape_detailed_jobs(self, job_category, angebotsart=1, max_results=100):
        """Scrape detailed job information with efficient parallel pagination"""
        
        # Step 1: Get total count from first request
        first_result = self.search_jobs(job_category, angebotsart, page=1, size=50)
        if not first_result or 'maxErgebnisse' not in first_result:
            print(f"No results found for {job_category}")
            return []
        
        total_available = first_result['maxErgebnisse']
        print(f"Found {total_available} total jobs for '{job_category}' (Angebotsart: {angebotsart})")
        
        # Limit to max_results or total available
        total_to_fetch = min(max_results, total_available)
        
        # Step 2: Calculate number of pages needed
        page_size = 50
        num_pages = math.ceil(total_to_fetch / page_size)
        print(f"Fetching {total_to_fetch} jobs across {num_pages} pages in parallel...")
        
        # Step 3: Fetch all pages in parallel
        jobs = []
        
        def fetch_page(page_num):
            """Fetch a single page of results"""
            try:
                result = self.search_jobs(job_category, angebotsart, page=page_num, size=page_size)
                if result and 'stellenangebote' in result:
                    return result['stellenangebote']
            except Exception as e:
                print(f"Error fetching page {page_num}: {e}")
            return []
        
        # Use ThreadPoolExecutor for parallel requests
        with ThreadPoolExecutor(max_workers=5) as executor:
            # Submit all page requests
            future_to_page = {executor.submit(fetch_page, page): page for page in range(1, num_pages + 1)}
            
            # Collect results as they complete
            for future in as_completed(future_to_page):
                page_num = future_to_page[future]
                try:
                    stellenangebote = future.result()
                    
                    # Process each job in this page
                    for job in stellenangebote:
                        if len(jobs) >= total_to_fetch:
                            break
                            
                        title = job.get('titel', '')
                        
                        # Determine if it's Praktikum based on title keywords
                        job_type_name = self._get_job_type_name(angebotsart)
                        if angebotsart == 34:  # Ausbildung/Praktikum parameter
                            title_lower = title.lower()
                            is_praktikum = any(keyword in title_lower for keyword in PRAKTIKUM_KEYWORDS)
                            job_type_name = 'Praktikum' if is_praktikum else 'Ausbildung/Duales Studium'
                        
                        job_data = {
                            'title': title,
                            'company': job.get('arbeitgeber', ''),
                            'category': job_category,
                            'job_type': job_type_name,
                            'job_id': job.get('hashId', ''),
                            'url': f"https://www.arbeitsagentur.de/jobsuche/jobdetail/{job.get('hashId', '')}" if job.get('hashId') else '',
                            'location': {}
                        }
                        
                        # Extract location data
                        if 'arbeitsort' in job:
                            location = job['arbeitsort']
                            job_data['location'] = {
                                'city': location.get('ort', ''),
                                'plz': location.get('plz', ''),
                                'region': location.get('region', ''),
                                'lat': location.get('koordinaten', {}).get('lat'),
                                'lon': location.get('koordinaten', {}).get('lon')
                            }
                        
                        jobs.append(job_data)
                        
                except Exception as e:
                    print(f"Error processing page {page_num}: {e}")
        
        print(f"Successfully fetched {len(jobs)} jobs for '{job_category}'")
        return jobs[:total_to_fetch]  # Ensure we don't exceed the limit
    
    def _get_job_type_name(self, angebotsart):
        """Get job type name from ID"""
        for name, id in JOB_TYPES.items():
            if id == angebotsart:
                return name
        return "Unknown"
    
    def scrape_all_detailed(self, job_categories=None, max_per_category=50):
        """Scrape detailed information for all categories and job types"""
        if job_categories is None:
            job_categories = DEFAULT_CATEGORIES
        
        all_jobs = []
        
        print(f"\nStarting detailed scrape at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        for category in job_categories:
            print(f"Scraping detailed: {category}")
            
            for job_type_name, job_type_id in JOB_TYPES.items():
                jobs = self.scrape_detailed_jobs(category, job_type_id, max_per_category)
                all_jobs.extend(jobs)
                print(f"  {job_type_name}: {len(jobs)} jobs")
                time.sleep(0.5)
        
        print(f"Detailed scraping completed: {len(all_jobs)} jobs\n")
        return all_jobs
    
    def save_detailed_data(self, jobs):
        """Save detailed job data and extract companies/locations"""
        # Save all detailed jobs
        with open(DETAILED_DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(jobs, f, indent=2, ensure_ascii=False)
        
        # Extract and save companies data
        companies_by_type = {}
        for job in jobs:
            job_type = job.get('job_type', 'Unknown')
            company = job.get('company', '').strip()
            
            if not company or company == '':
                continue
            
            if job_type not in companies_by_type:
                companies_by_type[job_type] = []
            
            companies_by_type[job_type].append(company)
        
        # Count and sort companies
        companies_data = {}
        for job_type, companies in companies_by_type.items():
            counter = Counter(companies)
            companies_data[job_type] = [
                {'name': name, 'count': count, 'visible': True}
                for name, count in counter.most_common()
            ]
        
        with open(COMPANIES_FILE, 'w', encoding='utf-8') as f:
            json.dump(companies_data, f, indent=2, ensure_ascii=False)
        
        # Extract and save locations data
        locations = []
        for job in jobs:
            loc = job.get('location', {})
            if loc.get('lat') and loc.get('lon'):
                locations.append({
                    'city': loc.get('city', ''),
                    'plz': loc.get('plz', ''),
                    'region': loc.get('region', ''),
                    'lat': loc.get('lat'),
                    'lon': loc.get('lon'),
                    'category': job.get('category', ''),
                    'job_type': job.get('job_type', ''),
                    'company': job.get('company', ''),
                    'title': job.get('title', ''),
                    'url': job.get('url', '')
                })
        
        with open(LOCATIONS_FILE, 'w', encoding='utf-8') as f:
            json.dump(locations, f, indent=2, ensure_ascii=False)
        
        # NEW: Also update job_data.json for consistency
        self._update_simple_counts_from_detailed(jobs)
        
        return {
            'jobs': len(jobs),
            'companies': sum(len(c) for c in companies_data.values()),
            'locations': len(locations)
        }
    
    def _update_simple_counts_from_detailed(self, detailed_jobs):
        """Synchronize job_data.json with detailed job data for consistency"""
        # Count jobs by category and job_type
        counts_by_key = {}
        
        for job in detailed_jobs:
            category = job.get('category', 'Unknown')
            job_type = job.get('job_type', 'Unknown')
            key = (category, job_type)
            counts_by_key[key] = counts_by_key.get(key, 0) + 1
        
        # Create job_data.json format
        date_today = datetime.now().strftime('%Y-%m-%d')
        simple_data = []
        
        for (category, job_type), count in counts_by_key.items():
            simple_data.append({
                'category': category,
                'job_type': job_type,
                'count': count,
                'date': date_today
            })
        
        # Save to job_data.json
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(simple_data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Synchronized job_data.json: {len(simple_data)} entries, {sum(counts_by_key.values())} total jobs")
    
    def load_locations_data(self):
        """Load locations data"""
        try:
            with open(LOCATIONS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    
    def load_companies_data(self):
        """Load companies data"""
        try:
            with open(COMPANIES_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
    
    def update_company_visibility(self, job_type, company_name, visible=True):
        """Update company visibility"""
        companies_data = self.load_companies_data()
        
        if job_type in companies_data:
            for company in companies_data[job_type]:
                if company['name'] == company_name:
                    company['visible'] = visible
                    break
        
        with open(COMPANIES_FILE, 'w', encoding='utf-8') as f:
            json.dump(companies_data, f, indent=2, ensure_ascii=False)
        
        return companies_data


# Initialize scraper
scraper = JobScraper()


# API Routes
@app.route('/')
def index():
    """Serve the main HTML page"""
    return send_from_directory('.', 'index.html')


@app.route('/<path:path>')
def serve_static(path):
    """Serve static files"""
    return send_from_directory('.', path)


@app.route('/api/scrape', methods=['POST'])
def scrape():
    """Trigger scraping"""
    try:
        data = request.get_json()
        categories = data.get('categories', DEFAULT_CATEGORIES)
        
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
        
        data = df.to_dict('records')
        return jsonify(data)
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500


@app.route('/api/categories', methods=['GET'])
def get_categories():
    """Get current job categories"""
    return jsonify(DEFAULT_CATEGORIES)


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


@app.route('/api/scrape-detailed', methods=['POST'])
def scrape_detailed():
    """Trigger detailed scraping with location and company data"""
    try:
        data = request.get_json()
        categories = data.get('categories', DEFAULT_CATEGORIES)
        max_per_category = data.get('max_per_category', 50)
        
        jobs = scraper.scrape_all_detailed(categories, max_per_category)
        stats = scraper.save_detailed_data(jobs)
        
        return jsonify({
            'success': True,
            'stats': stats,
            'message': 'Detailed scraping completed successfully'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/locations', methods=['GET'])
def get_locations():
    """Get all location data for heatmap with statistics"""
    try:
        locations = scraper.load_locations_data()
        
        # Load detailed jobs to calculate statistics
        try:
            with open(DETAILED_DATA_FILE, 'r', encoding='utf-8') as f:
                all_jobs = json.load(f)
        except FileNotFoundError:
            all_jobs = []
        
        # Calculate statistics
        total_jobs = len(all_jobs)
        jobs_with_location = len(locations)
        jobs_without_location = total_jobs - jobs_with_location
        
        # Group jobs without location by reason
        missing_location_details = []
        if jobs_without_location > 0:
            for job in all_jobs:
                loc = job.get('location', {})
                if not (loc.get('lat') and loc.get('lon')):
                    missing_location_details.append({
                        'title': job.get('title', 'Unknown'),
                        'company': job.get('company', 'Unknown'),
                        'category': job.get('category', 'Unknown'),
                        'job_type': job.get('job_type', 'Unknown'),
                        'location_text': loc.get('city', 'No location data')
                    })
        
        return jsonify({
            'locations': locations,
            'statistics': {
                'total_jobs': total_jobs,
                'jobs_with_location': jobs_with_location,
                'jobs_without_location': jobs_without_location,
                'location_coverage_percent': round((jobs_with_location / total_jobs * 100) if total_jobs > 0 else 0, 1),
                'missing_location_details': missing_location_details  # No limit - show all
            }
        })
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500


@app.route('/api/companies', methods=['GET', 'POST'])
def get_companies():
    """Get companies data with optional keyword filters"""
    try:
        # Check if filters are provided (POST request)
        include_keywords = []
        exclude_keywords = []
        
        if request.method == 'POST':
            data = request.get_json() or {}
            include_keywords = data.get('includeKeywords', [])
            exclude_keywords = data.get('excludeKeywords', [])
        
        # If no filters, return cached company data
        if not include_keywords and not exclude_keywords:
            companies = scraper.load_companies_data()
            return jsonify(companies)
        
        # If filters are provided, calculate from detailed jobs
        try:
            with open(DETAILED_DATA_FILE, 'r', encoding='utf-8') as f:
                all_jobs = json.load(f)
        except FileNotFoundError:
            return jsonify({})
        
        # Apply keyword filters
        filtered_jobs = apply_keyword_filters(all_jobs, include_keywords, exclude_keywords)
        
        # Aggregate by company and job type
        companies_by_type = {}
        for job in filtered_jobs:
            company = job.get('company', 'Unbekannt')
            job_type = job.get('job_type', 'Unbekannt')
            
            if job_type not in companies_by_type:
                companies_by_type[job_type] = {}
            
            if company not in companies_by_type[job_type]:
                companies_by_type[job_type][company] = {'name': company, 'count': 0, 'visible': True}
            
            companies_by_type[job_type][company]['count'] += 1
        
        # Convert to list format and sort
        result = {}
        for job_type, companies in companies_by_type.items():
            result[job_type] = sorted(
                companies.values(),
                key=lambda x: x['count'],
                reverse=True
            )
        
        return jsonify(result)
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500


@app.route('/api/companies/visibility', methods=['POST'])
def update_company_visibility_route():
    """Update company visibility"""
    try:
        data = request.get_json()
        job_type = data.get('job_type')
        company_name = data.get('company_name')
        visible = data.get('visible', True)
        
        companies = scraper.update_company_visibility(job_type, company_name, visible)
        
        return jsonify({
            'success': True,
            'companies': companies
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/data-status', methods=['GET'])
def get_data_status():
    """Get data consistency status between simple and detailed scraping"""
    try:
        # Load simple data (job_data.json)
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                simple_data = json.load(f)
            simple_total = sum(d.get('count', 0) for d in simple_data)
            simple_date = simple_data[0].get('date', 'Unknown') if simple_data else 'No data'
        except FileNotFoundError:
            simple_total = 0
            simple_date = 'No data'
        
        # Load detailed data (job_details.json)
        try:
            with open(DETAILED_DATA_FILE, 'r', encoding='utf-8') as f:
                detailed_data = json.load(f)
            detailed_total = len(detailed_data)
            # Get most recent date from detailed data
            if detailed_data:
                # Assuming jobs have a scraped_at or similar field, or use file modification time
                import os
                detailed_date = datetime.fromtimestamp(os.path.getmtime(DETAILED_DATA_FILE)).strftime('%Y-%m-%d')
            else:
                detailed_date = 'No data'
        except FileNotFoundError:
            detailed_total = 0
            detailed_date = 'No data'
        
        # Check consistency
        difference = abs(simple_total - detailed_total)
        is_consistent = difference <= 10  # Allow small difference
        
        status = {
            'simple_scraping': {
                'total_jobs': simple_total,
                'last_updated': simple_date,
                'source': 'job_data.json'
            },
            'detailed_scraping': {
                'total_jobs': detailed_total,
                'last_updated': detailed_date,
                'source': 'job_details.json'
            },
            'consistency': {
                'is_consistent': is_consistent,
                'difference': difference,
                'message': 'Data is synchronized' if is_consistent else f'Data mismatch: {difference} jobs difference'
            }
        }
        
        return jsonify(status)
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500


@app.route('/api/jobs/by-category', methods=['GET', 'POST'])
def get_jobs_by_category():
    """Get detailed jobs for a specific category and job type with optional keyword filters
    Supports both GET (backward compatible, no filters) and POST (with filters)"""
    try:
        # Support both GET and POST
        if request.method == 'POST':
            data = request.get_json() or {}
            category = data.get('category', '')
            job_type = data.get('job_type', '')
            include_keywords = data.get('includeKeywords', [])
            exclude_keywords = data.get('excludeKeywords', [])
        else:  # GET - backward compatible
            category = request.args.get('category', '')
            job_type = request.args.get('job_type', '')
            include_keywords = []
            exclude_keywords = []
        
        # Load detailed jobs
        try:
            with open(DETAILED_DATA_FILE, 'r', encoding='utf-8') as f:
                all_jobs = json.load(f)
        except FileNotFoundError:
            return jsonify([])
        
        # Filter by category and job type first
        filtered_jobs = []
        for job in all_jobs:
            if job.get('category', '') == category:
                if job_type and job.get('job_type', '') != job_type:
                    continue
                filtered_jobs.append(job)
        
        # Apply keyword filters (only if provided)
        if include_keywords or exclude_keywords:
            filtered_jobs = apply_keyword_filters(filtered_jobs, include_keywords, exclude_keywords)
        
        # Format response
        result = []
        for job in filtered_jobs:
            loc = job.get('location', {})
            result.append({
                'title': job.get('title', ''),
                'company': job.get('company', ''),
                'url': job.get('url', ''),
                'category': job.get('category', ''),
                'job_type': job.get('job_type', ''),
                'city': loc.get('city', '')
            })
        
        return jsonify(result)
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


def apply_keyword_filters(jobs, include_keywords=None, exclude_keywords=None):
    """
    Modular filter function for keyword-based job filtering.
    
    Args:
        jobs: List of job dictionaries with 'title' field
        include_keywords: List of dicts with 'keyword' and 'matchType' ('whole' or 'partial')
        exclude_keywords: List of dicts with 'keyword' and 'matchType' ('whole' or 'partial')
    
    Returns:
        Filtered list of jobs
    """
    if not jobs:
        return []
    
    filtered = jobs.copy()
    
    # Apply include filter first (if specified)
    if include_keywords and len(include_keywords) > 0:
        included = []
        for job in filtered:
            title = job.get('title', '')
            if not title:
                continue
            
            # Check if job matches ANY include keyword (OR logic)
            matches_include = False
            for kw_obj in include_keywords:
                keyword = kw_obj.get('keyword', '')
                match_type = kw_obj.get('matchType', 'partial')
                
                if match_type == 'whole':
                    # Whole word match (case-insensitive)
                    pattern = r'\b' + re.escape(keyword) + r'\b'
                    if re.search(pattern, title, re.IGNORECASE):
                        matches_include = True
                        break
                else:
                    # Partial match (case-insensitive)
                    if keyword.lower() in title.lower():
                        matches_include = True
                        break
            
            if matches_include:
                included.append(job)
        
        filtered = included
    
    # Apply exclude filter (if specified)
    if exclude_keywords and len(exclude_keywords) > 0:
        excluded = []
        for job in filtered:
            title = job.get('title', '')
            if not title:
                excluded.append(job)
                continue
            
            # Check if job matches ANY exclude keyword (OR logic for exclusion)
            should_exclude = False
            for kw_obj in exclude_keywords:
                keyword = kw_obj.get('keyword', '')
                match_type = kw_obj.get('matchType', 'partial')
                
                if match_type == 'whole':
                    # Whole word match (case-insensitive)
                    pattern = r'\b' + re.escape(keyword) + r'\b'
                    if re.search(pattern, title, re.IGNORECASE):
                        should_exclude = True
                        break
                else:
                    # Partial match (case-insensitive)
                    if keyword.lower() in title.lower():
                        should_exclude = True
                        break
            
            if not should_exclude:
                excluded.append(job)
        
        filtered = excluded
    
    return filtered


@app.route('/api/jobs/filtered', methods=['POST'])
def get_filtered_jobs():
    """
    Get filtered and aggregated job data based on include/exclude keywords.
    Returns aggregated counts per category and job type for use in charts.
    """
    try:
        data = request.get_json()
        include_keywords = data.get('includeKeywords', [])
        exclude_keywords = data.get('excludeKeywords', [])
        
        # Load detailed jobs
        try:
            with open(DETAILED_DATA_FILE, 'r', encoding='utf-8') as f:
                all_jobs = json.load(f)
        except FileNotFoundError:
            return jsonify({
                'aggregated': [],
                'total_jobs': 0,
                'filtered_jobs': 0
            })
        
        total_before = len(all_jobs)
        
        # Apply filters
        filtered_jobs = apply_keyword_filters(all_jobs, include_keywords, exclude_keywords)
        
        # Aggregate by category and job_type
        aggregated = {}
        for job in filtered_jobs:
            category = job.get('category', 'Unknown')
            job_type = job.get('job_type', 'Unknown')
            key = f"{category}|{job_type}"
            
            if key not in aggregated:
                aggregated[key] = {
                    'category': category,
                    'job_type': job_type,
                    'count': 0
                }
            aggregated[key]['count'] += 1
        
        # Convert to list
        result = list(aggregated.values())
        
        return jsonify({
            'aggregated': result,
            'total_jobs': total_before,
            'filtered_jobs': len(filtered_jobs),
            'filters_applied': {
                'include': len(include_keywords) > 0,
                'exclude': len(exclude_keywords) > 0
            }
        })
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500


@app.route('/api/jobs/by-city', methods=['GET', 'POST'])
def get_jobs_by_city():
    """Get detailed jobs for a specific city with optional keyword filters
    Supports both GET (backward compatible, no filters) and POST (with filters)"""
    try:
        # Support both GET and POST
        if request.method == 'POST':
            data = request.get_json() or {}
            city = data.get('city', '')
            job_type = data.get('job_type', '')
            category = data.get('category', '')
            include_keywords = data.get('includeKeywords', [])
            exclude_keywords = data.get('excludeKeywords', [])
        else:  # GET - backward compatible
            city = request.args.get('city', '')
            job_type = request.args.get('job_type', '')
            category = request.args.get('category', '')
            include_keywords = []
            exclude_keywords = []
        
        # Load detailed jobs
        try:
            with open(DETAILED_DATA_FILE, 'r', encoding='utf-8') as f:
                all_jobs = json.load(f)
        except FileNotFoundError:
            return jsonify([])
        
        # Filter by city, job type, and category first
        filtered_jobs = []
        for job in all_jobs:
            loc = job.get('location', {})
            if loc.get('city', '') == city:
                if job_type and job.get('job_type', '') != job_type:
                    continue
                if category and job.get('category', '') != category:
                    continue
                filtered_jobs.append(job)
        
        # Apply keyword filters (only if provided)
        if include_keywords or exclude_keywords:
            filtered_jobs = apply_keyword_filters(filtered_jobs, include_keywords, exclude_keywords)
        
        # Format response
        result = []
        for job in filtered_jobs:
            loc = job.get('location', {})
            result.append({
                'title': job.get('title', ''),
                'company': job.get('company', ''),
                'url': job.get('url', ''),
                'category': job.get('category', ''),
                'job_type': job.get('job_type', ''),
                'city': loc.get('city', '')
            })
        
        return jsonify(result)
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500


@app.route('/api/jobs/by-company', methods=['GET', 'POST'])
def get_jobs_by_company():
    """Get detailed jobs for a specific company with optional keyword filters
    Supports both GET (backward compatible, no filters) and POST (with filters)"""
    try:
        # Support both GET and POST
        if request.method == 'POST':
            data = request.get_json() or {}
            company = data.get('company', '')
            job_type = data.get('job_type', '')
            include_keywords = data.get('includeKeywords', [])
            exclude_keywords = data.get('excludeKeywords', [])
        else:  # GET - backward compatible
            company = request.args.get('company', '')
            job_type = request.args.get('job_type', '')
            include_keywords = []
            exclude_keywords = []
        
        # Load detailed jobs
        try:
            with open(DETAILED_DATA_FILE, 'r', encoding='utf-8') as f:
                all_jobs = json.load(f)
        except FileNotFoundError:
            return jsonify([])
        
        # Filter by company and job type first
        filtered_jobs = []
        for job in all_jobs:
            if job.get('company', '') == company:
                if job_type and job.get('job_type', '') != job_type:
                    continue
                filtered_jobs.append(job)
        
        # Apply keyword filters (only if provided)
        if include_keywords or exclude_keywords:
            filtered_jobs = apply_keyword_filters(filtered_jobs, include_keywords, exclude_keywords)
        
        # Format response
        result = []
        for job in filtered_jobs:
            loc = job.get('location', {})
            result.append({
                'title': job.get('title', ''),
                'company': job.get('company', ''),
                'url': job.get('url', ''),
                'category': job.get('category', ''),
                'job_type': job.get('job_type', ''),
                'city': loc.get('city', '')
            })
        
        return jsonify(result)
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500


if __name__ == '__main__':
    print("🚀 Starting Standalone Webapp Server")
    print("=" * 50)
    print("🌐 Open your browser to: http://localhost:5000")
    print("\n📊 API Endpoints:")
    print("   POST /api/scrape - Trigger scraping")
    print("   POST /api/scrape-detailed - Trigger detailed scraping")
    print("   GET  /api/data - Get all data")
    print("   GET  /api/categories - Get job categories")
    print("   GET  /api/stats - Get statistics")
    print("   GET  /api/locations - Get location data")
    print("   GET  /api/companies - Get companies data")
    print("   POST /api/companies/visibility - Update company visibility")
    print("   GET  /api/health - Health check")
    print("\nPress Ctrl+C to stop")
    print("=" * 50)
    print()
    
    app.run(debug=True, host='0.0.0.0', port=5000)

# Made with Bob
