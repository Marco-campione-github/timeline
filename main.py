import json
import pandas as pd
import plotly.express as px
from datetime import datetime

# Load tasks from JSON file
with open("data.json", "r") as file:
    tasks = json.load(file)

# Convert to DataFrame
df = pd.DataFrame(tasks)

# Convert date strings to datetime objects
df["Start"] = pd.to_datetime(df["Start"])
df["End"] = pd.to_datetime(df["End"])

# Set pixels per task row
pixels_per_row = 30
min_height = 400

# Dynamically set height
height = max(min_height, pixels_per_row * len(df["Name"].unique()))

# Create Gantt chart
fig = px.timeline(
    df,
    x_start="Start",
    x_end="End",
    y="Name",
    color="Name",
    title="Project Timeline (Jul - Oct 2025)",
    hover_data={
        "Start": True,
        "End": True,
        "Name": True  # Already used as y-axis
    }
)

# Adjust appearance
fig.update_yaxes(autorange="reversed")
fig.update_layout(
    xaxis=dict(
        range=[datetime(2025, 7, 1), datetime(2025, 10, 31)],
        tickformat="%B",
        dtick="M1",
        ticklabelmode="period"
    ),
    height=height,
    margin=dict(l=150, r=30, t=60, b=30),
    showlegend=False
)



fig.write_html("docs/index.html")
fig.show()
