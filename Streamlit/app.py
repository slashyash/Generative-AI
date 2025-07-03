import streamlit as st
import pandas as pd
import numpy as np
import random

## Title of the App
st.title("Helo Streamlit")

## A Simple Text
st.write("This is a Text")

## Create a Dataframe
df = pd.DataFrame({
    'first column' : [1,2,3,4],
    'second column' : [100,200,300,400]
})

## Dispaly the Dataframe
st.write("Here is the dataframe")
st.write(df)

chart_data = pd.DataFrame(
    np.random.randn(20,3), columns=['s', 'p', 'd']
)
st.line_chart(chart_data)