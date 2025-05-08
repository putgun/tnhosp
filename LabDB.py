import streamlit as st
import mysql.connector
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv() # Load variables from .env into enviroment
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")

# Function to connect to MySQL and fetch data
def get_data():
    try:
        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database="practice"
        )
        query = "SELECT * FROM Invoices"
        data = pd.read_sql(query, connection)

        connection.close()
        return  data

    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
        return None

# Streamlit app
def main():
    st.title("MySQL Data Display with Streamlit")

    # Fetch data
    data = get_data()

    if data is not None:
        # Display data in a table
        st.write("### Data from MySQL")
        st.dataframe(data)

        # Optional: Display data in other formats
        st.write("### First 5 Rows")
        st.table(data.head())

        # Optional: Add some interactivity
        st.write("### Filter Data")
        column = st.selectbox("Select column to filter", data.columns)
        unique_values = data[column].unique()
        selected_value = st.selectbox("Select value", unique_values)
        filtered_data = data[data[column] == selected_value]
        st.dataframe(filtered_data)


if __name__ == "__main__":
    main()


