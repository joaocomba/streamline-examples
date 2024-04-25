from vega_datasets import data
import streamlit as st
import altair as alt


cars = data.cars()

x_column = st.selectbox('Select x-axis column', cars.select_dtypes('number').columns)

chart = alt.Chart(cars).mark_point().encode(
    x=x_column,
    y='Displacement')

st.altair_chart(chart, use_container_width=True)