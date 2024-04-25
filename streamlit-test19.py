import folium
import streamlit as st

from streamlit_folium import st_folium

# center on Liberty Bell, add marker
m = folium.Map(location=[-30.03, -51.2], zoom_start=16)
folium.Marker(
    [-30.03, -51.2], popup="Porto Alegre", tooltip="Porto Alegre"
).add_to(m)

# call to render Folium map in Streamlit, but don't get any data back
# from the map (so that it won't rerun the app when the user interacts)
st_folium(m, width=725, returned_objects=[])