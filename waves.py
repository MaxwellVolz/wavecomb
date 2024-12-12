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

plot_waves_fig = plot_waves(surf_data)


st.plotly_chart(plot_waves_fig)
