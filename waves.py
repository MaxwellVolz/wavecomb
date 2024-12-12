import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from parse_data import plot_waves, get_data
import datetime

st.title("Wave Data")

test_file = "surfline_data/1733983398/surf.yaml"

surf_data = get_data(test_file)

# Example
# Timestamp Min Max 0 2024-12-11 00:00:00 (Waist to chest) 2.28068 4.00098 1 2024-12-11 01:00:00 (Waist to chest) 2.24483 3.90108 2 2024-12-11 02:00:00 (Waist to chest) 2.20899 3.83399

st.dataframe(surf_data, use_container_width=True)

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


st.plotly_chart(fig)
