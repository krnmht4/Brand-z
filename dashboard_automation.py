
import schedule
import time
import logging
from datetime import datetime
from social_media_connector import SocialMediaConnector, save_metrics_to_file, load_metrics_from_file
from data_integration import DataTrackerConnector, NotionDatabaseConnector
from workflow_automation import WorkflowAutomation
from dotenv import load_dotenv

load_dotenv()

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('dashboard_automation.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

class DashboardAutomation:
    """Main automation orchestrator for the brand dashboard"""

    def __init__(self):
        self.social_connector = SocialMediaConnector()
        self.data_tracker = DataTrackerConnector()
        self.notion_connector = NotionDatabaseConnector()
        self.workflow_automation = WorkflowAutomation()

        # Brand configuration
        self.brand_config = {
            "SpaceXec": {
                "linkedin_id": "spacexec",
                "category": "Commercial Real Estate"
            },
            "Aashi Realty": {
                "instagram_id": "aashi_realty",
                "facebook_id": "AashiRealty",
                "linkedin_id": "aashirealty",
                "category": "Residential Brokerage"
            },
            "TravelXec": {
                "instagram_id": "travel.xec",
                "facebook_id": "TravelXec",
                "linkedin_id": "travelxec",
                "category": "Online Travel Services"
            },
            "Schmooze Media": {
                "instagram_id": "schmoozemedia",
                "facebook_id": "SchmoozeMedia",
                "linkedin_id": "schmooze-media",
                "category": "Digital Marketing Agency"
            },
            "AutoXec": {
                "instagram_id": "autoxec",
                "category": "Automotive Retail"
            }
        }

        logger.info("Dashboard automation initialized")

    def hourly_social_media_refresh(self):
        """Refresh social media data every hour"""
        try:
            logger.info("Starting hourly social media data refresh")

            updated_metrics = self.social_connector.refresh_all_brand_data(self.brand_config)

            if updated_metrics:
                save_metrics_to_file(updated_metrics, 'data/social_metrics_latest.json')
                logger.info("Social media data refreshed successfully")

                # Trigger workflow notifications for significant changes
                self.workflow_automation.send_performance_alerts(updated_metrics)
            else:
                logger.warning("No social media data retrieved")

        except Exception as e:
            logger.error(f"Error in hourly refresh: {str(e)}")

    def daily_data_sync(self):
        """Daily sync with Data-tracker repository and Notion"""
        try:
            logger.info("Starting daily data synchronization")

            # Load latest social media data
            latest_metrics = load_metrics_from_file('data/social_metrics_latest.json')

            # Sync with Data-tracker repository
            if self.data_tracker.sync_with_repository(latest_metrics):
                logger.info("Data-tracker sync completed")

            # Update Notion database
            for brand_name, brand_data in latest_metrics.items():
                if brand_name in self.brand_config:
                    self.notion_connector.create_brand_book_entry(brand_name, {
                        'category': self.brand_config[brand_name]['category'],
                        'metrics': brand_data,
                        'insight': f"Updated metrics for {brand_name} on {datetime.now().strftime('%Y-%m-%d')}"
                    })

            logger.info("Daily synchronization completed")

        except Exception as e:
            logger.error(f"Error in daily sync: {str(e)}")

    def weekly_report_generation(self):
        """Generate and send weekly reports"""
        try:
            logger.info("Starting weekly report generation")

            # Load current data
            current_data = load_metrics_from_file('data/social_metrics_latest.json')

            # Trigger report workflows
            report_results = self.workflow_automation.trigger_weekly_report_workflows(current_data)

            logger.info(f"Weekly reports sent: {report_results}")

        except Exception as e:
            logger.error(f"Error in weekly report generation: {str(e)}")

    def setup_schedule(self):
        """Setup the automation schedule"""
        # Social media refresh every 6 hours
        schedule.every(6).hours.do(self.hourly_social_media_refresh)

        # Daily data sync at 9 AM IST
        schedule.every().day.at("09:00").do(self.daily_data_sync)

        # Weekly reports on Monday at 10 AM IST
        schedule.every().monday.at("10:00").do(self.weekly_report_generation)

        logger.info("Automation schedule configured:")
        logger.info("- Social media refresh: Every 6 hours")
        logger.info("- Data sync: Daily at 9:00 AM IST")
        logger.info("- Weekly reports: Monday at 10:00 AM IST")

    def run_automation(self):
        """Run the automation scheduler"""
        self.setup_schedule()

        logger.info("Dashboard automation started")
        logger.info("Press Ctrl+C to stop the automation")

        try:
            # Run initial sync
            logger.info("Performing initial data sync...")
            self.hourly_social_media_refresh()
            self.daily_data_sync()

            # Start scheduler
            while True:
                schedule.run_pending()
                time.sleep(60)  # Check every minute

        except KeyboardInterrupt:
            logger.info("Automation stopped by user")
        except Exception as e:
            logger.error(f"Automation error: {str(e)}")

def main():
    """Main function to start dashboard automation"""
    automation = DashboardAutomation()
    automation.run_automation()

if __name__ == "__main__":
    main()
