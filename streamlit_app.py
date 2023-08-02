import streamlit as st
import pandas as pd

st.title('My first app')

st.write("Here's our first attempt at using data to create a table:")

df = pd.read_csv("my_data.csv")
st.line_chart(df)
