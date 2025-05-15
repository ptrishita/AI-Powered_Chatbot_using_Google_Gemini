import streamlit as st
from chatbot import get_bot_response

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("🤖 AI-Powered Chatbot")
st.write("Ask me anything!")

user_input = st.text_input("You:")

if user_input:
    with st.spinner("Thinking..."):
        response = get_bot_response(user_input)
    st.success("Bot: " + response)
