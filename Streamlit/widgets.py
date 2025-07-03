import streamlit as st

st.title("Hey, how you doin:")

name = st.text_input("Please enter your name here")

age = st.slider("Select your age:", 1,100,20)


if name:
    st.write(f"Welcome onboard {name}!")

if age:
    st.write(f"Your age is {age}")

food = ["Apple", "Banana", "Orange", "Papaya"]
choice = st.selectbox("Choose your favourite food", food)

