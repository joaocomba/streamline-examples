import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

# Importing the Vega Dataset
from vega_datasets import data as vega_data

movies_df = pd.read_json(vega_data.movies.url)

def extract_year(value):
    return pd.to_datetime(value, format='%b %d %Y').year

movies_df["Year"] = movies_df["Release_Date"].apply(extract_year)

select_year = alt.selection_single(
    name='Select', fields=['Year'], init={'Year': 1928},
    bind=alt.binding_range(min=1968, max=2008, step=1)
)

mychart = alt.Chart(movies_df).mark_point(filled=True).encode(
    alt.X('Production_Budget'),
    alt.Y('Worldwide_Gross'),
    alt.Size('US_Gross'),
    alt.Color('Major_Genre'),
    alt.OpacityValue(0.7),
    tooltip = [alt.Tooltip('Title:N'),
               alt.Tooltip('Production_Budget:Q'),
               alt.Tooltip('Worldwide_Gross:Q'),
               alt.Tooltip('US_Gross:Q')
              ]
).add_selection(select_year).transform_filter(select_year)


st.altair_chart(mychart, use_container_width=True)