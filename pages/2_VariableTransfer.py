import streamlit as st

st.title("Variable Transfer")

st.write("Jeśli coś wpisałeś to jest to: ", st.session_state["my_input"])
