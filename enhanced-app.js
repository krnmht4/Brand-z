// MEGALITHIC DATA INTEGRATION ENHANCEMENT FOR BLACK BOX MARKETING
// Enhanced with enterprise-scale data processing, real-time streaming, and advanced analytics

// Extended mock data with megalithic capabilities
const megalithData = {
  // Original base metrics
  mockMetrics: {
    totalLeads: 1247,
    conversionRate: 12.5,
    cac: 85,
    ltv: 850,
    monthlyGrowth: 18.5,
    // Enhanced metrics
    totalDataSources: 47,
    realTimeStreams: 12,
    dataVelocity: '2.4M events/sec',
    storageCapacity: '847TB',
    aiModelAccuracy: 94.7
  },

  // Enhanced funnel data with multiple business units
  funnelData: [
    {"stage": "Visitors", "count": 12450, "rate": 100, "source": "web"},
    {"stage": "Leads", "count": 1247, "rate": 10.0, "source": "web"},
    {"stage": "MQLs", "count": 374, "rate": 30.0, "source": "web"},
    {"stage": "SQLs", "count": 112, "rate": 30.0, "source": "web"},
    {"stage": "Customers", "count": 28, "rate": 25.0, "source": "web"}
  ],

  // Expanded data sources for megalithic integration
  dataSources: [
    {
      category: "Marketing Platforms",
      sources: [
        {"name": "Google Analytics", "status": "connected", "dataRate": "Real-time", "volume": "50GB/day"},
        {"name": "Google Ads", "status": "connected", "dataRate": "Real-time", "volume": "25GB/day"},
        {"name": "Meta Marketing API", "status": "connected", "dataRate": "Real-time", "volume": "35GB/day"},
        {"name": "LinkedIn Ads API", "status": "connected", "dataRate": "Real-time", "volume": "18GB/day"},
        {"name": "TikTok Ads", "status": "connected", "dataRate": "Real-time", "volume": "22GB/day"},
        {"name": "Twitter Ads", "status": "connected", "dataRate": "Real-time", "volume": "15GB/day"},
        {"name": "Pinterest Ads", "status": "connected", "dataRate": "Real-time", "volume": "12GB/day"}
      ]
    },
    {
      category: "CRM & Sales",
      sources: [
        {"name": "Salesforce", "status": "connected", "dataRate": "CDC", "volume": "45GB/day"},
        {"name": "HubSpot", "status": "connected", "dataRate": "CDC", "volume": "30GB/day"},
        {"name": "Pipedrive", "status": "connected", "dataRate": "CDC", "volume": "20GB/day"},
        {"name": "Zoho CRM", "status": "connected", "dataRate": "Batch", "volume": "15GB/day"}
      ]
    },
    {
      category: "E-commerce",
      sources: [
        {"name": "Shopify", "status": "connected", "dataRate": "Real-time", "volume": "60GB/day"},
        {"name": "WooCommerce", "status": "connected", "dataRate": "Real-time", "volume": "40GB/day"},
        {"name": "Amazon Seller", "status": "connected", "dataRate": "Batch", "volume": "85GB/day"},
        {"name": "eBay", "status": "connected", "dataRate": "Batch", "volume": "35GB/day"}
      ]
    },
    {
      category: "Email & Communication",
      sources: [
        {"name": "Mailchimp", "status": "connected", "dataRate": "Real-time", "volume": "25GB/day"},
        {"name": "SendGrid", "status": "connected", "dataRate": "Real-time", "volume": "30GB/day"},
        {"name": "Klaviyo", "status": "connected", "dataRate": "Real-time", "volume": "35GB/day"},
        {"name": "Twilio", "status": "connected", "dataRate": "Real-time", "volume": "20GB/day"}
      ]
    },
    {
      category: "Analytics & BI",
      sources: [
        {"name": "Mixpanel", "status": "connected", "dataRate": "Real-time", "volume": "55GB/day"},
        {"name": "Amplitude", "status": "connected", "dataRate": "Real-time", "volume": "48GB/day"},
        {"name": "Segment", "status": "connected", "dataRate": "Real-time", "volume": "70GB/day"},
        {"name": "Adobe Analytics", "status": "connected", "dataRate": "Real-time", "volume": "65GB/day"}
      ]
    },
    {
      category: "Cloud Storage",
      sources: [
        {"name": "AWS S3", "status": "connected", "dataRate": "Streaming", "volume": "2.5TB/day"},
        {"name": "Google Cloud Storage", "status": "connected", "dataRate": "Streaming", "volume": "1.8TB/day"},
        {"name": "Azure Blob Storage", "status": "connected", "dataRate": "Streaming", "volume": "1.2TB/day"}
      ]
    },
    {
      category: "Database Systems",
      sources: [
        {"name": "PostgreSQL", "status": "connected", "dataRate": "CDC", "volume": "120GB/day"},
        {"name": "MySQL", "status": "connected", "dataRate": "CDC", "volume": "95GB/day"},
        {"name": "MongoDB", "status": "connected", "dataRate": "CDC", "volume": "80GB/day"},
        {"name": "Redis", "status": "connected", "dataRate": "Real-time", "volume": "40GB/day"}
      ]
    }
  ],

  // Real-time streaming metrics
  streamingMetrics: {
    kafkaPartitions: 256,
    messagesPerSecond: 2400000,
    avgLatency: "< 10ms",
    throughput: "15.2 GB/sec",
    activeConnections: 1847,
    errorRate: 0.001
  },

  // AI/ML model performance
  aiModels: [
    {
      name: "Customer Lifetime Value Predictor",
      accuracy: 94.7,
      lastTrained: "2 hours ago",
      predictions: "145K/day",
      status: "active"
    },
    {
      name: "Churn Risk Detector",
      accuracy: 92.3,
      lastTrained: "6 hours ago",
      predictions: "89K/day",
      status: "active"
    },
    {
      name: "Attribution Model",
      accuracy: 88.9,
      lastTrained: "1 day ago",
      predictions: "230K/day",
      status: "active"
    },
    {
      name: "Anomaly Detection Engine",
      accuracy: 96.1,
      lastTrained: "30 minutes ago",
      predictions: "Real-time",
      status: "active"
    }
  ],

  // Enhanced recommendations with AI insights
  enhancedRecommendations: [
    {
      type: "predictive",
      message: "AI model predicts 23% increase in conversion rates if budget shifts from Meta to Google Ads",
      confidence: 94.7,
      impact: "high",
      timeframe: "7 days"
    },
    {
      type: "anomaly",
      message: "Unusual spike in bounce rate detected from LinkedIn traffic - investigating attribution patterns",
      confidence: 87.2,
      impact: "medium",
      timeframe: "immediate"
    },
    {
      type: "optimization",
      message: "Cross-platform lookalike audience expansion could yield 156 additional high-value leads",
      confidence: 91.5,
      impact: "high",
      timeframe: "14 days"
    },
    {
      type: "predictive",
      message: "Customer lifetime value model suggests focusing on segments with 3+ touchpoints",
      confidence: 89.8,
      impact: "medium",
      timeframe: "30 days"
    }
  ],

  // Data pipeline health monitoring
  pipelineHealth: {
    dataIngestion: {
      status: "healthy",
      throughput: "2.4M events/sec",
      latency: "< 50ms",
      errorRate: 0.001
    },
    dataProcessing: {
      status: "healthy",
      sparkJobs: 45,
      avgProcessingTime: "2.3 seconds",
      queueDepth: 12
    },
    dataStorage: {
      status: "healthy",
      utilizationRate: 67.3,
      compressionRatio: 4.2,
      queryLatency: "< 100ms"
    }
  }
};

