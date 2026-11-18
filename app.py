import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



st.title("Retail Business Dashboard")

st.subheader("Manager Input Section")

st.write("Please enter the monthly sales target and select the region")

st.number_input("Enter Monthly Sales Target(in USD):", value=50000) 

option = st.selectbox("Select Region:",
                      ["North", "South", "West"])


Submit = st.button("Submit")

st.write("**bold** and *italic*")
st.write("**hello** and *world*")
st.code("print('hello')", language="python")

st.text_input("Your name")
st.number_input("Age", min_value=0, max_value=120)
st.slider("Pick a number", 0, 100, 50)
st.selectbox("Choose", ["A", "B", "C"])
st.checkbox("I agree")
st.button("Submitt")

col1, col2, col3 = st.columns(3)
with st.sidebar:
    st.write("Sidebar content")
    st.slider("Pick a number", 0, 100, 50)
st.tabs(["Tab 1", "Tab 2"])



