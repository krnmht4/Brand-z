import plotly.graph_objects as go

# Load the data
data = {"timeline": [{"process": "Social Media Refresh", "frequency": "every 6 hours", "intervals": [0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168]}, {"process": "Daily Data Sync", "frequency": "daily at 9 AM IST", "intervals": [9, 33, 57, 81, 105, 129, 153]}, {"process": "Weekly Reports", "frequency": "Monday 10 AM IST", "intervals": [10]}, {"process": "Backup Creation", "frequency": "with daily sync", "intervals": [9, 33, 57, 81, 105, 129, 153]}]}

# Brand colors
colors = ['#1FB8CD', '#DB4545', '#2E8B57', '#5D878F']

# Process abbreviations to fit 15 char limit
process_names = ["Social Media", "Daily Sync", "Weekly Report", "Backup"]

fig = go.Figure()

# Create traces for each process with proper Y positioning
for i, item in enumerate(data['timeline']):
    intervals = item['intervals']
    process_name = process_names[i]
    
    # Create bars for each time interval
    fig.add_trace(go.Bar(
        x=[1.5] * len(intervals),  # Duration of each task (1.5 hours for visibility)
        y=[process_name] * len(intervals),
        base=intervals,  # Start time for each bar
        orientation='h',
        marker_color=colors[i],
        name=process_name,
        hovertemplate=f'{item["process"]}<br>Start: Hour %{{base}}<br>Duration: 1.5 hrs<extra></extra>',
        showlegend=True
    ))

# Update layout
fig.update_layout(
    title="Brand Dashboard Schedule",
    xaxis_title="Hour of Week",
    yaxis_title="Process",
    barmode='overlay'
)

# Update legend to be horizontal and centered
fig.update_layout(legend=dict(orientation='h', yanchor='bottom', y=1.05, xanchor='center', x=0.5))

# Update x-axis to show full week (0-168 hours) with day markers
fig.update_xaxes(range=[0, 168], dtick=24)

# Ensure proper Y-axis ordering
fig.update_yaxes(categoryorder='array', categoryarray=process_names[::-1])  # Reverse order for better visual flow

# Update traces
fig.update_traces(cliponaxis=False)

# Save the chart
fig.write_image("dashboard_timeline.png")