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
    st.header("Interactive Table")
    st.subheader("Best DEALS below retail")
    
    res_dict = requests.request(
        "GET", f"https://www.cheapshark.com/api/1.0/games?id={game_id}"
    ).json()
    
    deals_df = pd.DataFrame(res_dict['deals'])
    
    #This makes the dealID link with the refferal link as mentioned in the API
    
    deals_df['dealID'] = "https://www.cheapshark.com/redirect?dealID=" + deals_df['dealID']
    
    #Source of images to link with the storeID
    
    deals_df['storeID'] = "https://www.cheapshark.com/img/stores/logos/" + (deals_df['storeID'].astype(int) - 1).astype(str) + ".png"
    
    #st.write(deals_df)
    '''
    st.dataframe(
        deals_df, 
        column_config={
            "storeID"
            "dealID"
            "price"
            "retailPrice"
            "savings"
        }
    )
    '''
    
    #Help with this area if you can, i can't figure out how to disclude a line
    
    agree = st.checkbox("Minimum Percantage savings?")
    min = 0
    if agree :
        min_input = st.text_input("Whats your minimum deal percantage that you want to see?", "0-100")
        try:
            min = int(min)
            if min < 0 or min > 100:
                st.error("Please enter a value between 0 and 100.")
                min = 0
        except ValueError:
            st.error("Please enter a valid integer from 0-100")
    
    if agree and min >= 0 and min <= 100:
        filtered_df = deals_df[deals_df['savings'].astype(float) >= min]
    else:
        filtered_df = deals_df
    
    #End of area i need help with    
        
    #Super helpful in understanding st.dataframe
    #https://github.com/streamlit/docs/blob/main/python/api-examples-source/data.column_config.py
    
    st.dataframe(filtered_df,
                 hide_index= True,
                 column_config={
                     "storeID": st.column_config.ImageColumn("Logo", help="The stores Logo"),
                     "dealID": st.column_config.LinkColumn("Link", help="Link to deal"),
                     "price" : st.column_config.NumberColumn("Deal Price",help="This is the best deal at this site."),
                     "retailPrice": st.column_config.NumberColumn("Cost", help="Normal retail price without deal"),
                     "savings": st.column_config.NumberColumn("Percent", help="Percantage of savings form original retail price")
                 })
