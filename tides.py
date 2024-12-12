import yaml
import pandas as pd
from datetime import datetime
import plotly.express as px


# Function to get data from a YAML file
def get_tides_data(file_path):

    with open(file_path, "r") as file:
        data = yaml.safe_load(file)
    tides_data = data["data"]["tides"]

    ts = [datetime.fromtimestamp(tides["timestamp"]) for tides in tides_data]

    height = [tides["height"] for tides in tides_data]
    txt = [tides["type"] for tides in tides_data]

    return pd.DataFrame(
        {
            "Timestamp": ts,
            "height": height,
            "txt": txt,
        }
    )


def plot_tides(data):
    fig = px.line(
        data,
        x="Timestamp",
        y="height",
        title=None,
        labels={"Timestamp": "Day", "height": "ft"},
    )
    fig.update_layout(margin=dict(l=0, r=0, t=0, b=0), showlegend=False)
    fig.update_xaxes(
        tickmode="array",
        tickvals=pd.date_range(
            data["Timestamp"].min(), data["Timestamp"].max(), freq="1d"
        ),
        tickformat="%d",
    )

    day_starts = pd.date_range(
        start=data["Timestamp"].min(),
        end=data["Timestamp"].max(),
        freq="D",
    )

    for day in day_starts:
        fig.add_vline(x=day, line_width=2, line_dash="dash", line_color="black")

    return fig


# data:
#   tides:
#   - height: 1.53
#     timestamp: 1733904000
#     type: NORMAL
#     utcOffset: -8
#   - height: 2.24
#     timestamp: 1733907600
#     type: NORMAL
#     utcOffset: -8
#   - height: 3.25
