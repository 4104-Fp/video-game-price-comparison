import pandas as pd
import plotly.express as px
import requests
import streamlit as st


# Feature-API-Call #3 (Name):
#   - Bar chart comparing store discounted price


def display_bar_chart(game_id):
    st.warning("Bar Chart")


# Feature-API-Call #4 (Martin):
#   - Line Chart compare the cheapest store prices vs cheapest historical price


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


# Feature-API-Call #5 (Name):
#   - Include all stores for an interactive table


def display_table(game_id):
    st.success("Table")
