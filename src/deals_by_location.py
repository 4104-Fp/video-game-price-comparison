import json

import requests
import streamlit as st

file_api_keys = open("src/api_keys.json")
json_file = json.load(file_api_keys)
api_key = json_file["api_key"]


@st.cache_data
def __map_creator(latitude, longitude):
    from streamlit_folium import folium_static
    import folium

    # center on the station
    m = folium.Map(location=[latitude, longitude], zoom_start=10)

    # add marker for the station
    folium.Marker([latitude, longitude], popup="Station", tooltip="Station").add_to(m)

    # call to render Folium map in Streamlit
    folium_static(m)


def __display_map(api_data):
    st.title("Deals by Location")
    lon1 = api_data["data"]["location"]["coordinates"][0]
    lat1 = api_data["data"]["location"]["coordinates"][1]

    __map_creator(lat1, lon1)


def __display_deals(all_deals_dict):
    import random

    random_store_deals = []
    for i in range(10):
        random_store_deals.append(random.choice(all_deals_dict))

    for i, item in enumerate(random_store_deals):
        img = item.get("thumb")
        try:
            col1, col2 = st.columns([1, 2])
            with col1:
                if img:
                    st.image(img, width=200)
            with col2:
                savings = item.get("savings")
                st.write("Title: ", item.get("title", "Unknown"))
                st.write("Game ID: ", item.get("gameID"))
                st.write("Sale Price: ", item.get("salePrice"))
                st.write("Normal Price: ", item.get("normalPrice"))
                st.write(f"Savings: {savings}%")
            st.markdown("---")
        except Exception as e:
            title = item.get("title")
            print(f"Game does not have thumbnail {title}: {e}")
            continue


def deals_by_location():
    air_visual_url = f"https://api.airvisual.com/v2/nearest_city?key={api_key}"
    cheap_shark_url = "https://www.cheapshark.com/api/1.0/deals"
    all_deals_dict = requests.get(cheap_shark_url).json()
    aqi_data_dict = requests.get(air_visual_url).json()

    if aqi_data_dict["status"] == "success":
        __display_map(aqi_data_dict)
        st.header("Local Based Deals")
        st.subheader("Best Deals Near You")
        st.markdown("---")
        __display_deals(all_deals_dict)

    else:
        st.warning("No data available for this location.")