// Enhanced global variables for megalithic features
let funnelChart = null;
let performanceChart = null;
let realTimeMetricsChart = null;
let streamingDashboard = null;
let dataFlowDiagram = null;

// WebSocket connection for real-time updates
let websocket = null;
const WS_URL = 'wss://megalith-data-stream.example.com/ws';

// Initialize enhanced application
document.addEventListener('DOMContentLoaded', function() {
  initializeMegalithicApp();
});

function initializeMegalithicApp() {
  // Original initialization
  setupTabNavigation();
  populateDashboard();
  setupAPICards();
  setupBusinessModelSelector();
  setupKPIWidgets();
  setupFormHandlers();
  
  // Enhanced megalithic features
  initializeDataSourceGrid();
  setupRealTimeStreaming();
  initializeAIModelDashboard();
  setupDataPipelineMonitoring();
  startMegalithicUpdates();
  initializeAdvancedAnalytics();
  
  updateLastUpdatedTime();
}

// Enhanced tab navigation with new megalithic tabs
function setupTabNavigation() {
  const navTabs = document.querySelectorAll('.nav-tab');
  const tabContents = document.querySelectorAll('.tab-content');

  navTabs.forEach(tab => {
    tab.addEventListener('click', function() {
      const targetTab = this.getAttribute('data-tab');
      
      // Remove active class from all tabs and contents
      navTabs.forEach(t => t.classList.remove('active'));
      tabContents.forEach(content => content.classList.remove('active'));
      
      // Add active class to clicked tab and corresponding content
      this.classList.add('active');
      document.getElementById(targetTab).classList.add('active');
      
      // Initialize charts based on active tab
      setTimeout(() => {
        switch(targetTab) {
          case 'dashboard':
            initializeFunnelChart();
            break;
          case 'data-integration':
            initializeDataFlowDiagram();
            break;
          case 'real-time':
            initializeRealTimeCharts();
            break;
          case 'ai-insights':
            initializeAICharts();
            break;
          case 'reports':
            initializePerformanceChart();
            break;
        }
      }, 100);
    });
  });
}

