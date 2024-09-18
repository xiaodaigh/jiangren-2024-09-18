import streamlit as st

# step 3 other plotting libraries should work
import matplotlib.pyplot as plt

# step 2 show a dataframe
import pandas as pd

from shared import tips, TIME_OPTIONS

st.title("Hello World")

st.write("This is a simple Streamlit app.")

st.write("Here's a table:")

# Step 2
st.dataframe(tips)

# Optionally, you can add more customization to the dataframe display
# st.dataframe(tips, width=700, height=300)  # Adjust width and height as needed

# Step 2
st.line_chart(tips, y=["total_bill", "tip"])

# Add a radio button for selecting time (Dinner/Lunch)
time_option = st.radio(
    "Select time of day:",
    options=TIME_OPTIONS,
    index=0  # Default to Dinner
)

# # Filter the dataframe based on the selected time
filtered_tips = tips[tips['time'] == time_option]

# # Display the filtered dataframe
st.subheader(f"Tips data for {time_option}")
st.dataframe(filtered_tips)

# # Update the line chart to use the filtered data
st.subheader(f"Line Chart: Total Bill and Tip for {time_option}")
st.line_chart(filtered_tips, y=["total_bill", "tip"])


# Step 2
# Add a scatter plot of total_bill and tips
st.subheader("Scatter Plot: Total Bill vs. Tip")
st.scatter_chart(
    tips,
    x="total_bill",
    y="tip",
)

# Step 3
st.subheader("Matplot lib or most python plotting libraries should work")
plt.scatter(filtered_tips["total_bill"], filtered_tips["tip"])
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.title("Scatter Plot: Total Bill vs. Tip")
st.pyplot(plt)
