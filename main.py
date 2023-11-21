import requests

from src.display_charts import *

# Method of access to API
url = 'https://www.cheapshark.com/api/1.0/games?'

st.title('Deal Time')
st.header('Deal Selection Time')

game_name = st.text_input("Game Name")
# url = 'https://www.cheapshark.com/api/1.0/games?title=batman'
payload = {"title": game_name}
if game_name:
    # response = requests.request("GET", 'https://www.cheapshark.com/api/1.0/games?title=batman', headers=headers,
    # data=payload)
    response = requests.request("GET", url, params=payload)
    r_dict = response.json()
    st.write(len(r_dict))
    for item in r_dict:
        img = item.get('thumb')
        try:
            if img:  # Check if img is not None
                # get name of game
                game_name = item.get('external', 'Unknown')
                select_game = st.checkbox(game_name, key=game_name)
                if select_game:
                    display_bar_chart()
                    display_line_chart()
                    display_table()
                st.image(img, width=200)
        except Exception as e:
            # display error in console
            print(f"No Thumbnail Found, {e}, for {item.get('external', 'Unknown')}")
            st.warning("No Thumbnail Found")
