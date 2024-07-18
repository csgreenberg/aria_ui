import streamlit as st
from streamlit_javascript import st_javascript
from urllib.parse import urlparse
from urllib.parse import parse_qs

import random
import time


# import API implementation
from aria_dialog_api_team import Team_ARIADialogAPI as ARDI_API

# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

### Look for USER ID via <URL>/?userid=302-billy&sessionid=9001
userid = None

url = st_javascript("await fetch('').then(r => window.parent.location.href)")
parsed_url = urlparse(url)
query_dict = parse_qs(parsed_url.query)
if ('userid' in query_dict):
    userid = query_dict['userid'][0]
    

st.title("ARIA: Assessing Risks of AI")
st.header(f'User /{userid}/ Testing - Demo1')

# define auth used by API implementation
import os
import json
AUTH_ENV_VAR = 'ARIA_AUTH_JSON'
auth_json = os.getenv(AUTH_ENV_VAR)
auth = {}  ### The default
if (auth_json is not None):
    try:
        auth = json.loads(auth_json)
        print(f"Auth Dictionary: {auth}")
    except ValueError as e:
        print(f"Error parsing JSON string /{auth_json}/ error {e}.")
        print("Exiting")
        exit(1)

# Instantiate the API and authenticate
ardi_api = ARDI_API()
ardi_api.OpenConnection(auth)
ardi_api.StartSession()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
#    with st.chat_message("assistant"):
#        response = st.write_stream(response_generator())
    with st.chat_message("assistant"):
        response = ardi_api.GetResponse(prompt)
        st.write(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

