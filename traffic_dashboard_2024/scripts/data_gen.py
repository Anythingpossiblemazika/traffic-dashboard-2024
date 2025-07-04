
import pandas as pd
import numpy as np
import os

os.makedirs("traffic_dashboard_2024/data", exist_ok=True)

# Incident locations
incident_data = {
    "zone": ["Zone A", "Zone B", "Zone C", "Zone A", "Zone B", "Zone C", "Zone A"],
    "lat": [37.77, 37.76, 37.75, 37.77, 37.76, 37.75, 37.77],
    "lon": [-122.42, -122.43, -122.44, -122.42, -122.43, -122.44, -122.42],
    "incident_type": ["Crash", "Jam", "Crash", "Jam", "Crash", "Jam", "Crash"]
}
df_incidents = pd.DataFrame(incident_data)
df_incidents.to_csv("traffic_dashboard_2024/data/incident_locations.csv", index=False)

# Zone speed trends
np.random.seed(42)
dates = pd.date_range("2024-01-01", "2024-01-10")
zone_speed = {
    "date": np.tile(dates, 3),
    "zone": ["Zone A"]*len(dates) + ["Zone B"]*len(dates) + ["Zone C"]*len(dates),
    "avg_speed": np.random.normal(40, 5, len(dates)*3)
}
df_speeds = pd.DataFrame(zone_speed)
df_speeds.to_csv("traffic_dashboard_2024/data/zone_speed_trends.csv", index=False)

# Traffic volume per zone
volume_data = {
    "zone": ["Zone A", "Zone B", "Zone C"],
    "vehicle_count": [1200, 950, 1130],
    "peak_hour": ["8-9 AM", "5-6 PM", "12-1 PM"]
}
df_volume = pd.DataFrame(volume_data)
df_volume.to_csv("traffic_dashboard_2024/data/traffic_volumes.csv", index=False)
