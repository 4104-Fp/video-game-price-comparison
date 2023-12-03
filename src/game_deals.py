# it has to have the full path to the file in order to run main.py
from datetime import datetime

from src.utils.display_charts import *


def game_deals():
    st.title("Deal Time")
    st.subheader("Deal Selection Time")

    # Method of access to API
    url = "https://www.cheapshark.com/api/1.0/games?"

    game_name = st.text_input(
        "Game Name. e.g: Cyberpunk 2077", placeholder="Cyberpunk 2077"
    )
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

                        cheapest_price_date = (
                            requests.request(
                                "GET",
                                f"https://www.cheapshark.com/api/1.0/games?id={game_id}",
                            )
                            .json()
                            .get("cheapestPriceEver")
                            .get("date")
                        )
                        date = st.date_input("Days since cheapest deal", value=None)
                        try:
                            if date:
                                json_date = datetime.fromtimestamp(cheapest_price_date)
                                current_date = datetime(date.year, date.month, date.day)
                                st.write(current_date - json_date)
                        except Exception as e:
                            print(f"Error parsing date: {e}")
                        # if date:
                        #     json_date = datetime.fromtimestamp(item.get("date"))
                        #     selected_date = datetime(date.year, date.month, date.day)
                        #     st.write(selected_date)
                        #     st.write(json_date)

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
