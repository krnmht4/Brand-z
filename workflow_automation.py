
import requests
import json
from datetime import datetime
import logging
from dotenv import load_dotenv
import os

load_dotenv()

logger = logging.getLogger(__name__)

class WorkflowAutomation:
    """Integration with Power Automate, n8n, and Make platforms"""

    def __init__(self):
        self.power_automate_webhook = os.getenv('POWER_AUTOMATE_WEBHOOK')
        self.n8n_webhook = os.getenv('N8N_WEBHOOK')
        self.make_webhook = os.getenv('MAKE_WEBHOOK')

    def trigger_power_automate_flow(self, brand_name, metrics_data, alert_type="update"):
        """Trigger Power Automate workflow"""
        try:
            if not self.power_automate_webhook:
                logger.warning("Power Automate webhook not configured")
                return False

            payload = {
                "brand_name": brand_name,
                "alert_type": alert_type,
                "metrics": metrics_data,
                "timestamp": datetime.now().isoformat(),
                "dashboard_url": "http://localhost:8501"  # Streamlit default
            }

            response = requests.post(
                self.power_automate_webhook,
                json=payload,
                headers={'Content-Type': 'application/json'}
            )

            if response.status_code == 200:
                logger.info(f"Power Automate flow triggered for {brand_name}")
                return True
            else:
                logger.error(f"Power Automate trigger failed: {response.status_code}")
                return False

        except Exception as e:
            logger.error(f"Power Automate error: {str(e)}")
            return False

    def trigger_n8n_workflow(self, brand_data, workflow_type="data_sync"):
        """Trigger n8n workflow for data processing"""
        try:
            if not self.n8n_webhook:
                logger.warning("n8n webhook not configured")
                return False

            payload = {
                "workflow_type": workflow_type,
                "brands": brand_data,
                "timestamp": datetime.now().isoformat()
            }

            response = requests.post(
                self.n8n_webhook,
                json=payload,
                headers={'Content-Type': 'application/json'}
            )

            if response.status_code == 200:
                logger.info(f"n8n workflow triggered: {workflow_type}")
                return True
            else:
                logger.error(f"n8n trigger failed: {response.status_code}")
                return False

        except Exception as e:
            logger.error(f"n8n workflow error: {str(e)}")
            return False

    def trigger_make_scenario(self, alert_data, scenario_type="performance_alert"):
        """Trigger Make.com scenario"""
        try:
            if not self.make_webhook:
                logger.warning("Make webhook not configured")
                return False

            payload = {
                "scenario_type": scenario_type,
                "data": alert_data,
                "timestamp": datetime.now().isoformat()
            }

            response = requests.post(
                self.make_webhook,
                json=payload,
                headers={'Content-Type': 'application/json'}
            )

            if response.status_code == 200:
                logger.info(f"Make scenario triggered: {scenario_type}")
                return True
            else:
                logger.error(f"Make trigger failed: {response.status_code}")
                return False

        except Exception as e:
            logger.error(f"Make scenario error: {str(e)}")
            return False

    def send_performance_alerts(self, brands_data):
        """Analyze performance and send alerts"""
        alerts_sent = []

        for brand_name, brand_data in brands_data.items():
            metrics = brand_data['metrics']

            # Check for performance thresholds
            alerts = self.check_performance_thresholds(brand_name, metrics)

            for alert in alerts:
                # Send to Power Automate for email/Teams notifications
                if self.trigger_power_automate_flow(brand_name, metrics, alert['type']):
                    alerts_sent.append({
                        'brand': brand_name,
                        'alert': alert,
                        'timestamp': datetime.now().isoformat()
                    })

        return alerts_sent

    def check_performance_thresholds(self, brand_name, metrics):
        """Check if metrics exceed alert thresholds"""
        alerts = []

        # Define thresholds (these should be configurable)
        thresholds = {
            'low_engagement': 2.0,  # Below 2% engagement rate
            'low_traffic': 10000,   # Below 10k monthly traffic
            'high_performance': {
                'engagement': 4.0,  # Above 4% engagement
                'traffic_growth': 50000  # Above 50k traffic for celebration
            }
        }

        # Check low engagement
        if metrics.get('engagement_rate') and metrics['engagement_rate'] < thresholds['low_engagement']:
            alerts.append({
                'type': 'low_engagement',
                'message': f"{brand_name} engagement rate ({metrics['engagement_rate']}%) below threshold",
                'severity': 'warning'
            })

        # Check low traffic
        if metrics['website_traffic'] < thresholds['low_traffic']:
            alerts.append({
                'type': 'low_traffic',
                'message': f"{brand_name} website traffic ({metrics['website_traffic']:,}) below threshold",
                'severity': 'warning'
            })

        # Check high performance (positive alerts)
        if metrics.get('engagement_rate') and metrics['engagement_rate'] > thresholds['high_performance']['engagement']:
            alerts.append({
                'type': 'high_engagement',
                'message': f"{brand_name} excellent engagement rate: {metrics['engagement_rate']}%",
                'severity': 'success'
            })

        if metrics['website_traffic'] > thresholds['high_performance']['traffic_growth']:
            alerts.append({
                'type': 'high_traffic',
                'message': f"{brand_name} strong website performance: {metrics['website_traffic']:,} visitors",
                'severity': 'success'
            })

        return alerts

    def create_weekly_report_data(self, brands_data):
        """Prepare data for weekly automated reports"""
        report_data = {
            'report_date': datetime.now().isoformat(),
            'quarter': 'Q3_2025',
            'total_brands': len(brands_data),
            'summary': {
                'total_traffic': sum([brand['metrics']['website_traffic'] for brand in brands_data.values()]),
                'total_followers': sum([brand['metrics']['social_followers'] for brand in brands_data.values()]),
                'avg_engagement': sum([brand['metrics'].get('engagement_rate', 0) for brand in brands_data.values() if brand['metrics'].get('engagement_rate')]) / 3
            },
            'brand_performance': []
        }

        for brand_name, brand_data in brands_data.items():
            brand_summary = {
                'name': brand_name,
                'category': brand_data['category'],
                'website_traffic': brand_data['metrics']['website_traffic'],
                'social_followers': brand_data['metrics']['social_followers'],
                'engagement_rate': brand_data['metrics'].get('engagement_rate'),
                'key_insight': brand_data['insight']
            }
            report_data['brand_performance'].append(brand_summary)

        return report_data

    def trigger_weekly_report_workflows(self, brands_data):
        """Trigger all weekly report workflows"""
        report_data = self.create_weekly_report_data(brands_data)

        results = {
            'power_automate': self.trigger_power_automate_flow("Portfolio", report_data, "weekly_report"),
            'n8n': self.trigger_n8n_workflow(report_data, "weekly_report"),
            'make': self.trigger_make_scenario(report_data, "weekly_report")
        }

        return results

