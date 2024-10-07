from __future__ import annotations
import folium
import streamlit as st
import pandas as pd 
import requests
from folium.plugins import GroupedLayerControl
import folium.features
import shapely
from streamlit_folium import st_folium #Widget de Streamlit para mostrar los mapas
from folium.plugins import MarkerCluster #Plugin para agrupar marcadores

from streamlit_folium import st_folium

st.set_page_config(
    page_title="Fiber Optic Project By Wisnu",
    page_icon=":earth_asia:",
    layout="wide",
)
st.header('Fiber Optic Project')

m= folium.Map(location=[-6.211156,106.816281], zoom_start=13,tiles="Cartodb Positron")
url= "https://raw.githubusercontent.com/ywisnu/Map/main/Data/merged.json"
url2= "https://raw.githubusercontent.com/ywisnu/Map/main/Data/RouteR5.geojson"
folium.GeoJson(url).add_to(m)

G2 = folium.GeoJson(url2).add_to(m)

m.add_child(G2)

folium.LayerControl(collapsed=False).add_to(m)
macro = MacroElement()
folium.Marker(location=[-6.230830556,106.7775056],
    popup=folium.Popup("PAG KEBAYORAN LAMA JAW-JK-KYB-1231 T1C1-T1C4", parse_html=True, max_width=100),
    icon=folium.Icon(color="red"),
    ).add_to(m)

folium.Marker(
    location=[-6.244827778,106.8261472],
    popup=folium.Popup("PAG Mampang JAW-JK-KYB-1692 T1C1-T1C4", parse_html=True, max_width=100),
    icon=folium.Icon(color="red"),
    ).add_to(m)

folium.Marker(
    location=[-6.253739,106.807],
    popup=folium.Popup("BRAWIJAYA IV PULO T1C1-T1C4", parse_html=True, max_width=100),
    ).add_to(m)

folium.Marker(
    location=[-6.253055556,106.8048056],
    popup=folium.Popup("3G_DHARMAWGS T2C1-T2C4", parse_html=True, max_width=100),
    ).add_to(m)

folium.Marker(
    location=[-6.252492,106.804353],
    popup=folium.Popup("RESIDENCEATDHRMAWANSA T1C1-T1C4", parse_html=True, max_width=100),
    ).add_to(m)

folium.Marker(
    location=[-6.249780556,106.808],
    popup=folium.Popup("KEMANG PRAPANCA T2C1-T2C4", parse_html=True, max_width=100),
    ).add_to(m)

folium.Marker(
    location=[-6.26246557814017,106.812135134260998],
    popup=folium.Popup("KEMANG VILLAGE2 T1C1-T1C4", parse_html=True, max_width=100),
    ).add_to(m)

folium.Marker(
    location=[-6.262661111,106.8151306],
    popup=folium.Popup("Kemang6 T2C1-T2C4", parse_html=True, max_width=100),
    ).add_to(m)

folium.Marker(
    location=[-6.253169,106.820561],
    popup=folium.Popup("BANGKA 9 T1C1-T1C4", parse_html=True, max_width=100),
    ).add_to(m)

folium.Marker(
    location=[-6.250972222,106.8253611],
    popup=folium.Popup("Mampang Prapatan T1C1-T1C4", parse_html=True, max_width=100),
    ).add_to(m)

col1, col2 = st.columns(2)
with col1:
    st.markdown("Python by Wisnu")
    st_folium(m,use_container_width=True, width=900, height=500
    )
with col2:
    "## Table FO Project"
    df= pd.read_csv("https://raw.githubusercontent.com/ywisnu/portfolio/main/views/project1.csv")
    st.dataframe(df, height=300)

    
    "## Revenue Generated"
    df2= pd.read_csv("https://raw.githubusercontent.com/ywisnu/Map/main/Data/revenue2.csv")
    st.dataframe(df2, height=300)



       
  

    

    
    
    


    
    


