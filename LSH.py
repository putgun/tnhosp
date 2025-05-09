import streamlit as st
import pandas as pd

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    [data-testid="stToolbar"] {visibility: hidden !important;}
    fotter {visibility: hidden;}
    header {visibility: hidden;}
    ._profileContainer_gzau3_53 {display: none;}
    ._container_gzau3_1 _viewerBadge_nim44_23 {display: none;}
    ._container_gzau3_1 _viewerBadge_nim44_23 {display: none;}
    </style>
""", unsafe_allow_html=True)

# st.title("Display Excel Data with Streamlit")
#
# upload_file = st.file_uploader("Choose an Excel file", type=['xlsx'])
# if upload_file is not None:
#     df = pd.read_excel(upload_file)
#     st.dataframe(df)

def main():
    st.title("Excel Data Display with Streamlit")

    try:
        data = pd.read_excel("tnhosp.xlsx")

        # Display data
        st.write("### Data from Excel")
        st.dataframe(data)

        # Interactive filtering
        st.write("### Filter Data")
        # Each column selected
        # column = st.selectbox("Select column to filter", data.columns)
        # Specific column selected, "Invoice" in this case
        column = st.selectbox("Select column to filter", data.columns[6])
        unique_values = data[column].unique()
        selected_value = st.selectbox("Select value", unique_values)
        filtered_data = data[data[column] == selected_value]
        st.dataframe(filtered_data)

    except FileNotFoundError:
        st.error("Excel file not found. Please ensure data is in the same directory")
    except Exception as e:
        st.error(f"Error: {e}")

if __name__ == "__main__":
    main()













