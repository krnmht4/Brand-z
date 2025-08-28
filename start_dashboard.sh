#!/bin/bash

# Brand Dashboard Startup Script
echo "🚀 Starting Unified Brand Management Dashboard..."

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install requirements
echo "Installing requirements..."
pip install -r requirements.txt

# Create data directory
mkdir -p data/backups
mkdir -p data/processed

# Copy .env template if .env doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file from template..."
    cp .env.template .env
    echo "⚠️  Please edit .env file with your API keys and configuration"
fi

echo "✅ Setup complete!"
echo ""
echo "To start the dashboard:"
echo "1. Edit .env file with your API keys"
echo "2. Run: streamlit run brand_dashboard_app.py"
echo "3. Run background automation: python dashboard_automation.py"
echo ""
echo "Dashboard will be available at: http://localhost:8501"
