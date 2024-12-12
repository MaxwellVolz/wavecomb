import yaml
import plotly.graph_objects as go
from datetime import datetime

test_file = "surfline_data/1733983398/surf.yaml"


# file format:
#
# associated:
# ...
# data:
#   surf:
#   - surf:
#       humanRelation: Waist to chest
#       max: 4
#       min: 3
#       plus: false
#       raw:
#         max: 4.00098
#         min: 2.28068
#     timestamp: 1733904000
#     utcOffset: -8
#   - surf:
#       humanRelation: Waist to chest
#       max: 4
#       min: 3
#       plus: false
#       raw:
#         max: 3.90108
#         min: 2.24483
#     timestamp: 1733907600
#     utcOffset: -8


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
min_values = [surf["surf"]["min"] for surf in surf_data]
# max_values = [surf["surf"]["max"] for surf in surf_data]
max_values = [surf["surf"]["max"] - surf["surf"]["min"] for surf in surf_data]

fig = go.Figure(
    data=[
        go.Bar(name="Min", x=timestamps, y=min_values),
        go.Bar(name="Max", x=timestamps, y=max_values),
    ]
)

# Change the bar mode to stack
fig.update_layout(
    barmode="stack",
    title="Surf Wave Data",
    xaxis_title="Timestamp and Human Relation",
    yaxis_title="Wave Height (min and max values)",
)

fig.show()