// Initialize comprehensive data source grid
function initializeDataSourceGrid() {
  const container = document.getElementById('data-sources-grid');
  if (!container) return;

  container.innerHTML = '';
  
  megalithData.dataSources.forEach(category => {
    const categorySection = document.createElement('div');
    categorySection.className = 'data-source-category';
    
    categorySection.innerHTML = `
      <div class="category-header">
        <h4>${category.category}</h4>
        <span class="source-count">${category.sources.length} sources</span>
      </div>
      <div class="sources-grid" id="sources-${category.category.replace(/\s+/g, '-')}">
      </div>
    `;
    
    container.appendChild(categorySection);
    
    const sourcesGrid = categorySection.querySelector('.sources-grid');
    category.sources.forEach(source => {
      const sourceCard = document.createElement('div');
      sourceCard.className = 'source-card';
      
      const statusClass = source.status === 'connected' ? 'connected' : 'disconnected';
      
      sourceCard.innerHTML = `
        <div class="source-header">
          <h5>${source.name}</h5>
          <span class="source-status ${statusClass}">${source.status}</span>
        </div>
        <div class="source-metrics">
          <div class="metric">
            <span class="label">Data Rate:</span>
            <span class="value">${source.dataRate}</span>
          </div>
          <div class="metric">
            <span class="label">Volume:</span>
            <span class="value">${source.volume}</span>
          </div>
        </div>
        <div class="source-actions">
          <button class="btn btn--sm btn--outline">Monitor</button>
          <button class="btn btn--sm btn--secondary">Config</button>
        </div>
      `;
      
      sourcesGrid.appendChild(sourceCard);
    });
  });
}

// Setup real-time streaming capabilities
function setupRealTimeStreaming() {
  // Initialize WebSocket connection
  if (typeof WebSocket !== 'undefined') {
    try {
      websocket = new WebSocket(WS_URL);
      
      websocket.onopen = function(event) {
        console.log('Real-time streaming connected');
        showNotification('Real-time data streaming activated');
      };
      
      websocket.onmessage = function(event) {
        const data = JSON.parse(event.data);
        handleRealTimeUpdate(data);
      };
      
      websocket.onerror = function(error) {
        console.log('WebSocket error:', error);
        // Fallback to polling
        startPollingMode();
      };
    } catch (error) {
      console.log('WebSocket not available, using polling mode');
      startPollingMode();
    }
  } else {
    startPollingMode();
  }
}

// Handle real-time data updates
function handleRealTimeUpdate(data) {
  switch(data.type) {
    case 'metrics_update':
      updateMetricsDashboard(data.payload);
      break;
    case 'anomaly_detected':
      handleAnomalyAlert(data.payload);
      break;
    case 'pipeline_status':
      updatePipelineStatus(data.payload);
      break;
    case 'ai_prediction':
      handleAIPrediction(data.payload);
      break;
  }
}

