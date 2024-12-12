import streamlit as st
from wave_data import plot_waves, get_wave_data
from tides import plot_tides, get_tides_data
import os
from utils import get_folders

st.markdown("## Wave Data")

file_options = get_folders()
test_file = st.selectbox("Select Test File:", file_options)

file_selection = f"surfline_data\{test_file}\\"
wave_data = get_wave_data(f"{file_selection}surf.yaml")

plot_waves_fig = plot_waves(wave_data)

st.plotly_chart(plot_waves_fig)

if st.button("Show Dataframe"):
    st.dataframe(wave_data, use_container_width=True)

st.markdown("---")

st.markdown("## Tides Data")

tides_data = get_tides_data(f"{file_selection}tides.yaml")

st.dataframe(tides_data, use_container_width=True)
