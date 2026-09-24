import streamlit as st
st.title("my first streamlit App!!!")
st.write("Welcome to my AI application!")
name=st.text_input("Enter your name")
if st.button("submit"):
    st.write("hello",name)
    