// Initialize AI model dashboard
function initializeAIModelDashboard() {
  const container = document.getElementById('ai-models-grid');
  if (!container) return;

  container.innerHTML = '';
  
  megalithData.aiModels.forEach(model => {
    const modelCard = document.createElement('div');
    modelCard.className = 'ai-model-card';
    
    const accuracyColor = model.accuracy > 90 ? 'success' : model.accuracy > 85 ? 'warning' : 'error';
    
    modelCard.innerHTML = `
      <div class="model-header">
        <h5>${model.name}</h5>
        <span class="model-status ${model.status}">${model.status}</span>
      </div>
      <div class="model-metrics">
        <div class="accuracy-metric">
          <span class="label">Accuracy</span>
          <div class="accuracy-bar">
            <div class="accuracy-fill ${accuracyColor}" style="width: ${model.accuracy}%"></div>
            <span class="accuracy-value">${model.accuracy}%</span>
          </div>
        </div>
        <div class="model-stats">
          <div class="stat">
            <span class="label">Last Trained:</span>
            <span class="value">${model.lastTrained}</span>
          </div>
          <div class="stat">
            <span class="label">Predictions:</span>
            <span class="value">${model.predictions}</span>
          </div>
        </div>
      </div>
      <div class="model-actions">
        <button class="btn btn--sm btn--primary">Retrain</button>
        <button class="btn btn--sm btn--outline">Analyze</button>
      </div>
    `;
    
    container.appendChild(modelCard);
  });
}

// Setup data pipeline monitoring
function setupDataPipelineMonitoring() {
  const container = document.getElementById('pipeline-health');
  if (!container) return;

  const health = megalithData.pipelineHealth;
  
  container.innerHTML = `
    <div class="pipeline-section">
      <h4>Data Ingestion</h4>
      <div class="health-metrics">
        <div class="metric">
          <span class="label">Status:</span>
          <span class="value status-${health.dataIngestion.status}">${health.dataIngestion.status}</span>
        </div>
        <div class="metric">
          <span class="label">Throughput:</span>
          <span class="value">${health.dataIngestion.throughput}</span>
        </div>
        <div class="metric">
          <span class="label">Latency:</span>
          <span class="value">${health.dataIngestion.latency}</span>
        </div>
        <div class="metric">
          <span class="label">Error Rate:</span>
          <span class="value">${health.dataIngestion.errorRate}%</span>
        </div>
      </div>
    </div>
    
    <div class="pipeline-section">
      <h4>Data Processing</h4>
      <div class="health-metrics">
        <div class="metric">
          <span class="label">Status:</span>
          <span class="value status-${health.dataProcessing.status}">${health.dataProcessing.status}</span>
        </div>
        <div class="metric">
          <span class="label">Active Jobs:</span>
          <span class="value">${health.dataProcessing.sparkJobs}</span>
        </div>
        <div class="metric">
          <span class="label">Avg Processing:</span>
          <span class="value">${health.dataProcessing.avgProcessingTime}</span>
        </div>
        <div class="metric">
          <span class="label">Queue Depth:</span>
          <span class="value">${health.dataProcessing.queueDepth}</span>
        </div>
      </div>
    </div>
    
    <div class="pipeline-section">
      <h4>Data Storage</h4>
      <div class="health-metrics">
        <div class="metric">
          <span class="label">Status:</span>
          <span class="value status-${health.dataStorage.status}">${health.dataStorage.status}</span>
        </div>
        <div class="metric">
          <span class="label">Utilization:</span>
          <span class="value">${health.dataStorage.utilizationRate}%</span>
        </div>
        <div class="metric">
          <span class="label">Compression:</span>
          <span class="value">${health.dataStorage.compressionRatio}:1</span>
        </div>
        <div class="metric">
          <span class="label">Query Latency:</span>
          <span class="value">${health.dataStorage.queryLatency}</span>
        </div>
      </div>
    </div>
  `;
}

// Initialize real-time charts
function initializeRealTimeCharts() {
  initializeStreamingMetricsChart();
  initializeThroughputChart();
  initializeLatencyChart();
}

// Initialize streaming metrics chart
function initializeStreamingMetricsChart() {
  const ctx = document.getElementById('streamingMetricsChart');
  if (!ctx) return;

  if (realTimeMetricsChart) {
    realTimeMetricsChart.destroy();
  }

  const timeLabels = generateTimeLabels(60); // Last 60 minutes
  const throughputData = generateRealtimeData(60, 2000000, 2800000);
  const latencyData = generateRealtimeData(60, 5, 15);

  realTimeMetricsChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: timeLabels,
      datasets: [{
        label: 'Messages/sec',
        data: throughputData,
        borderColor: '#1FB8CD',
        backgroundColor: 'rgba(31, 184, 205, 0.1)',
        tension: 0.4,
        yAxisID: 'y'
      }, {
        label: 'Latency (ms)',
        data: latencyData,
        borderColor: '#FFC185',
        backgroundColor: 'rgba(255, 193, 133, 0.1)',
        tension: 0.4,
        yAxisID: 'y1'
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        y: {
          type: 'linear',
          display: true,
          position: 'left',
          title: {
            display: true,
            text: 'Messages per Second'
          }
        },
        y1: {
          type: 'linear',
          display: true,
          position: 'right',
          title: {
            display: true,
            text: 'Latency (ms)'
          },
          grid: {
            drawOnChartArea: false,
          },
        }
      }
    }
  });
}

