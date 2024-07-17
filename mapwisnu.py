from __future__ import annotations
import folium
import streamlit as st
import pandas as pd 
import requests
from folium.plugins import GroupedLayerControl
import folium.features
import shapely

from streamlit_folium import st_folium

st.set_page_config(
    page_title="Fiber Optic Project By Wisnu",
    page_icon=":earth_asia:",
    layout="wide",
)


st.title("Fiber Optic Project")

m = folium.Map(location=[-6.211156,106.816281], zoom_start=13,tiles="Cartodb Positron")
url = "https://raw.githubusercontent.com/ywisnu/Map/main/Data/merged.json"
url2 = "https://raw.githubusercontent.com/ywisnu/Map/main/Data/RouteR5.geojson"
folium.GeoJson(url).add_to(m)


G2 = folium.GeoJson(url2).add_to(m)

m.add_child(G2)

folium.LayerControl(collapsed=False).add_to(m)



col1, col2 = st.columns(2)
with col1:
    st.markdown("## XL Project")
    st_folium(m,use_container_width=True)
with col2:
    "## Table FO Project"
    df= pd.read_csv("https://raw.githubusercontent.com/ywisnu/portfolio/main/views/project1.csv")
    st.dataframe(df, height=300)
    
    

    

    
    
    


    
    


