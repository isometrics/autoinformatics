import streamlit as st
import requests

st.title("Simple Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to say?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get AI response from API
    with st.chat_message("assistant"):
        try:
            response = requests.post(
                "http://localhost:8000/chat",
                json={"message": prompt}
            )
            response.raise_for_status()
            ai_response = response.json()
            
            # Display whatever we get from the API
            st.markdown(str(ai_response))
            
            # Add AI response to chat history
            st.session_state.messages.append({"role": "assistant", "content": str(ai_response)})
        except requests.exceptions.RequestException as e:
            error_msg = f"Error connecting to API: {str(e)}"
            st.error(error_msg)
            st.session_state.messages.append({"role": "assistant", "content": error_msg})
