import ollama
import streamlit as st
st.title("Welcome to my Chatbot App!!!")
if "messages" not in st.session_state:
    st.session_state.messages = []
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
question = st.chat_input("You:")

if question:
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })
    with st.chat_message("user"):
        st.write(question)
    with st.spinner("thinking..."):
    response = ollama.chat(
        model="llama3.2:3b",
        messages=st.session_state.messages
    )

    answer = response["message"]["content"]
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
    with st.chat_message("assistant"):
        st.write(answer)

    print("---- Chat history -----")
    for msg in st.session_state.messages:

        print(msg["role"], ":", msg["content"])