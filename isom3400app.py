import streamlit as st
st.write("ISOM3400")
st.write("ISOM3400")

st.header("This is header")
st.title("This is title")

st.markdown("**This is bold text**")
st.markdown("*This is Italic*")

age = st.number_input("Enter your age: ", min_value = 0, max_value = 120, value = 25) #default shows 25
st.write(f"Your age is {age}")

option = st.selectbox("Choose your favorite color:", ["red", "green", "blue"])
st.write(f"You selected: {option}")
