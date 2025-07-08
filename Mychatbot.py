import streamlit as st
import google.generativeai as genai

# Api key is pasted in the secrets.toml file
# Load Gemini API key securely from secrets

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

#  Loading the Gemini model
model = genai.GenerativeModel("models/gemini-1.5-flash")

# Streamlit UI setup process
st.set_page_config(page_title="Keerthi's Chatbot", page_icon="🤖")
st.title("💬 Welcome to KEERTHI's Chatbot")

# Chat history in session state
if "chat" not in st.session_state:
    st.session_state.chat = []

#  Button to clear chat and rerun
if st.button("🔄 Start New Chat"):
    st.session_state.chat = []
    st.rerun()

# Input box
user_input = st.text_input("You:", "")

#  Generating the response
if user_input:
    st.session_state.chat.append(("You", user_input))
    try:
        response = model.generate_content(user_input)
        reply = response.text
    except Exception as e:
        reply = f"❌ Error: {str(e)}"
    st.session_state.chat.append(("Keerthi's-bot", reply))

# Displaying the chat history
for sender, message in st.session_state.chat:
    st.markdown(f"**{sender}:** {message}")
