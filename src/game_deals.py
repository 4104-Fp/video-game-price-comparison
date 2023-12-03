# it has to have the full path to the file in order to run main.py
from src.utils.display_charts import *


def game_deals():
    st.title("Deal Time")
    st.header("Deal Selection Time")

    # Method of access to API
    url = "https://www.cheapshark.com/api/1.0/games?"

    game_name = st.text_input("Game Name")
    payload = {"title": game_name}

    if game_name:
        # response = requests.request("GET", 'https://www.cheapshark.com/api/1.0/games?title=game_name',
        # data=payload)
        r_dict = requests.request("GET", url, params=payload).json()
        for item in r_dict:
            img = item.get("thumb")
            try:
                if img:
                    game_name = item.get("external", "Unknown")
                    select_game = st.checkbox(game_name, key=game_name)
                    if select_game:
                        # provide gameId so we can get all necessary data
                        # https://www.cheapshark.com/api/1.0/games?id=612
                        game_id = item.get("gameID")

                        st.button("No Deal", type="primary")
                        if st.button("Best Deal"):
                            st.link_button(
                                ":money_mouth_face:Link:money_mouth_face:",
                                "https://www.cheapshark.com/redirect?dealID="
                                + item.get("cheapestDealID"),
                            )
                        else:
                            st.write("")

                        chart = st.radio(
                            "What type of chart would you like to see",
                            [
                                "Bar Chart - Store Discounted Prices",
                                "Line Chart - Store Lowest Price vs All Time Lowest Price",
                                "Interactive Table - Best DEALS below retail",
                            ],
                            index=None,
                        )
                        if chart == "Bar Chart - Store Discounted Prices":
                            display_bar_chart(game_id)
                        if (
                                chart
                                == "Line Chart - Store Lowest Price vs All Time Lowest Price"
                        ):
                            display_line_chart(game_id)
                        if chart == "Interactive Table - Best DEALS below retail":
                            display_table(game_id)
                        else:
                            st.warning("Please select a interactive widget view.")
                    st.image(img, width=200)
            except Exception as e:
                print(f"No Thumbnail Found, {e}, for {item.get('external', 'Unknown')}")
                st.image("public/no_image_found.png", width=200)
