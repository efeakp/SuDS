import requests
import pandas as pd
import streamlit as st

# Fetch data from the API
url = "https://www.weatherlink.com/embeddablePage/summaryData/a87ff1bc9e5c4ccc9228ea71e02a7b4b"

# Streamlit app
st.title("SuDS Data Dashboard")

try:
    # Send GET request
    response = requests.get(url)
    
    if response.status_code == 200:
        # Parse JSON data
        data = response.json()

        # Extract relevant part of the JSON for DataFrame
        # Adjust this based on the JSON structure (use st.json(data) to inspect it)
        if "currConditionValues" in data:
            conditions = data["currConditionValues"]

            # Convert to a Pandas DataFrame
            df = pd.DataFrame(conditions)

            # Display the DataFrame as a table in Streamlit
            st.subheader("Current Weather Conditions")
            st.dataframe(df)

            # Add a simple chart (example: temperature over time)
            if "temperature" in df.columns:
                st.line_chart(df["temperature"])
        else:
            st.error("Key 'currConditionValues' not found in the API response.")
    else:
        st.error(f"Failed to fetch data. Status Code: {response.status_code}")

except Exception as e:
    st.error(f"Error: {str(e)}")
st.write("Ekolay")