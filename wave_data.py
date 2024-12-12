import yaml
import pandas as pd
from datetime import datetime
import plotly.express as px


# Function to get data from a YAML file
def get_wave_data(file_path):

    with open(file_path, "r") as file:
        data = yaml.safe_load(file)
    surf_data = data["data"]["surf"]

    # Example
    # Timestamp Min Max 0 2024-12-11 00:00:00 (Waist to chest) 2.28068 4.00098 1 2024-12-11 01:00:00 (Waist to chest) 2.24483 3.90108 2 2024-12-11 02:00:00 (Waist to chest) 2.20899 3.83399
    # Convert timestamps to datetime objects directly
    timestamps = [datetime.fromtimestamp(surf["timestamp"]) for surf in surf_data]

    min_values = [surf["surf"]["raw"]["min"] for surf in surf_data]
    max_values = [surf["surf"]["raw"]["max"] for surf in surf_data]
    human_txt = [surf["surf"]["humanRelation"] for surf in surf_data]

    return pd.DataFrame(
        {
            "Timestamp": timestamps,
            "Min": min_values,
            "Max": max_values,
            "Human": human_txt,
        }
    )


def plot_waves(surf_data):
    fig = px.line(
        surf_data, x="Timestamp", y=["Min", "Max"], title="Wave Heights Over Time"
    )

    fig.update_xaxes(
        tickmode="array",
        tickvals=pd.date_range(
            surf_data["Timestamp"].min(), surf_data["Timestamp"].max(), freq="1d"
        ),
        tickformat="%d",
    )

    day_starts = pd.date_range(
        start=surf_data["Timestamp"].min(),
        end=surf_data["Timestamp"].max(),
        freq="D",
    )

    for day in day_starts:
        fig.add_vline(x=day, line_width=2, line_dash="dash", line_color="black")

    return fig