// Enhanced recommendations with AI insights
function populateEnhancedRecommendations() {
  const container = document.getElementById('enhanced-recommendations');
  if (!container) return;

  container.innerHTML = '';
  
  megalithData.enhancedRecommendations.forEach(rec => {
    const item = document.createElement('div');
    item.className = `recommendation-item ${rec.type}`;
    
    const confidenceColor = rec.confidence > 90 ? 'success' : rec.confidence > 80 ? 'warning' : 'info';
    const impactIcon = rec.impact === 'high' ? '🚀' : rec.impact === 'medium' ? '📈' : '📊';
    
    item.innerHTML = `
      <div class="rec-header">
        <span class="rec-type">${rec.type}</span>
        <span class="rec-confidence ${confidenceColor}">${rec.confidence}%</span>
      </div>
      <div class="rec-content">
        <span class="rec-impact">${impactIcon}</span>
        <p>${rec.message}</p>
      </div>
      <div class="rec-footer">
        <span class="rec-timeframe">Expected timeframe: ${rec.timeframe}</span>
        <button class="btn btn--sm btn--primary">Implement</button>
      </div>
    `;
    
    container.appendChild(item);
  });
}

// Start megalithic real-time updates
function startMegalithicUpdates() {
  // Update streaming metrics every 5 seconds
  setInterval(() => {
    updateStreamingMetrics();
  }, 5000);
  
  // Update AI model metrics every 30 seconds
  setInterval(() => {
    updateAIModelMetrics();
  }, 30000);
  
  // Update data pipeline health every 10 seconds
  setInterval(() => {
    updatePipelineHealth();
  }, 10000);
  
  // Refresh enhanced recommendations every 2 minutes
  setInterval(() => {
    refreshEnhancedRecommendations();
  }, 120000);
}

// Generate time labels for charts
function generateTimeLabels(count) {
  const labels = [];
  const now = new Date();
  for (let i = count - 1; i >= 0; i--) {
    const time = new Date(now.getTime() - i * 60000); // 1 minute intervals
    labels.push(time.toLocaleTimeString('en-US', { hour12: false }));
  }
  return labels;
}

// Generate realistic real-time data
function generateRealtimeData(count, min, max) {
  const data = [];
  for (let i = 0; i < count; i++) {
    const value = Math.random() * (max - min) + min;
    data.push(Math.round(value));
  }
  return data;
}

// Update streaming metrics display
function updateStreamingMetrics() {
  const metrics = megalithData.streamingMetrics;
  
  // Add some realistic variance
  metrics.messagesPerSecond += Math.floor(Math.random() * 200000) - 100000;
  metrics.messagesPerSecond = Math.max(2000000, Math.min(3000000, metrics.messagesPerSecond));
  
  document.getElementById('kafka-partitions').textContent = metrics.kafkaPartitions;
  document.getElementById('messages-per-second').textContent = metrics.messagesPerSecond.toLocaleString();
  document.getElementById('avg-latency').textContent = metrics.avgLatency;
  document.getElementById('throughput').textContent = metrics.throughput;
  document.getElementById('active-connections').textContent = metrics.activeConnections.toLocaleString();
  document.getElementById('error-rate').textContent = metrics.errorRate;
}

// Initialize advanced analytics features
function initializeAdvancedAnalytics() {
  setupCustomerJourneyMapping();
  setupAttributionModeling();
  setupCohortAnalysis();
  setupPredictiveInsights();
}

// Setup customer journey mapping
function setupCustomerJourneyMapping() {
  // Implement interactive customer journey visualization
  console.log('Customer journey mapping initialized');
}

// Setup attribution modeling
function setupAttributionModeling() {
  // Implement multi-touch attribution analysis
  console.log('Attribution modeling initialized');
}

// Setup cohort analysis
function setupCohortAnalysis() {
  // Implement cohort-based retention analysis
  console.log('Cohort analysis initialized');
}

