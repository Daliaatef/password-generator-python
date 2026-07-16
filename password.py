import streamlit as st
import random as rd
import string

st.set_page_config(page_title="password generator",layout="centered")
st.title("Password Generator")
st.write("Generate strong and secure password")

#user setting
length = st.slider("password length", min_value=8 , max_value= 32 , value=12)
include_digits = st.checkbox("Include digits(0-9)" , value = True)
include_symbols = st.checkbox("Include symbols(@ ,# ,$ ,% ,^)" , value = True)
include_uppercase = st.checkbox("Include uppercase(A-Z)", value = True)
include_lowercase = st.checkbox("Include lowercase(a-z)",value=True)
if st.button("Generate password"):
    characters = ''
    if include_digits:
        characters +=string.digits
    if include_symbols:
        characters+= string.punctuation
    if include_lowercase:
        characters+=string.ascii_lowercase
    if include_uppercase:
        characters+= string.ascii_uppercase
    
    if characters:
        password = "".join(rd.choice(characters) for _ in range(length))
        st.success("you generate your password")
        st.write(password)
    else:
        st.error("you must select at least one checkbox")

