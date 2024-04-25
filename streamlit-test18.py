from vega_datasets import data
import streamlit as st
import altair as alt
import pandas as pd


import altair as alt
from vega_datasets import data

# Importing the Vega Dataset
from vega_datasets import data as vega_data

movies_df = pd.read_json(vega_data.movies.url)

def extract_year(value):
    return pd.to_datetime(value, format='%b %d %Y').year

movies_df["Year"] = movies_df["Release_Date"].apply(extract_year)

select_year = alt.selection_single(
    name='Select', fields=['Year'], init={'Year': 1968},
    bind=alt.binding_range(min=1968, max=2008, step=1)
)

#x_column = st.selectbox('Select x-axis column', movies_df.select_dtypes('number').columns)
y_column = st.selectbox('Select y-axis column', movies_df.select_dtypes('number').columns)

chart = alt.Chart(movies_df).mark_point(filled=True).encode(
    x = 'Production_Budget',
 #   y = 'Worldwide_Gross',
    y = y_column,
    size = alt.Size('US_Gross'),
    color = alt.Color('Major_Genre'),
    opacity = alt.OpacityValue(0.7),
    tooltip = [alt.Tooltip('Title:N'),
               alt.Tooltip('Production_Budget:Q'),
               alt.Tooltip('Worldwide_Gross:Q'),
               alt.Tooltip('US_Gross:Q'),
               alt.Tooltip('US_DVD_Sales:Q'),
               alt.Tooltip('Running_Time_min:Q'),
               alt.Tooltip('Rotten_Tomatoes_Rating:Q'),
               alt.Tooltip('IMDB_Rating:Q'),
               alt.Tooltip('IMDB_Votes:Q'),
               alt.Tooltip('US_DVD_Sales:Q')
              ]
).add_selection(select_year).transform_filter(select_year)

st.altair_chart(chart, use_container_width=True)
