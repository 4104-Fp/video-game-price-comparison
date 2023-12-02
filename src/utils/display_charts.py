import pandas as pd
import plotly.express as px
import requests
import streamlit as st


# Feature-API-Call #3 (Name):
#   - Bar chart comparing store discounted price
def display_bar_chart(game_id):
    st.warning("Bar Chart")


def display_line_chart(game_id):
    res_dict = requests.request(
        "GET", f"https://www.cheapshark.com/api/1.0/games?id={game_id}"
    ).json()
    all_time_lowest = res_dict.get("cheapestPriceEver").get("price")
    store_lowest = [store.get("price") for store in res_dict.get("deals")]

    data = pd.DataFrame(
        {
            "Store Lowest Price": store_lowest
            if len(store_lowest) > 1
            else store_lowest * 5,
            "All Time Lowest Price": [all_time_lowest] * len(store_lowest)
            if len(store_lowest) > 1
            else [all_time_lowest] * 5,
        }
    )

    fig = px.line(
        data,
        height=500,
    )
    fig.update_layout(
        title="Store Lowest Price vs All Time Lowest Price",
        xaxis_title="Store",
        yaxis_title="Price",
    )
    st.subheader("Line Chart")
    st.info("If the line is flat, there is only one store.")
    st.plotly_chart(fig, use_container_width=True)


def get_logo_url(store_id):
    try:
        logo_url = (
            f"https://www.cheapshark.com/img/stores/logos/{int(store_id) - 1}.png"
        )
        return logo_url
    except Exception as e:
        print(f"Error generating logo URL for storeID {store_id}: {e}")
        return None


def display_table(game_id):
    st.header("Interactive Table")
    st.subheader("Best DEALS below retail")

    res_dict = requests.request(
        "GET", f"https://www.cheapshark.com/api/1.0/games?id={game_id}"
    ).json()

    deals_df = pd.DataFrame(res_dict["deals"])

    deals_df["dealID"] = (
            "https://www.cheapshark.com/redirect?dealID=" + deals_df["dealID"]
    )

    deals_df["storeID"] = deals_df["storeID"].apply(get_logo_url)

    agree = st.checkbox("Minimum Percentage savings?")
    min_value = 0
    if agree:
        min_input = st.text_input(
            "What's your minimum deal percentage that you want to see? eg. 50", "0"
        )
        try:
            min_value = int(min_input)
            if min_value < 0 or min_value > 100:
                st.error("Please enter a value between 0 and 100.")
                min_value = 0
        except ValueError:
            st.error("Please enter a valid integer from 0-100")

    if agree and 0 <= min_value <= 100:
        filtered_df = deals_df[deals_df["savings"].astype(float) >= min_value]
    else:
        filtered_df = deals_df

    st.dataframe(
        filtered_df,
        hide_index=True,
        column_config={
            "storeID": st.column_config.ImageColumn("Logo", help="The stores Logo"),
            "dealID": st.column_config.LinkColumn("Link", help="Link to deal"),
            "price": st.column_config.NumberColumn(
                "Deal Price", help="This is the best deal at this site."
            ),
            "retailPrice": st.column_config.NumberColumn(
                "Cost", help="Normal retail price without deal"
            ),
            "savings": st.column_config.NumberColumn(
                "Percent", help="Percentage of savings form original retail price"
            ),
        },
    )
