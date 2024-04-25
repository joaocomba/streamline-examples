import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

# Importing the Vega Dataset
from vega_datasets import data as vega_data

gm_df = vega_data.gapminder()

select_year = alt.selection_single(
 name='Select', fields=['year'], init={'year': 1955},
 bind=alt.binding_range(min=1955, max=2005, step=5)
)
scatter_plot = alt.Chart(gm_df).mark_point(filled=True).encode(
 alt.X('life_expect'),
 alt.Y('fertility'),
 alt.Size('pop'),
 alt.Color('country'),
 alt.OpacityValue(0.7),
 tooltip = [alt.Tooltip('country'),
 alt.Tooltip('fertility'),
 alt.Tooltip('life_expect'),
 alt.Tooltip('pop'),
 alt.Tooltip('year')]
).properties(
 width=500,
 height=500,
 title='Relationship between fertility and life expectancy for various countries by year'
).add_selection(select_year).transform_filter(select_year).interactive()
scatter_plot.configure_title(
 fontSize=16,
 font='Arial',
 anchor='middle',
 color='gray')


st.altair_chart(scatter_plot, use_container_width=True)