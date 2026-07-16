import streamlit as st
st.title("welcom")
if "users" not in st.session_state:

    st.session_state.users = []
name = st.text_input("enter ur name")
if st.button("add"):
    st.session_state.users.append(name)
st.write(st.session_state.users)
