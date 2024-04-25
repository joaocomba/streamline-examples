#Plot a map
import streamlit as st
import numpy as np
import pandas as pd

map_data = pd.DataFrame(
 # San Francisco Lat Long
 #   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], 
 # Porto Alegre Lat Long
    np.random.randn(1000, 2) / [50, 50] + [-30.03, -51.2],
    columns=['lat', 'lon'])

st.map(map_data)