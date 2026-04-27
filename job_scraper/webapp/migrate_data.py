#!/usr/bin/env python3
"""
Migration script to update old data format to new format
- Renames "Ausbildung" to "Ausbildung/Duales Studium"
- Separates "Praktikum" based on keywords
"""

import json
import os

# Files to migrate
DATA_FILE = "job_data.json"
DETAILED_DATA_FILE = "job_details.json"
LOCATIONS_FILE = "locations_data.json"
COMPANIES_FILE = "companies_data.json"

PRAKTIKUM_KEYWORDS = ['praktikum', 'praktikant', 'intern', 'internship']

def migrate_job_data():
    """Migrate job_data.json"""
    if not os.path.exists(DATA_FILE):
        print(f"❌ {DATA_FILE} not found")
        return
    
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    updated = 0
    for job in data:
        if job.get('job_type') == 'Ausbildung':
            job['job_type'] = 'Ausbildung/Duales Studium'
            updated += 1
    
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ {DATA_FILE}: {updated} entries updated")

def migrate_detailed_data():
    """Migrate job_details.json and separate Praktikum"""
    if not os.path.exists(DETAILED_DATA_FILE):
        print(f"❌ {DETAILED_DATA_FILE} not found")
        return
    
    with open(DETAILED_DATA_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    updated_ausbildung = 0
    updated_praktikum = 0
    
    for job in data:
        if job.get('job_type') == 'Ausbildung':
            title = job.get('title', '').lower()
            is_praktikum = any(keyword in title for keyword in PRAKTIKUM_KEYWORDS)
            
            if is_praktikum:
                job['job_type'] = 'Praktikum'
                updated_praktikum += 1
            else:
                job['job_type'] = 'Ausbildung/Duales Studium'
                updated_ausbildung += 1
    
    with open(DETAILED_DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ {DETAILED_DATA_FILE}: {updated_ausbildung} → Ausbildung/Duales Studium, {updated_praktikum} → Praktikum")

def migrate_locations_data():
    """Migrate locations_data.json"""
    if not os.path.exists(LOCATIONS_FILE):
        print(f"❌ {LOCATIONS_FILE} not found")
        return
    
    with open(LOCATIONS_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    updated_ausbildung = 0
    updated_praktikum = 0
    
    for loc in data:
        if loc.get('job_type') == 'Ausbildung':
            title = loc.get('title', '').lower()
            is_praktikum = any(keyword in title for keyword in PRAKTIKUM_KEYWORDS)
            
            if is_praktikum:
                loc['job_type'] = 'Praktikum'
                updated_praktikum += 1
            else:
                loc['job_type'] = 'Ausbildung/Duales Studium'
                updated_ausbildung += 1
    
    with open(LOCATIONS_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ {LOCATIONS_FILE}: {updated_ausbildung} → Ausbildung/Duales Studium, {updated_praktikum} → Praktikum")

def migrate_companies_data():
    """Migrate companies_data.json"""
    if not os.path.exists(COMPANIES_FILE):
        print(f"❌ {COMPANIES_FILE} not found")
        return
    
    with open(COMPANIES_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Rename key if exists
    if 'Ausbildung' in data:
        data['Ausbildung/Duales Studium'] = data.pop('Ausbildung')
        print(f"✅ {COMPANIES_FILE}: Renamed 'Ausbildung' → 'Ausbildung/Duales Studium'")
    
    # Note: We can't separate Praktikum companies without detailed job data
    # This would require re-scraping
    
    with open(COMPANIES_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    print("🔄 Starting data migration...")
    print("=" * 50)
    
    migrate_job_data()
    migrate_detailed_data()
    migrate_locations_data()
    migrate_companies_data()
    
    print("=" * 50)
    print("✅ Migration complete!")
    print("\n⚠️  Note: For complete Praktikum separation, please run 'Detailliert Scrapen' again.")

# Made with Bob
