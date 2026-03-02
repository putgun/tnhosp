import streamlit as st

st.markdown("""
    <style>
    /* This targets the text labels in the sidebar navigation */
        [data-testid="stSidebarNav"] span {
            font-size: 20px !important;
            font-weight: bold;
        }
        
        /* This targets any other text inside the sidebar */
        [data-testid="stSidebar"] {
            font-size: 18px;
        }
    #MainMenu {visibility: hidden;}
    [data-testid="stToolbar"] {visibility: hidden !important;}
    footer {display: none !important;}
    header {visibility: hidden;}
    .viewerBadge_container__1QSob,
    .viewerBadge_link__1S137,
    .viewerBadge_text__1JaDK {display: none !important;}
    </style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="Lab Assistant", layout="wide")

st.title("台南醫院計畫")
st.write("Welcome to the automated calculation tool.")

st.info("👈 選擇計畫年度 ")













