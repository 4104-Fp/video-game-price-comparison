from src.game_deals import *

st.set_page_config(
    layout="wide",
    page_title="Deal Time",
    page_icon=":video_game:",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://docs.streamlit.io/",
        "Report a bug": "mailto:macohiho@gmail.com?subject=Bug%20Report",
        "About": "Welcome to Game Deals. Developed by 4104 Final Project Org team, 2023. https://github.com/4104-Fp",
    },
)

add_select_box = st.sidebar.selectbox(
    "Select a Project",
    [
        "Game Deals",
        "Project 2",
        "Project 3",
    ],
)

if add_select_box == "Game Deals":
    game_deals()
