import streamlit as st
st.write("ISOM3400")
st.write("ISOM3400")

st.title("Retail Business Dashboard")
st.header("Manager Input Section")
st.write("Please enter the monthly sales target and enter the region.")
target = st.number_input("Enter monthly sales target (USD):", min_value = 0, value = 0)
if target > 100000:
  st.write("Great! You have enter an ambitious target!")
region = st.selectbox("Select region:", ["East", "South", "West", "North"])

if st.button("Submit"):
  st.write(f"You submit! target: {target}, region: {region}.")
  st.success("Complete")
  

