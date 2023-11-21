import json
from datetime import datetime

import requests
import streamlit as st

#Method of access to API
url = 'https://www.cheapshark.com/api/1.0/games?'
payload = {}
headers = {}

st.title('Deal Time')
st.header('Deal Selection Time')

game_name = st.text_input("Game Name")
#url = 'https://www.cheapshark.com/api/1.0/games?title=batman'
payload = {"title" : game_name}
if game_name:
    response = requests.request("GET", url, headers=headers, params=payload)
    r_dict = response.json()
    #response = requests.request("GET", 'https://www.cheapshark.com/api/1.0/games?title=batman', headers=headers, data=payload)
    st.write(r_dict)
    st.write(len(r_dict))
    for x in range(len(r_dict)):
        if r_dict[x]["thumb"] is "None":
            st.warning("Does not exist")
        else:
            st.image(r_dict[x]["thumb"]) 