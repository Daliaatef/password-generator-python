import streamlit as st
st.title("append test")
#if "users" not in st.session_state:
st.session_state.users = []
#users = []
name = st.text_input("enter your name")
if st.button("add"):
    st.session_state.users.append(name)
st.write("users",st.session_state.users)