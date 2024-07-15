import streamlit as st

st.set_page_config(
    page_title="Fiber Optic Project",
    page_icon=":earth_asia:",
    layout="wide",
)

"# Fiber Optic Project"

with st.echo(code_location="below"):
    import folium
    import streamlit as st
    from folium.plugins import Draw

    from streamlit_folium import st_folium

    m = folium.Map(location=[106.816281,-6.211156], zoom_start=14,tiles="Cartodb Positron")
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

    c1, c2 = st.columns(2)
    with c1:
        output = st_folium(m, width=900, height=500)

    with c2:
        output = ()
        "# Fiber Optic Project"
        
        
