import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

df = pd.DataFrame({
    'name': ['brian', 'dominik', 'patricia'],
    'age': [20, 30, 40],
    'salary': [100, 200, 300]
})

a = alt.Chart(df).mark_area(opacity=1).encode(
    x='name', y='age')

b = alt.Chart(df).mark_area(opacity=0.6).encode(
    x='name', y='salary')

c = alt.layer(a, b)

st.altair_chart(c, use_container_width=True)