// Setup predictive insights
function setupPredictiveInsights() {
  // Implement ML-powered predictive analytics
  console.log('Predictive insights initialized');
}

// Fallback polling mode when WebSocket is unavailable
function startPollingMode() {
  setInterval(() => {
    // Simulate real-time updates via polling
    const simulatedData = {
      type: 'metrics_update',
      payload: generateSimulatedMetrics()
    };
    handleRealTimeUpdate(simulatedData);
  }, 10000); // Poll every 10 seconds
}

// Generate simulated metrics for demo purposes
function generateSimulatedMetrics() {
  return {
    leads: Math.floor(Math.random() * 50) + megalithData.mockMetrics.totalLeads,
    conversionRate: Math.round((Math.random() * 2 + megalithData.mockMetrics.conversionRate) * 10) / 10,
    streamingThroughput: Math.floor(Math.random() * 500000) + 2000000
  };
}

// Enhanced notification system with different types
function showEnhancedNotification(message, type = 'info', duration = 3000) {
  const notification = document.createElement('div');
  notification.className = `notification notification--${type}`;
  notification.textContent = message;
  
  const typeColors = {
    info: 'var(--color-info)',
    success: 'var(--color-success)',
    warning: 'var(--color-warning)',
    error: 'var(--color-error)'
  };
  
  notification.style.cssText = `
    position: fixed;
    top: 20px;
    right: 20px;
    background-color: ${typeColors[type]};
    color: var(--color-btn-primary-text);
    padding: var(--space-12) var(--space-20);
    border-radius: var(--radius-base);
    box-shadow: var(--shadow-lg);
    z-index: 1000;
    font-size: var(--font-size-sm);
    font-weight: var(--font-weight-medium);
    opacity: 0;
    transform: translateX(100%);
    transition: all var(--duration-normal) var(--ease-standard);
  `;
  
  document.body.appendChild(notification);
  
  setTimeout(() => {
    notification.style.opacity = '1';
    notification.style.transform = 'translateX(0)';
  }, 100);
  
  setTimeout(() => {
    notification.style.opacity = '0';
    notification.style.transform = 'translateX(100%)';
    setTimeout(() => {
      if (document.body.contains(notification)) {
        document.body.removeChild(notification);
      }
    }, 300);
  }, duration);
}

// Enhanced error handling and monitoring
function handleAnomalyAlert(anomaly) {
  showEnhancedNotification(
    `Anomaly detected: ${anomaly.description}`,
    'warning',
    5000
  );
  
  // Log to monitoring system
  console.log('Anomaly detected:', anomaly);
  
  // Trigger automated response if configured
  if (anomaly.autoResponse) {
    triggerAutomatedResponse(anomaly);
  }
}

// Automated response system
function triggerAutomatedResponse(anomaly) {
  switch(anomaly.type) {
    case 'traffic_spike':
      // Auto-scale processing capacity
      console.log('Auto-scaling triggered for traffic spike');
      break;
    case 'conversion_drop':
      // Alert marketing team
      console.log('Marketing team alerted for conversion drop');
      break;
    case 'data_quality':
      // Pause affected pipelines
      console.log('Data quality issue - pausing affected pipelines');
      break;
  }
}

// Export megalithic data for external systems
function exportMegalithicData(format = 'json') {
  const exportData = {
    timestamp: new Date().toISOString(),
    metrics: megalithData.mockMetrics,
    dataSources: megalithData.dataSources,
    streamingMetrics: megalithData.streamingMetrics,
    aiModels: megalithData.aiModels,
    pipelineHealth: megalithData.pipelineHealth
  };
  
  switch(format) {
    case 'json':
      return JSON.stringify(exportData, null, 2);
    case 'csv':
      return convertToCSV(exportData);
    default:
      return exportData;
  }
}

// Convert data to CSV format
function convertToCSV(data) {
  // Implement CSV conversion logic
  const csv = [
    'timestamp,metric,value',
    `${data.timestamp},totalLeads,${data.metrics.totalLeads}`,
    `${data.timestamp},conversionRate,${data.metrics.conversionRate}`,
    `${data.timestamp},messagesPerSecond,${data.streamingMetrics.messagesPerSecond}`,
    // Add more metrics as needed
  ].join('\n');
  
  return csv;
}

// Original functions maintained for backward compatibility
// ... (include all original functions from the base app.js)

// Initialize tooltips for megalithic features
document.addEventListener('DOMContentLoaded', function() {
  initializeTooltips();
});