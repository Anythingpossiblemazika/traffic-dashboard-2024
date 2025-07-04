
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# Read CSVs
incidents = pd.read_csv("traffic_dashboard_2024/data/incident_locations.csv")
speeds = pd.read_csv("traffic_dashboard_2024/data/zone_speed_trends.csv")
volumes = pd.read_csv("traffic_dashboard_2024/data/traffic_volumes.csv")

# Incident map
map_fig = px.scatter_mapbox(
    incidents,
    lat="lat",
    lon="lon",
    color="incident_type",
    hover_name="zone",
    zoom=12,
    mapbox_style="open-street-map",
    title="📍 Traffic Incidents by Zone"
)

# Speed trends line chart
line_fig = px.line(
    speeds,
    x="date",
    y="avg_speed",
    color="zone",
    title="📉 Average Speed Trends by Zone"
)

# Traffic volume bar chart
bar_fig = px.bar(
    volumes,
    x="zone",
    y="vehicle_count",
    color="peak_hour",
    title="🚗 Vehicle Count per Zone"
)

# Dashboard layout
from plotly.subplots import make_subplots
from plotly.graph_objs import Figure

fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=("Traffic Incidents Map", "Average Speed Trends", "Vehicle Volume"),
    specs=[[{"type": "mapbox"}, {"type": "xy"}],
           [{"colspan": 2, "type": "xy"}, None]]
)

fig.add_trace(map_fig.data[0], row=1, col=1)
for d in line_fig.data:
    fig.add_trace(d, row=1, col=2)
for d in bar_fig.data:
    fig.add_trace(d, row=2, col=1)

fig.update_layout(
    height=800,
    title_text="🧭 Traffic Monitoring Dashboard",
    mapbox_style="open-street-map",
    margin={"r":10,"t":30,"l":10,"b":10},
    showlegend=True
)

os.makedirs("traffic_dashboard_2024/outputs", exist_ok=True)

fig.write_html("traffic_dashboard_2024/outputs/dashboard.html")
fig.write_image("traffic_dashboard_2024/outputs/screenshot.png")

print("✅ Dashboard HTML and screenshot saved!")
