import streamlit as st
from waves import plot_waves, get_wave_data
from tides import plot_tides, get_tides_data
from utils import get_folders

st.set_page_config(page_title="Your Page Title", layout="wide")

file_options = get_folders()
test_file = st.selectbox("Select Test File:", file_options)

st.markdown("## Waves")

file_selection = f"surfline_data\{test_file}\\"
wave_data = get_wave_data(f"{file_selection}surf.yaml")

plot_waves_fig = plot_waves(wave_data)

st.plotly_chart(plot_waves_fig)

if st.button("Show Waves Data"):
    st.dataframe(wave_data, use_container_width=True)

st.markdown("---")

st.markdown("## Tides")

tides_data = get_tides_data(f"{file_selection}tides.yaml")
plot_tides_fig = plot_tides(tides_data)


st.plotly_chart(plot_tides_fig)

if st.button("Show Tides Data"):
    st.dataframe(tides_data, use_container_width=True)
