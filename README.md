# Unified Brand Management Dashboard

A comprehensive Streamlit-based dashboard for managing multiple brands with real-time social media integration, data tracking, and workflow automation.

## Features

🚀 **Multi-Brand Overview**
- Portfolio-level KPI tracking
- Interactive brand comparison
- Real-time social media metrics

📊 **Individual Brand Deep Dives**  
- Digital footprint analysis
- Operational metrics tracking
- Market trend insights

🔄 **Automated Data Integration**
- Social media API connections (LinkedIn, Instagram, Facebook, TikTok)
- Data-tracker repository sync
- Notion database integration
- Workflow automation (Power Automate, n8n, Make)

## Your Brands
- **SpaceXec**: Commercial Real Estate
- **Aashi Realty**: Residential Brokerage  
- **TravelXec**: Online Travel Services
- **Schmooze Media**: Digital Marketing Agency
- **AutoXec**: Automotive Retail

## Quick Start

1. **Setup Environment**
   ```bash
   ./start_dashboard.sh
   ```

2. **Configure API Keys**
   - Edit `.env` file with your social media API credentials
   - Add Data-tracker repository path
   - Configure workflow webhooks

3. **Run Dashboard**
   ```bash
   streamlit run brand_dashboard_app.py
   ```

4. **Start Automation** (Optional)
   ```bash
   python dashboard_automation.py
   ```

## File Structure

```
├── brand_dashboard_app.py          # Main Streamlit dashboard
├── social_media_connector.py       # Social media API integration
├── data_integration.py             # Data-tracker & Notion integration
├── workflow_automation.py          # Power Automate/n8n/Make workflows  
├── dashboard_automation.py         # Scheduled automation
├── requirements.txt                # Python dependencies
├── .env.template                   # Environment variables template
├── start_dashboard.sh              # Quick setup script
└── data/
    ├── backups/                    # Automated backups
    └── processed/                  # Processed data files
```

## Configuration

### Social Media APIs
- LinkedIn: Company page access
- Instagram: Business account required  
- Facebook: Page access token
- TikTok: Business API access

### Integration Endpoints
- Data-tracker repository path
- Notion database ID and API key
- Workflow automation webhooks

### Automation Schedule
- Social media refresh: Every 6 hours
- Data sync: Daily at 9:00 AM IST  
- Weekly reports: Monday at 10:00 AM IST

## Cost Breakdown (Monthly)
- Zoho Social Professional: ₹1,725
- Additional API calls: ₹500
- Cloud hosting: ₹1,200
- **Total**: ₹6,425/month

## Support

Built for Indian brand management with local integrations including:
- WhatsApp Business API notifications
- Telegram alerts
- IST timezone scheduling
- Cost-optimized for Indian market

---
**Ready to manage your brand portfolio efficiently!** 🚀
