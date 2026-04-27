"""
Scheduler for daily job scraping
"""

import schedule
import time
from datetime import datetime
from scraper import run_daily_scrape


def job():
    """Job function to run daily"""
    print(f"\n{'='*50}")
    print(f"Running scheduled scrape at {datetime.now()}")
    print(f"{'='*50}\n")
    
    try:
        run_daily_scrape()
        print("\n✅ Scheduled scrape completed successfully!")
    except Exception as e:
        print(f"\n❌ Error during scheduled scrape: {e}")


def run_scheduler():
    """Run the scheduler"""
    # Schedule job to run daily at 9:00 AM
    schedule.every().day.at("09:00").do(job)
    
    print("🕐 Scheduler started!")
    print("📅 Job will run daily at 09:00")
    print("Press Ctrl+C to stop\n")
    
    # Run once immediately on startup
    print("Running initial scrape...")
    job()
    
    # Keep running
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute


if __name__ == "__main__":
    run_scheduler()

# Made with Bob
