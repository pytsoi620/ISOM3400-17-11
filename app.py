import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



st.title("Retail Business Dashboard")

st.subheader("Manager Input Section")

st.write("Please enter the monthly sales target and selecet the region")

st.write("Enter Monthly Sales Target(in USD):")

st.sidebar.header("Select Region")

option = st.selectbox("Select Region:",
                      ["North", "South", "West"])


Submit = st.button("Submit")




