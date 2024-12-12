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

    print(f"{tides_data}")
    height = [tides["height"] for tides in tides_data]
    txt = [tides["type"] for tides in tides_data]

    return pd.DataFrame(
        {
            "Timestamp": ts,
            "height": height,
            "txt": txt,
        }
    )


def plot_tides():
    "no"


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
