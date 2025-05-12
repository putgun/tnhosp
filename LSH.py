import streamlit as st
import pandas as pd

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    [data-testid="stToolbar"] {visibility: hidden !important;}
    footer {display: none !important;}
    header {visibility: hidden;}
    .viewerBadge_container__1QSob,
    .viewerBadge_link__1S137,
    .viewerBadge_text__1JaDK {display: none !important;}
    </style>
""", unsafe_allow_html=True)

# st.title("台南醫院報帳請款")
#
# upload_file = st.file_uploader("Choose an Excel file", type=['xlsx'])
# if upload_file is not None:
#     df = pd.read_excel(upload_file)
#     st.dataframe(df)

def main():
    st.title("台南醫院報帳請款")

    try:
        data = pd.read_excel("tnhosp.xlsx")

        # Display data
        st.write("### Data from Excel")
        st.dataframe(data)
        columns_selected = data['Total']

        st.write("Total price: $", columns_selected.sum()) # Calculate the total price of purchase

        # Interactive filtering
        st.write("### Filter Data")
        # Each column selected
        # column = st.selectbox("Select column to filter", data.columns)
        # Specific column selected, "Invoice" in this case
        column = st.selectbox("Select column to filter", data.columns[[6,8]])
        unique_values = data[column].unique()
        selected_value = st.selectbox("Select value", unique_values)
        filtered_data = data[data[column] == selected_value]
        st.dataframe(filtered_data)
        st.write('Total price: ', filtered_data['Total'].sum())

    except FileNotFoundError:
        st.error("Excel file not found. Please ensure data is in the same directory")
    except Exception as e:
        st.error(f"Error: {e}")

if __name__ == "__main__":
    main()













