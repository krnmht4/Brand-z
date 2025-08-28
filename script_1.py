# Create requirements.txt file for the Streamlit app
requirements = '''streamlit==1.28.1
pandas==2.0.3
plotly==5.17.0
python-dotenv==1.0.0
requests==2.31.0
beautifulsoup4==4.12.2
lxml==4.9.3
schedule==1.2.0
openpyxl==3.1.2
groq==0.4.2
'''

with open('requirements.txt', 'w') as f:
    f.write(requirements)

print("✅ Requirements.txt created")

# Create .env template
env_template = '''# Social Media API Keys
LINKEDIN_ACCESS_TOKEN=your_linkedin_token_here
INSTAGRAM_ACCESS_TOKEN=your_instagram_token_here
FACEBOOK_ACCESS_TOKEN=your_facebook_token_here
TIKTOK_ACCESS_TOKEN=your_tiktok_token_here

# Data Sources
DATA_TRACKER_REPO_PATH=../Data-tracker
NOTION_API_KEY=your_notion_api_key_here
NOTION_DATABASE_ID=your_notion_database_id_here

# Workflow Automation
POWER_AUTOMATE_WEBHOOK=your_power_automate_webhook_url
N8N_WEBHOOK=your_n8n_webhook_url
MAKE_WEBHOOK=your_make_webhook_url

# Dashboard Settings
REFRESH_INTERVAL_HOURS=6
BACKUP_DATA_PATH=./data/backups
LOG_LEVEL=INFO
'''

with open('.env.template', 'w') as f:
    f.write(env_template)

print("✅ .env template created")

# Create social media API integration module
social_api_module = '''
import requests
import json
from datetime import datetime
import os
from dotenv import load_dotenv
import logging

load_dotenv()

# Setup logging
logging.basicConfig(level=getattr(logging, os.getenv('LOG_LEVEL', 'INFO')))
logger = logging.getLogger(__name__)

class SocialMediaConnector:
    """Social Media API integration for brand dashboard"""
    
    def __init__(self):
        self.linkedin_token = os.getenv('LINKEDIN_ACCESS_TOKEN')
        self.instagram_token = os.getenv('INSTAGRAM_ACCESS_TOKEN')
        self.facebook_token = os.getenv('FACEBOOK_ACCESS_TOKEN')
        self.tiktok_token = os.getenv('TIKTOK_ACCESS_TOKEN')
        
    def get_linkedin_metrics(self, company_id):
        """Fetch LinkedIn company page metrics"""
        try:
            headers = {'Authorization': f'Bearer {self.linkedin_token}'}
            
            # Followers endpoint
            followers_url = f"https://api.linkedin.com/v2/networkSizes/{company_id}?edgeType=CompanyFollowedByMember"
            followers_response = requests.get(followers_url, headers=headers)
            
            if followers_response.status_code == 200:
                followers_data = followers_response.json()
                follower_count = followers_data.get('firstDegreeSize', 0)
                
                return {
                    'platform': 'LinkedIn',
                    'followers': follower_count,
                    'engagement_rate': None,  # Requires additional API calls
                    'last_updated': datetime.now().isoformat()
                }
            else:
                logger.error(f"LinkedIn API error: {followers_response.status_code}")
                return None
                
        except Exception as e:
            logger.error(f"LinkedIn connection error: {str(e)}")
            return None
    
    def get_instagram_metrics(self, instagram_account_id):
        """Fetch Instagram business account metrics"""
        try:
            # Instagram Basic Display API
            base_url = "https://graph.instagram.com"
            
            # Get account info
            account_url = f"{base_url}/{instagram_account_id}?fields=account_type,media_count,followers_count&access_token={self.instagram_token}"
            account_response = requests.get(account_url)
            
            if account_response.status_code == 200:
                account_data = account_response.json()
                
                return {
                    'platform': 'Instagram',
                    'followers': account_data.get('followers_count', 0),
                    'media_count': account_data.get('media_count', 0),
                    'engagement_rate': None,  # Calculate from recent posts
                    'last_updated': datetime.now().isoformat()
                }
            else:
                logger.error(f"Instagram API error: {account_response.status_code}")
                return None
                
        except Exception as e:
            logger.error(f"Instagram connection error: {str(e)}")
            return None
    
    def get_facebook_metrics(self, page_id):
        """Fetch Facebook page metrics"""
        try:
            base_url = "https://graph.facebook.com/v18.0"
            
            # Get page info
            page_url = f"{base_url}/{page_id}?fields=name,fan_count,engagement&access_token={self.facebook_token}"
            page_response = requests.get(page_url)
            
            if page_response.status_code == 200:
                page_data = page_response.json()
                
                return {
                    'platform': 'Facebook',
                    'followers': page_data.get('fan_count', 0),
                    'engagement_rate': None,
                    'last_updated': datetime.now().isoformat()
                }
            else:
                logger.error(f"Facebook API error: {page_response.status_code}")
                return None
                
        except Exception as e:
            logger.error(f"Facebook connection error: {str(e)}")
            return None
    
    def refresh_all_brand_data(self, brand_config):
        """Refresh data for all brands"""
        updated_data = {}
        
        for brand_name, config in brand_config.items():
            brand_metrics = {}
            
            if 'linkedin_id' in config:
                linkedin_data = self.get_linkedin_metrics(config['linkedin_id'])
                if linkedin_data:
                    brand_metrics['linkedin'] = linkedin_data
            
            if 'instagram_id' in config:
                instagram_data = self.get_instagram_metrics(config['instagram_id'])
                if instagram_data:
                    brand_metrics['instagram'] = instagram_data
            
            if 'facebook_id' in config:
                facebook_data = self.get_facebook_metrics(config['facebook_id'])
                if facebook_data:
                    brand_metrics['facebook'] = facebook_data
            
            updated_data[brand_name] = brand_metrics
            
        return updated_data

def save_metrics_to_file(metrics_data, filename='social_metrics.json'):
    """Save metrics to JSON file"""
    with open(filename, 'w') as f:
        json.dump(metrics_data, f, indent=2)
    logger.info(f"Metrics saved to {filename}")

def load_metrics_from_file(filename='social_metrics.json'):
    """Load metrics from JSON file"""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.warning(f"Metrics file {filename} not found")
        return {}

if __name__ == "__main__":
    # Example usage
    connector = SocialMediaConnector()
    
    # Brand configuration with social media IDs
    brand_config = {
        "SpaceXec": {
            "linkedin_id": "spacexec"
        },
        "Aashi Realty": {
            "instagram_id": "aashi_realty",
            "facebook_id": "AashiRealty",
            "linkedin_id": "aashirealty"
        },
        "TravelXec": {
            "instagram_id": "travel.xec",
            "facebook_id": "TravelXec",
            "linkedin_id": "travelxec"
        },
        "Schmooze Media": {
            "instagram_id": "schmoozemedia",
            "facebook_id": "SchmoozeMedia",
            "linkedin_id": "schmooze-media"
        },
        "AutoXec": {
            "instagram_id": "autoxec"
        }
    }
    
    # Refresh data
    updated_metrics = connector.refresh_all_brand_data(brand_config)
    save_metrics_to_file(updated_metrics)
    
    print("Social media data refresh completed!")
'''

with open('social_media_connector.py', 'w') as f:
    f.write(social_api_module)

print("✅ Social media API connector created")