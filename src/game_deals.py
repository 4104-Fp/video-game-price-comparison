# it has to have the full path to the file in order to run main.py
from datetime import datetime

from src.utils.display_charts import *


def __display_date_since(game_id):
    date = st.date_input("Days since cheapest deal", value=None)

    cheapest_price_date = (
        requests.request(
            "GET",
            f"https://www.cheapshark.com/api/1.0/games?id={game_id}",
        )
        .json()
        .get("cheapestPriceEver")
        .get("date")
    )
    try:
        if date:
            cheapest_date = datetime.fromtimestamp(cheapest_price_date)
            current_date = datetime(date.year, date.month, date.day)
            st.write(
                f"Its been {current_date - cheapest_date} and hours since the cheapest deal"
            )
    except Exception as e:
        print(f"Error parsing date: {e}")


def __show_charts(game_id):
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
    if chart == "Line Chart - Store Lowest Price vs All Time Lowest Price":
        display_line_chart(game_id)
    if chart == "Interactive Table - Best DEALS below retail":
        display_table(game_id)
    else:
        st.warning("Please select a interactive widget view.")


def __show_deal_no_deal(item):
    st.button("No Deal", type="primary")
    if st.button("Best Deal"):
        st.link_button(
            ":money_mouth_face:Link:money_mouth_face:",
            "https://www.cheapshark.com/redirect?dealID=" + item.get("cheapestDealID"),
        )
    else:
        st.write("")


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

                        __show_deal_no_deal(item)
                        __display_date_since(game_id)
                        __show_charts(game_id)
                    st.image(img, width=200)
            except Exception as e:
                print(f"No Thumbnail Found, {e}, for {item.get('external', 'Unknown')}")
                st.image("public/no_image_found.png", width=200)
