import yaml
import plotly.graph_objects as go
from datetime import datetime

test_file = "surfline_data/1733983398/surf.yaml"


# Open and read the YAML file
with open(test_file, "r") as file:
    data = yaml.safe_load(file)

# Extract surf data
surf_data = data["data"]["surf"]

# Example of processing: print each surf entry with its timestamp
for surf in surf_data:
    print(f"Timestamp: {surf['timestamp']}, Surf Data: {surf['surf']}")

timestamps = [
    datetime.fromtimestamp(surf["timestamp"]).strftime("%Y-%m-%d %H:%M:%S")
    + f" ({surf['surf']['humanRelation']})"
    for surf in surf_data
]
min_values = [surf["surf"]["raw"]["min"] for surf in surf_data]
max_values = [surf["surf"]["raw"]["max"] for surf in surf_data]
diff_values = [
    surf["surf"]["raw"]["max"] - surf["surf"]["raw"]["min"] for surf in surf_data
]


fig = go.Figure(
    data=[
        go.Bar(name="Min", x=timestamps, y=min_values),
        go.Bar(name="Max", x=timestamps, y=max_values),
    ]
)
# bar mode to stack
fig.update_layout(
    barmode="stack",
    title="Surf Wave Data",
    xaxis_title="Timestamp and Human Relation",
    yaxis_title="Wave Height (min and max values)",
)

fig.show()

fig2 = go.Figure(
    data=[
        go.Scatter(
            name="Max",
            x=timestamps,
            y=max_values,
            line_color="rgb(22,169,250)",
            mode="lines+markers",
            fill="tozeroy",
            line_shape="spline",
        ),
        go.Scatter(
            name="Min",
            x=timestamps,
            y=min_values,
            line_color="rgb(22,57,250)",
            mode="lines+markers",
            fill="tozeroy",
            line_shape="spline",
        ),
    ]
)

# Update layout for the line chart
fig2.update_layout(
    title="Surf Wave Data",
    xaxis_title="Timestamp and Human Relation",
    yaxis_title="Wave Height (min and max values)",
)


fig2.show()
