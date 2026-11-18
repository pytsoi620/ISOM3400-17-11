import streamlit as st

st.set_page_config(page_title="My First App", page_icon="✨")

# Sidebar
with st.sidebar:
    st.header("Settings")
    name = st.text_input("Your name", "Student")

# Main title
st.title("Welcome to My First Streamlit App")
st.write(f"Hello, **{name}**! This app is built in pure Python.")

# Tabs
tab1, tab2 = st.tabs(["Greeting", "Calculator"])

with tab1:
    st.subheader("A Friendly Greeting")
    mood = st.selectbox("How are you feeling?", ["Happy", "Neutral", "Tired"])
    if st.button("Say hello"):
        st.success(f"Great to hear you're {mood.lower()}, {name}!")

with tab2:
    st.subheader("Simple Calculator")
    col1, col2 = st.columns(2)
    with col1:
        a = st.number_input("First number", value=0.0)
    with col2:
        b = st.number_input("Second number", value=0.0)
    op = st.radio("Operation", ["+", "-", "×", "÷"], horizontal=True)
    if st.button("Calculate"):
        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "×":
            result = a * b
        else:
            result = a / b if b != 0 else "undefined (division by zero)"
        st.metric("Result", result)
