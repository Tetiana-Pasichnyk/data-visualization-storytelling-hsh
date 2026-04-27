"""
Core scraper module for Arbeitsagentur job search using official API
"""

import requests
import json
import pandas as pd
from datetime import datetime
import time
from collections import Counter
from config import JOB_CATEGORIES, JOB_TYPES, DATA_FILE, HISTORY_FILE

# Additional data files
DETAILED_DATA_FILE = "job_details.json"
COMPANIES_FILE = "companies_data.json"
LOCATIONS_FILE = "locations_data.json"


class JobScraper:
    def __init__(self):
        self.session = requests.Session()
        self.api_key = "jobboerse-jobsuche"
        self.base_url = "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service"
        
        # Set headers with API key
        self.session.headers.update({
            'X-API-Key': self.api_key,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def search_jobs(self, job_category, angebotsart=1, page=1, size=100):
        """
        Search for jobs using the Arbeitsagentur API
        
        Args:
            job_category: Job title/category to search for
            angebotsart: 1=ARBEIT, 2=SELBSTAENDIGKEIT, 4=AUSBILDUNG, 34=PRAKTIKUM
            page: Page number
            size: Results per page (max 100)
        
        Returns:
            API response with job listings
        """
        endpoint = f"{self.base_url}/pc/v4/app/jobs"
        
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
        """
        Get total count of jobs for a category and job type
        
        Args:
            job_category: Job title/category to search for
            angebotsart: Job type (1, 2, 4, or 34)
        
        Returns:
            Total number of job listings
        """
        result = self.search_jobs(job_category, angebotsart, page=1, size=1)
        
        if result and 'maxErgebnisse' in result:
            count = int(result['maxErgebnisse'])
            print(f"  Found {count} jobs for '{job_category}' (Angebotsart: {angebotsart})")
            return count
        
        return 0
    
    def scrape_all_categories(self, job_categories=None):
        """Scrape job counts for all categories and job types"""
        if job_categories is None:
            job_categories = JOB_CATEGORIES
        
        results = []
        timestamp = datetime.now().isoformat()
        
        print(f"\n{'='*60}")
        print(f"Starting scrape at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*60}\n")
        
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
                
                # Be polite - add delay between requests
                time.sleep(0.5)
            
            print()  # Empty line between categories
        
        print(f"{'='*60}")
        print(f"Scraping completed: {len(results)} entries")
        print(f"{'='*60}\n")
        
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
        
        print(f"✅ Saved to {DATA_FILE}")
        
        # Save to CSV for history
        df = pd.DataFrame(results)
        
        try:
            existing_df = pd.read_csv(HISTORY_FILE)
            df = pd.concat([existing_df, df], ignore_index=True)
        except FileNotFoundError:
            pass
        
        df.to_csv(HISTORY_FILE, index=False, encoding='utf-8')
        print(f"✅ Saved to {HISTORY_FILE}")
        
        return df
    
    def load_history(self):
        """Load historical data"""
        try:
            df = pd.read_csv(HISTORY_FILE)
            return df
        except FileNotFoundError:
            return pd.DataFrame(columns=['timestamp', 'date', 'category', 'job_type', 'job_type_id', 'count'])
    
    def get_job_details(self, refnr):
        """
        Get detailed information about a specific job
        
        Args:
            refnr: Job reference number (needs to be base64 encoded)
        
        Returns:
            Job details
        """
        import base64
        encoded_refnr = base64.b64encode(refnr.encode()).decode()
        endpoint = f"{self.base_url}/pc/v4/jobdetails/{encoded_refnr}"
        
        try:
            response = self.session.get(endpoint, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error getting job details: {e}")
            return None


def run_daily_scrape():
    """Function to run daily scraping"""
    scraper = JobScraper()
    
    results = scraper.scrape_all_categories()
    df = scraper.save_results(results)
    
    print(f"\n📊 Summary:")
    print(f"   Total entries: {len(df)}")
    print(f"   Unique dates: {df['date'].nunique()}")
    print(f"   Categories: {df['category'].nunique()}")
    
    return df


if __name__ == "__main__":
    run_daily_scrape()

# Made with Bob

    
    def scrape_detailed_jobs(self, job_category, angebotsart=1, max_results=100):
        """
        Scrape detailed job information including location and company
        
        Args:
            job_category: Job title/category to search for
            angebotsart: Job type (1, 2, 4, or 34)
            max_results: Maximum number of results to fetch
        
        Returns:
            List of detailed job information
        """
        result = self.search_jobs(job_category, angebotsart, page=1, size=min(max_results, 100))
        
        if not result or 'stellenangebote' not in result:
            return []
        
        jobs = []
        for job in result['stellenangebote']:
            job_info = {
                'title': job.get('beruf', ''),
                'company': job.get('arbeitgeber', 'Unbekannt'),
                'location_city': job.get('arbeitsort', {}).get('ort', ''),
                'location_plz': job.get('arbeitsort', {}).get('plz', ''),
                'location_region': job.get('arbeitsort', {}).get('region', ''),
                'location_lat': job.get('arbeitsort', {}).get('koordinaten', {}).get('lat', None),
                'location_lon': job.get('arbeitsort', {}).get('koordinaten', {}).get('lon', None),
                'category': job_category,
                'job_type': [k for k, v in JOB_TYPES.items() if v == angebotsart][0],
                'date': datetime.now().strftime('%Y-%m-%d')
            }
            jobs.append(job_info)
        
        return jobs
    
    def scrape_all_detailed(self, job_categories=None, max_per_category=50):
        """Scrape detailed information for all categories"""
        if job_categories is None:
            job_categories = JOB_CATEGORIES
        
        all_jobs = []
        
        print(f"\n{'='*60}")
        print(f"Starting detailed scrape at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*60}\n")
        
        for category in job_categories:
            print(f"Scraping details for: {category}")
            
            for job_type_name, job_type_id in JOB_TYPES.items():
                jobs = self.scrape_detailed_jobs(category, job_type_id, max_per_category)
                all_jobs.extend(jobs)
                print(f"  {job_type_name}: {len(jobs)} jobs")
                time.sleep(1)
            
            print()
        
        print(f"{'='*60}")
        print(f"Detailed scraping completed: {len(all_jobs)} jobs")
        print(f"{'='*60}\n")
        
        return all_jobs
    
    def save_detailed_data(self, jobs):
        """Save detailed job data"""
        # Save all jobs
        try:
            with open(DETAILED_DATA_FILE, 'r', encoding='utf-8') as f:
                existing_data = json.load(f)
        except FileNotFoundError:
            existing_data = []
        
        existing_data.extend(jobs)
        
        with open(DETAILED_DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(existing_data, f, indent=2, ensure_ascii=False)
        
        # Extract and save companies data
        companies = {}
        for job in jobs:
            job_type = job['job_type']
            company = job['company']
            
            if job_type not in companies:
                companies[job_type] = Counter()
            
            companies[job_type][company] += 1
        
        # Convert to sorted lists
        companies_data = {}
        for job_type, counter in companies.items():
            companies_data[job_type] = [
                {'name': company, 'count': count}
                for company, count in counter.most_common()
            ]
        
        with open(COMPANIES_FILE, 'w', encoding='utf-8') as f:
            json.dump(companies_data, f, indent=2, ensure_ascii=False)
        
        # Extract and save locations data
        locations = []
        for job in jobs:
            if job['location_lat'] and job['location_lon']:
                locations.append({
                    'city': job['location_city'],
                    'plz': job['location_plz'],
                    'region': job['location_region'],
                    'lat': job['location_lat'],
                    'lon': job['location_lon'],
                    'category': job['category'],
                    'job_type': job['job_type'],
                    'company': job['company']
                })
        
        with open(LOCATIONS_FILE, 'w', encoding='utf-8') as f:
            json.dump(locations, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Saved {len(jobs)} detailed jobs")
        print(f"✅ Saved companies data for {len(companies_data)} job types")
        print(f"✅ Saved {len(locations)} locations with coordinates")
        
        return {
            'jobs': len(jobs),
            'companies': companies_data,
            'locations': len(locations)
        }
    
    def load_companies_data(self):
        """Load companies data"""
        try:
            with open(COMPANIES_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
    
    def load_locations_data(self):
        """Load locations data"""
        try:
            with open(LOCATIONS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    
    def update_company_visibility(self, job_type, company_name, visible=True):
        """Update company visibility (for hiding/showing in UI)"""
        try:
            with open(COMPANIES_FILE, 'r', encoding='utf-8') as f:
                companies_data = json.load(f)
        except FileNotFoundError:
            return False
        
        if job_type in companies_data:
            for company in companies_data[job_type]:
                if company['name'] == company_name:
                    company['visible'] = visible
                    break
            
            with open(COMPANIES_FILE, 'w', encoding='utf-8') as f:
                json.dump(companies_data, f, indent=2, ensure_ascii=False)
            
            return True
        
        return False
