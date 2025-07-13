import json
import pandas as pd
import plotly.express as px
from datetime import datetime

# Optional: Define colors per task
color_map = {
    "Design Phase": "blue",
    "Development Phase": "green",
    "Testing": "orange",
    "Deployment": "red",
    "Linh": "white"
}

# Load tasks from JSON file
with open("data.json", "r") as file:
    tasks = json.load(file)

# Convert to DataFrame
df = pd.DataFrame(tasks)

# Convert date strings to datetime objects
df["Start"] = pd.to_datetime(df["Start"])
df["End"] = pd.to_datetime(df["End"])

# Create Gantt chart
fig = px.timeline(
    df,
    x_start="Start",
    x_end="End",
    y="Name",
    color="Name",
    color_discrete_map=color_map,
    title="Project Timeline (Jul - Oct 2025)"
)

# Adjust appearance
fig.update_yaxes(autorange="reversed")
fig.update_layout(
    xaxis=dict(
        range=[datetime(2025, 7, 1), datetime(2025, 10, 31)],
        tickformat="%b %Y",
        ticklabelmode="period",
        dtick="M1"
    ),
    height=400,
    margin=dict(l=150, r=30, t=60, b=30),
    showlegend=False
)

fig.show()
