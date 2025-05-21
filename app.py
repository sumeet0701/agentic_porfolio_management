from agentic_pm.utils import setup_logging
import streamlit as st
from agentic_pm.components.agent import planning_agent
from agentic_pm.utils import setup_logging
logger = setup_logging()
st.set_page_config(page_title="Agentic Portfolio Chatbot", page_icon="🤖")

# Add a clear button at the top left
top_left_col, _ = st.columns([10, 10])
with top_left_col:
    if st.button("🗑️ Clear History", use_container_width=False):
        st.session_state.chat_history = []

st.title("Agentic Portfolio Management Chatbot 🤖")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    logger.info("Chat history initialized.")
    st.session_state.chat_history = []
    logger.info(f"{st.session_state.chat_history}")

# Chat input box
user_input = st.chat_input("Type your message...")

# Display chat history
for message in st.session_state.chat_history:
    if message["role"] == "user":
        with st.chat_message("user"):
            st.markdown(message["content"])
    else:
        with st.chat_message("assistant"):
            st.markdown(message["content"])

# Handle new user input
if user_input:
    # Add user message to history
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Get agent response
    with st.spinner("Agent is typing..."):
        try:
            response = planning_agent.run(user_input).content
            # If response is a generator, get the final output
            if hasattr(response, "__iter__") and not isinstance(response, str):
                response = list(response)[-1]
            if isinstance(response, dict) and "content" in response:
                agent_reply = response["content"]
            else:
                agent_reply = str(response)
        except Exception as e:
            agent_reply = f"Error: {e}"

    # Add agent response to history
    st.session_state.chat_history.append({"role": "assistant", "content": agent_reply})

    # Display agent response
    with st.chat_message("assistant"):
        st.markdown(agent_reply)