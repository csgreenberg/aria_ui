import time
import os
import json
from datetime import datetime

import streamlit as st
from streamlit_javascript import st_javascript


# import API implementation
from aria_dialog_api_team import Team_ARIADialogAPI as ARDI_API
import utilities as util

#### Get the ARIA-UI Environment Variables
# ARIA_UI_PUBLIC_KEY_JSON  = a json string holding the two values of an RSA public key {'n': "...", 'e': ".."}
# ARIA_UI_PRIVATE_KEY_JSON = a json string holding the four values of an RSA public key {'n': "...", 'e': "..", 'd': "..", 'p': "..", 'q': "..", 'rs': ".."}
# ARIA_TEAM_AUTH_JSON      = a json string holding the authentication codes for a team's implementation
# ARIA_INFO_STRING         = a colon separated text string defining the mode of the UI's operation.  This is
#                            either set on the command line for debugging or sent in a URL parameter called
#                            'info'.

ARIA_UI_PUBLIC_KEY = util.make_PublicKey(util.get_env_json_as_dict("ARIA_UI_PUBLIC_KEY_JSON"))
ARIA_UI_PRIVATE_KEY = util.make_PrivateKey(util.get_env_json_as_dict("ARIA_UI_PRIVATE_KEY_JSON"))
ARIA_TEAM_AUTH = util.get_env_json_as_dict("ARIA_TEAM_AUTH_JSON")
ARIA_INFO = util.get_env_string("ARIA_INFO_STRING")
URL_ARIA_INFO = util.extract_param_from_url('info')

### parse the info strings.  The env version takes priorityo
state, eval_mode, user_id, assignment_id = util.parse_info_str("")  ### Set the defaults
if (ARIA_INFO != ""):
    state, eval_mode, user_id, assignment_id = util.parse_info_str(ARIA_INFO)
elif (URL_ARIA_INFO != ""):
    dec_info = util.decrypt_info_str(URL_ARIA_INFO, ARIA_UI_PRIVATE_KEY)
    state, eval_mode, user_id, assignment_id = util.parse_info_str(dec_info)
    
if (state == "DISABLED"):
    st.title("ARIA: Assessing Risks of AI")
    st.header(f'Unfortunately, the application was not passed the appropriate information to start.  Please contact NIST if you did not expect this error.')
else:
    ### Begin the UI
    st.title("ARIA: Assessing Risks of AI")
    st.header(f'Demo1: User /{user_id}/ assignment /{assignment_id}/')

    # Instantiate the API and authenticate
    ardi_api = ARDI_API()
    ardi_api.OpenConnection(ARIA_TEAM_AUTH)
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
        with st.chat_message("assistant"):
            response_info = ardi_api.GetResponse(prompt)
            if (response_info['success']):
                st.write(response_info['response'])
            else:
                st.write("Error: model did not return a response  Contact NIST")
                
    
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response_info['response']})

