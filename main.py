import json
from datetime import datetime

import requests
import streamlit as st

# Method of access to API
url = 'https://www.cheapshark.com/api/1.0/games?'
payload = {}
headers = {}

st.title('Deal Time')
st.header('Deal Selection Time')

game_name = st.text_input("Game Name")
# url = 'https://www.cheapshark.com/api/1.0/games?title=batman'
payload = {"title": game_name}
if game_name:
    # response = requests.request("GET", 'https://www.cheapshark.com/api/1.0/games?title=batman', headers=headers,
    # data=payload)
    response = requests.request("GET", url, headers=headers, params=payload)
    r_dict = response.json()
    # st.write(r_dict)
    st.write(len(r_dict))
    for item in r_dict:
        img = item.get('thumb')
        try:
            if img:  # Check if img is not None
                st.image(img)
        except Exception as e:
            st.warning(f"Could not display image for {item.get('external', 'Unknown')} game. Error: {e}")
