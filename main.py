import requests

from src.display_charts import *

# Method of access to API
url = 'https://www.cheapshark.com/api/1.0/games?'
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
    st.write(len(r_dict))
    for item in r_dict:
        img = item.get('thumb')
        try:
            if img:  # Check if img is not None
                # get name of game
                select_game = st.checkbox(item.get('external', 'Unknown'), key=item.get('external', 'Unknown'))
                if select_game:
                    display_writing()
                st.image(img, width=200)
        except Exception as e:
            st.warning(f"Could not display image for {item.get('external', 'Unknown')} game. Error: {e}")
