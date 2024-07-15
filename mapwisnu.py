import folium
import streamlit as st
from folium.plugins import GroupedLayerControl
from folium.plugins import Draw
from streamlit_folium import st_folium

st.set_page_config(
    page_title="Fiber Optic Project",
    page_icon=":earth_asia:",
    layout="wide",
)

    m = folium.Map(location=[-6.211156,106.816281], zoom_start=13,tiles="Cartodb Positron")
    Draw(export=True).add_to(m)
    
    url = "https://raw.githubusercontent.com/ywisnu/Map/main/Data/merged.json"
    folium.GeoJson(url).add_to(m)

    folium.Marker(
    location=[-6.230830556,106.7775056],
    popup=folium.Popup("PAG KEBAYORAN LAMA JAW-JK-KYB-1231", parse_html=True, max_width=100),
    ).add_to(m)

    folium.Marker(
    location=[-6.244827778,106.8261472],
    popup=folium.Popup("HUT Mampang JAW-JK-KYB-1692", parse_html=True, max_width=100),
    ).add_to(m)

st_folium(m)

        