def send_whatsapp_alert(message, phone_number=None):
    """Send WhatsApp alert using API (placeholder for Indian WhatsApp Business API)"""
    try:
        # This would integrate with WhatsApp Business API
        # Popular Indian providers: Gupshup, Karix, or direct WhatsApp Business API

        logger.info(f"WhatsApp alert sent: {message}")
        return True

    except Exception as e:
        logger.error(f"WhatsApp alert error: {str(e)}")
        return False

def create_telegram_notification(message, chat_id=None):
    """Send Telegram notification (popular in India for business alerts)"""
    try:
        telegram_token = os.getenv('TELEGRAM_BOT_TOKEN')
        if not telegram_token or not chat_id:
            logger.warning("Telegram credentials not configured")
            return False

        url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
        payload = {
            'chat_id': chat_id,
            'text': message,
            'parse_mode': 'Markdown'
        }

        response = requests.post(url, json=payload)

        if response.status_code == 200:
            logger.info("Telegram notification sent successfully")
            return True
        else:
            logger.error(f"Telegram notification failed: {response.status_code}")
            return False

    except Exception as e:
        logger.error(f"Telegram notification error: {str(e)}")
        return False

if __name__ == "__main__":
    # Example usage
    automation = WorkflowAutomation()

    # Sample brand data for testing
    sample_brands = {
        "SpaceXec": {
            "category": "Commercial Real Estate",
            "metrics": {
                "website_traffic": 250000,
                "social_followers": 18000,
                "engagement_rate": 2.5
            },
            "insight": "Strong performance in suburban markets"
        }
    }

    # Test performance alerts
    alerts = automation.send_performance_alerts(sample_brands)
    print(f"Alerts sent: {len(alerts)}")

    # Test weekly reports
    report_results = automation.trigger_weekly_report_workflows(sample_brands)
    print(f"Report workflows triggered: {report_results}")
