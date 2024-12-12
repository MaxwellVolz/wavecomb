import streamlit as st
from wave_data import plot_waves, get_wave_data
import os
from utils import get_folders

st.markdown("## Wave Data")

file_options = get_folders()
test_file = st.selectbox("Select Test File:", file_options)

wave_data = get_wave_data(f"surfline_data\{test_file}\surf.yaml")

plot_waves_fig = plot_waves(wave_data)

st.plotly_chart(plot_waves_fig)

if st.button("Show Dataframe"):
    st.dataframe(wave_data, use_container_width=True)

st.markdown("---")
