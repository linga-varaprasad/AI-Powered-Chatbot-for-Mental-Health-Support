import streamlit as st
from dotenv import load_dotenv
import os
from groq import Groq
from tenacity import retry, stop_after_attempt, wait_random_exponential

# Load environment variables
load_dotenv()

# Initialize the Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Function to generate responses based on user input
@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(3))
def generate_response(user_input):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful healthcare support chatbot. Provide empathetic and informative responses to user queries about health and well-being.",
                },
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
            model="llama3-70b-8192",
            max_tokens=500,
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        st.error(f"Error generating response: {str(e)}")
        return "I'm sorry, I'm having trouble generating a response right now. Please try again later."

# Streamlit UI
st.set_page_config(page_title="Healthcare Support Chatbot", page_icon="🏥", layout="wide")

# Apply custom CSS
st.markdown("""
    <style>
    .stTextInput > div > div > input {
        caret-color: #4CAF50;
    }
    .stButton > button {
        color: #4CAF50;
        border-color: #4CAF50;
    }
    .stButton > button:hover {
        background-color: #4CAF50;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.title('🏥 Healthcare Support Chatbot')
st.subheader("Welcome! How can I assist you with your health concerns today?")

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Chat container
chat_container = st.container()

# Display chat messages
with chat_container:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# User input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Generate and display AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            ai_response = generate_response(user_input)
            st.session_state.messages.append({"role": "assistant", "content": ai_response})
            st.markdown(ai_response)

# Sidebar for additional features
with st.sidebar:
    st.header("Options")
    
    if st.button("Clear Conversation"):
        st.session_state.messages = []
        st.experimental_rerun()
    
    st.subheader("Quick Health Tips")
    st.info("Remember to stay hydrated and get enough sleep!")
    
    st.subheader("Emergency Contacts")
    st.warning("For emergencies, call 911 or your local emergency number.")

# Footer
st.markdown("---")
st.caption("**Note:** This chatbot is for informational purposes only and does not replace professional medical advice.")
st.caption("Your privacy is important. Conversations are not stored after the session ends.")