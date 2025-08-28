import plotly.graph_objects as go
import plotly.io as pio
import json

# Create the figure
fig = go.Figure()

# Define positions for nodes (x, y coordinates) - better layout
node_positions = {
    # Social Media APIs (separate nodes)
    "LinkedIn": (0, 5),
    "Instagram": (0, 4),
    "Facebook": (0, 3),
    "TikTok": (0, 2),
    # Processing layer
    "Social Media Connector": (2, 3.5),
    "Data Integration": (4, 3.5),
    # Storage layer
    "Data-tracker Repo": (6, 4.5),
    "Notion Database": (6, 2.5),
    # Interface layer
    "Streamlit Dashboard": (8, 3.5),
    # Output layer
    "Workflow Automation": (10, 3.5),
    # Controller
    "Automation Scheduler": (5, 1)
}

# Define colors for different component types
colors = {
    "social_api": "#1FB8CD",      # Strong cyan
    "processor": "#DB4545",        # Bright red
    "storage": "#2E8B57",          # Sea green
    "interface": "#5D878F",        # Cyan
    "automation": "#D2BA4C",       # Moderate yellow
    "controller": "#B4413C"        # Moderate red
}

# Define node details with exact terminology
node_details = {
    "LinkedIn": {"type": "social_api", "size": 50},
    "Instagram": {"type": "social_api", "size": 50},
    "Facebook": {"type": "social_api", "size": 50},
    "TikTok": {"type": "social_api", "size": 50},
    "Social Media Connector": {"type": "processor", "size": 70},
    "Data Integration": {"type": "processor", "size": 70},
    "Data-tracker Repo": {"type": "storage", "size": 65},
    "Notion Database": {"type": "storage", "size": 65},
    "Streamlit Dashboard": {"type": "interface", "size": 70},
    "Workflow Automation": {"type": "automation", "size": 70},
    "Automation Scheduler": {"type": "controller", "size": 70}
}

# Add connections with better routing
connections = [
    ("LinkedIn", "Social Media Connector"),
    ("Instagram", "Social Media Connector"),
    ("Facebook", "Social Media Connector"),
    ("TikTok", "Social Media Connector"),
    ("Social Media Connector", "Data Integration"),
    ("Data Integration", "Data-tracker Repo"),
    ("Data Integration", "Notion Database"),
    ("Data Integration", "Streamlit Dashboard"),
    ("Streamlit Dashboard", "Workflow Automation"),
    ("Automation Scheduler", "Social Media Connector"),
    ("Automation Scheduler", "Data Integration"),
    ("Automation Scheduler", "Streamlit Dashboard")
]

# Add edges first (so they appear behind nodes)
for start, end in connections:
    x0, y0 = node_positions[start]
    x1, y1 = node_positions[end]
    
    # Add line
    fig.add_trace(go.Scatter(
        x=[x0, x1],
        y=[y0, y1],
        mode='lines',
        line=dict(color='#13343B', width=2),
        showlegend=False,
        hoverinfo='skip'
    ))
    
    # Add arrowhead
    # Calculate arrow position slightly before the target node
    arrow_offset = 0.3
    dx = x1 - x0
    dy = y1 - y0
    length = (dx**2 + dy**2)**0.5
    if length > 0:
        unit_x = dx / length
        unit_y = dy / length
        arrow_x = x1 - arrow_offset * unit_x
        arrow_y = y1 - arrow_offset * unit_y
        
        fig.add_annotation(
            x=arrow_x, y=arrow_y,
            ax=x0, ay=y0,
            xref='x', yref='y',
            axref='x', ayref='y',
            arrowhead=2,
            arrowsize=1.2,
            arrowwidth=2,
            arrowcolor='#13343B',
            showarrow=True
        )

# Add nodes with improved styling
type_names = {
    "social_api": "Social APIs",
    "processor": "Processors", 
    "storage": "Storage",
    "interface": "Interface",
    "automation": "Automation",
    "controller": "Controller"
}

legend_added = set()

for node, pos in node_positions.items():
    x, y = pos
    node_type = node_details[node]["type"]
    node_size = node_details[node]["size"]
    
    # Create abbreviated text for display
    display_text = node.replace("Social Media ", "SM ").replace("Automation ", "Auto ")
    if len(display_text) > 15:
        display_text = display_text[:12] + "..."
    
    show_legend = node_type not in legend_added
    if show_legend:
        legend_added.add(node_type)
    
    fig.add_trace(go.Scatter(
        x=[x],
        y=[y],
        mode='markers+text',
        marker=dict(
            size=node_size,
            color=colors[node_type],
            line=dict(color='#13343B', width=1)
        ),
        text=display_text,
        textposition='middle center',
        textfont=dict(size=8, color='white', family='Arial Black'),
        name=type_names[node_type],
        showlegend=show_legend,
        hovertext=f"{node}<br>Type: {type_names[node_type]}",
        hoverinfo='text'
    ))

# Update layout
fig.update_layout(
    title="Brand Dashboard System Architecture",
    xaxis=dict(
        showgrid=False, 
        zeroline=False, 
        showticklabels=False,
        range=[-0.5, 10.5]
    ),
    yaxis=dict(
        showgrid=False, 
        zeroline=False, 
        showticklabels=False,
        range=[0.5, 5.5]
    ),
    showlegend=True,
    legend=dict(
        orientation='h', 
        yanchor='bottom', 
        y=-0.1, 
        xanchor='center', 
        x=0.5,
        bgcolor='rgba(255,255,255,0.8)'
    ),
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)'
)

fig.update_traces(cliponaxis=False)

# Save the chart
fig.write_image("brand_dashboard_architecture.png")