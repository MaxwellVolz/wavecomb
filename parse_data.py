import yaml
import pandas as pd
from datetime import datetime


# Function to get data from a YAML file
def get_data(file_path):
    with open(file_path, "r") as file:
        data = yaml.safe_load(file)
    surf_data = data["data"]["surf"]

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


# Now you can use this function to load and handle data effectively.


def plot_waves():

    return
