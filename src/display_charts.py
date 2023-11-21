import requests
import streamlit as st


# Feature-API-Call #3 (Name):
#   - Bar chart comparing store discounted price


def display_bar_chart(game_id):
    st.warning("Bar Chart")


# Feature-API-Call #4 (Martin):
#   - Line Chart compare the cheapest store prices vs cheapest historical price


def display_line_chart(game_id):
    res = requests.request(
        "GET", f"https://www.cheapshark.com/api/1.0/games?id={game_id}"
    )
    st.write(res.json())


# Feature-API-Call #5 (Name):
#   - Include all stores for an interactive table


def display_table(game_id):
    st.success("Table")
