import streamlit as st
import random as rd
st.title("Ice Breaker AI")
questions =["what's ur name?","what's ur dream job?","wha's ur hobby?"]
name = st.text_input("Enter a person's name")
clicked = st.button("Generate Ice Breaker")
if clicked:
        
    if name=="":
        st.error("please enter your name")
    else:
        st.success(f"hello {name} Welcome to Ice breaker AI")
        st.write("Let's discover interesting questions about you")
        
        random_question = rd.choice(questions)
        st.write(random_question)
        answer = st.text_input("write your answer")
        clicked_ans = st.button("submit answer")
        if clicked_ans:

            
             answers = {random_question: answer}
             answers[random_question] = answer
             st.write(answers)