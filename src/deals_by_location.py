import json

import requests
import streamlit as st

file_api_keys = open("src/api_keys.json")
json_file = json.load(file_api_keys)
api_key = json_file["api_key"]


def display_map(api_data):
    st.title("Deals by Location")
    lon1 = api_data["data"]["location"]["coordinates"][0]
    lat1 = api_data["data"]["location"]["coordinates"][1]

    map_creator(lat1, lon1)


@st.cache_data
def map_creator(latitude, longitude):
    from streamlit_folium import folium_static
    import folium

    # center on the station
    m = folium.Map(location=[latitude, longitude], zoom_start=10)

    # add marker for the station
    folium.Marker([latitude, longitude], popup="Station", tooltip="Station").add_to(m)

    # call to render Folium map in Streamlit
    folium_static(m)


def deals_by_location():
    url = f"https://api.airvisual.com/v2/nearest_city?key={api_key}"
    aqi_data_dict = requests.get(url).json()

    if aqi_data_dict["status"] == "success":
        display_map(aqi_data_dict)

    else:
        st.warning("No data available for this location.")
