import streamlit as st

st.set_page_config(
    page_title="Fiber Optic Project",
    page_icon=":earth_asia:",
    layout="wide",
)


with st.echo(code_location="below"):
    import folium
    import streamlit as st
    from folium.plugins import Draw

    from streamlit_folium import st_folium

    m = folium.Map(location=[39.949610, -75.150282], zoom_start=5)
    Draw(export=True).add_to(m)

    c1, c2 = st.columns(2)
    with c1:
        output = st_folium(m, width=700, height=500)

    with c2:
        st.write(output)
