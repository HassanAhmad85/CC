import streamlit as st
from openai import OpenAI
from PIL import Image

# Load the page icon
im = Image.open(r'src/pages/Content/Screenshot 2024-04-24 013429.png')

# Set Streamlit page config
st.set_page_config(page_title="FIDIC 2017", page_icon=im, layout="wide")

hide_default_format = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
/* Reduce the padding on the sides of the main panel */
.css-18e3th9 {
    padding: 0 1rem 0 1rem;
}
/* Center align the title */
h1 {
    text-align: center;
}
/* Message container style */
.message-container {
    border: 1px solid #ddd;
    border-radius: 10px;
    padding: 10px;
    margin-bottom: 10px;
}
</style>
"""
st.markdown(hide_default_format, unsafe_allow_html=True)

# Configuration for OpenAI
ASSISTANT_ID = "asst_CEez9ujyTOyButHOsm88Trob"
API_KEY = "sk-proj-4FeL3zTinepVnXGgYvMjT3BlbkFJ9PXtOQYFmXDvPJ0SH0Ee"

# Initialize the OpenAI client
client = OpenAI(api_key=API_KEY)

def get_response(query):
    thread = client.beta.threads.create(
        messages=[
            {
                "role": "user",
                "content": query,
            }
        ]
    )
    run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=ASSISTANT_ID)
    
    # Wait for run to complete
    while run.status != "completed":
        run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
    
    # Get the latest message from the thread
    message_response = client.beta.threads.messages.list(thread_id=thread.id)
    messages = message_response.data
    return messages[0].content[0].text.value
pass

st.title("Claim Correspondent FIDIC 2017 Red Book")

# UI for user input and send button
user_input = st.text_area("Example Prompt: Write a notice for extension of time due to the employer's failure to provide access required for the Contractor to the site."
,key="user_input", height=75) 

if st.button("Send"):
    if user_input.strip():  # Check if the input is not just whitespace
        response = get_response(user_input)
        # Manage conversation state
        if 'conversation' not in st.session_state:
            st.session_state.conversation = []
        st.session_state.conversation.insert(0, ("Claim Correspondent", response))
        st.session_state.conversation.insert(0, ("User", user_input))
        # Clear input
        st.experimental_rerun()

# Display message history
st.markdown("### Responses:")
if 'conversation' in st.session_state:
    for i in range(0, len(st.session_state.conversation), 2):
        with st.container():
            col1, col2 = st.columns([1, 3])
            with col1:
                st.markdown("### User")
            with col2:
                st.markdown(f"{st.session_state.conversation[i][1]}")

            if i+1 < len(st.session_state.conversation):
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.markdown("### Claim Correspondent")
                with col2:
                    st.markdown(f"{st.session_state.conversation[i+1][1]}")

            st.markdown("<div class='message-container'></div>", unsafe_allow_html=True)

# Custom styles for message history
st.markdown("""
<style>
.stText, .stMarkdown {
    margin-bottom: 1rem;
    border-bottom: 1px solid #eee;
    padding-bottom: 0.5rem;
}
/* Adjust text area width to prevent overflow */
.stTextArea {
    width: 100%;
    word-wrap: break-word; /* Ensures text wraps to avoid horizontal scrolling */
}
</style>
""", unsafe_allow_html=True)
