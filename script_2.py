# Create Data-tracker repository integration module
data_tracker_module = '''
import pandas as pd
import json
import os
from datetime import datetime
import logging
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

class DataTrackerConnector:
    """Integration with existing Data-tracker repository"""
    
    def __init__(self):
        self.repo_path = os.getenv('DATA_TRACKER_REPO_PATH', '../Data-tracker')
        self.backup_path = os.getenv('BACKUP_DATA_PATH', './data/backups')
        self.ensure_directories()
    
    def ensure_directories(self):
        """Create necessary directories"""
        os.makedirs(self.backup_path, exist_ok=True)
        os.makedirs('./data/processed', exist_ok=True)
        
    def load_existing_data(self):
        """Load data from Data-tracker repository"""
        try:
            # Check for existing CSV files
            data_files = {
                'brands': f'{self.repo_path}/brands_data.csv',
                'metrics': f'{self.repo_path}/social_metrics.csv', 
                'campaigns': f'{self.repo_path}/campaign_data.csv',
                'leads': f'{self.repo_path}/leads_data.csv'
            }
            
            loaded_data = {}
            
            for data_type, file_path in data_files.items():
                if os.path.exists(file_path):
                    loaded_data[data_type] = pd.read_csv(file_path)
                    logger.info(f"Loaded {data_type} data from {file_path}")
                else:
                    logger.warning(f"Data file not found: {file_path}")
                    loaded_data[data_type] = pd.DataFrame()
            
            return loaded_data
            
        except Exception as e:
            logger.error(f"Error loading Data-tracker data: {str(e)}")
            return {}
    
    def sync_with_repository(self, dashboard_data):
        """Sync dashboard data with Data-tracker repository"""
        try:
            # Convert dashboard data to DataFrames
            brands_df = self.create_brands_dataframe(dashboard_data)
            metrics_df = self.create_metrics_dataframe(dashboard_data)
            
            # Save to Data-tracker repository
            brands_df.to_csv(f'{self.repo_path}/dashboard_brands.csv', index=False)
            metrics_df.to_csv(f'{self.repo_path}/dashboard_metrics.csv', index=False)
            
            # Create backup
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            brands_df.to_csv(f'{self.backup_path}/brands_backup_{timestamp}.csv', index=False)
            metrics_df.to_csv(f'{self.backup_path}/metrics_backup_{timestamp}.csv', index=False)
            
            logger.info("Data successfully synced with Data-tracker repository")
            return True
            
        except Exception as e:
            logger.error(f"Error syncing with repository: {str(e)}")
            return False
    
    def create_brands_dataframe(self, dashboard_data):
        """Convert brand data to structured DataFrame"""
        brands_list = []
        
        for brand_name, brand_info in dashboard_data.items():
            brands_list.append({
                'brand_name': brand_name,
                'category': brand_info['category'],
                'website_traffic': brand_info['metrics']['website_traffic'],
                'primary_social_platform': brand_info['metrics']['primary_social_platform'],
                'social_followers': brand_info['metrics']['social_followers'],
                'engagement_rate': brand_info['metrics']['engagement_rate'],
                'leads': brand_info['metrics'].get('leads'),
                'operational_metric': brand_info['metrics']['operational_metric'],
                'operational_value': brand_info['metrics']['operational_value'],
                'insight': brand_info['insight'],
                'last_updated': datetime.now().isoformat()
            })
        
        return pd.DataFrame(brands_list)
    
    def create_metrics_dataframe(self, dashboard_data):
        """Convert metrics data to time-series DataFrame"""
        metrics_list = []
        current_time = datetime.now()
        
        for brand_name, brand_info in dashboard_data.items():
            metrics = brand_info['metrics']
            
            # Create individual metric records
            metric_records = [
                ('website_traffic', metrics['website_traffic']),
                ('social_followers', metrics['social_followers']),
                ('engagement_rate', metrics['engagement_rate']),
                ('operational_value', metrics['operational_value'])
            ]
            
            for metric_name, metric_value in metric_records:
                if metric_value is not None:
                    metrics_list.append({
                        'brand_name': brand_name,
                        'metric_name': metric_name,
                        'metric_value': metric_value,
                        'timestamp': current_time.isoformat(),
                        'quarter': 'Q3_2025'
                    })
        
        return pd.DataFrame(metrics_list)
    
    def get_historical_trends(self, brand_name, metric_name, periods=12):
        """Get historical trends for a specific brand and metric"""
        try:
            metrics_file = f'{self.repo_path}/dashboard_metrics.csv'
            if os.path.exists(metrics_file):
                df = pd.read_csv(metrics_file)
                brand_metrics = df[
                    (df['brand_name'] == brand_name) & 
                    (df['metric_name'] == metric_name)
                ].tail(periods)
                
                return brand_metrics.to_dict('records')
            else:
                return []
                
        except Exception as e:
            logger.error(f"Error getting historical trends: {str(e)}")
            return []

class NotionDatabaseConnector:
    """Integration with Notion database for brand books"""
    
    def __init__(self):
        self.api_key = os.getenv('NOTION_API_KEY')
        self.database_id = os.getenv('NOTION_DATABASE_ID')
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
            'Notion-Version': '2022-06-28'
        }
    
    def create_brand_book_entry(self, brand_name, brand_data):
        """Create or update brand book entry in Notion"""
        try:
            import requests
            
            # Prepare Notion page properties
            properties = {
                "Brand Name": {
                    "title": [{"text": {"content": brand_name}}]
                },
                "Category": {
                    "select": {"name": brand_data['category']}
                },
                "Website Traffic": {
                    "number": brand_data['metrics']['website_traffic']
                },
                "Social Followers": {
                    "number": brand_data['metrics']['social_followers']
                },
                "Last Updated": {
                    "date": {"start": datetime.now().isoformat()}
                }
            }
            
            # Create page content
            children = [
                {
                    "object": "block",
                    "type": "heading_2",
                    "heading_2": {
                        "rich_text": [{"text": {"content": "Strategic Insight"}}]
                    }
                },
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [{"text": {"content": brand_data['insight']}}]
                    }
                },
                {
                    "object": "block",
                    "type": "heading_2",
                    "heading_2": {
                        "rich_text": [{"text": {"content": "Market Trends"}}]
                    }
                }
            ]
            
            # Add trend bullets
            for trend in brand_data['trends']:
                children.append({
                    "object": "block",
                    "type": "bulleted_list_item",
                    "bulleted_list_item": {
                        "rich_text": [{"text": {"content": trend}}]
                    }
                })
            
            payload = {
                "parent": {"database_id": self.database_id},
                "properties": properties,
                "children": children
            }
            
            response = requests.post(
                "https://api.notion.com/v1/pages",
                headers=self.headers,
                json=payload
            )
            
            if response.status_code == 200:
                logger.info(f"Brand book entry created for {brand_name}")
                return response.json()
            else:
                logger.error(f"Notion API error: {response.status_code}")
                return None
                
        except Exception as e:
            logger.error(f"Error creating Notion entry: {str(e)}")
            return None

def initialize_data_connections():
    """Initialize all data connections"""
    connections = {
        'data_tracker': DataTrackerConnector(),
        'notion': NotionDatabaseConnector()
    }
    
    logger.info("Data connections initialized")
    return connections

if __name__ == "__main__":
    # Test the connections
    connections = initialize_data_connections()
    
    # Load existing data from Data-tracker
    existing_data = connections['data_tracker'].load_existing_data()
    print(f"Loaded data types: {list(existing_data.keys())}")
    
    print("Data integration modules ready!")
'''

with open('data_integration.py', 'w') as f:
    f.write(data_tracker_module)

print("✅ Data-tracker integration module created")