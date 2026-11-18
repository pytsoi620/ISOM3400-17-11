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






