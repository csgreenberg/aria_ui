import streamlit as st
import streamlit as st
import pandas as pd
#import pandas_bokeh
# import API implementation
from aria_dialog_api_team import Team_ARIADialogAPI as ARDI_API

st.set_page_config(layout="wide")

ardi_api = ARDI_API()
ardi_api.OpenConnection({ "api_key": "AIzaSyCmgdM4lRIRomzksuIWtDqHYU0zmQ046JQ"})
ardi_api.StartSession()

#VIDEO_URL = "file://Users/jon/Downloads/SampleVideo_1280x720_10mb.mp4"
#video_file = open("/Users/jon/Downloads/SampleVideo_1280x720_10mb.mp4", "rb")
#video_file = open("pres/slides_quick.mov", "rb")
video_file = open("pres/ARIA 0.1 Pilot Kiosk Video Slides No Audio.mp4", "rb")
video_file = open("pres/ARIA 0.1 Pilot Kiosk Video Slides.mp4", "rb")
video_bytes = video_file.read()

TESTER_ROLES = ["Red Teamer", "Field Tester"]
if "tester_role" not in st.session_state:
    st.session_state.tester_role = None

SCENARIO_ROLES = ["TV Spoiler", "Meal Planner", "Path Finder"]
if "scenario_role" not in st.session_state:
    st.session_state.scenario_role = None

    
roles = ['story1', "story2", "story3"]
if "role" not in st.session_state:
    st.session_state.role = None

def story_1():
    #st.header("story step 1")
    with st.container(height=900,  border=True):
        st.video(video_bytes)
            
    col1, col2, col3 = st.columns(3)
    with col2:
        if st.button("Are you ready to be a tester?"):
            st.session_state.role = "story2"
            st.rerun()
    
def story_2():
    #st.header("story step 2")
    
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("back"):
            st.session_state.role = "story1"
            st.rerun()
    with col3:
        if st.button("Restart"):
            st.session_state.role = "story1"
            st.rerun()

    with st.container(height=900,  border=True):
        st.image("pres/pics/Slide6.png")

    #st.write("Select a Testing Role")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Be Red Teamer"):
            st.session_state.role = "story3"
            st.session_state.tester_role = "Red Teamer"
            st.rerun()
    with col2:
        if st.button("Be Field Tester"):
            st.session_state.role = "story3"
            st.session_state.tester_role = "Field Tester"
            st.rerun()


def story_3():
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("back"):
            st.session_state.role = "story2"
            st.rerun()
    with col3:
        if st.button("Restart"):
            st.session_state.role = "story1"
            st.rerun()

    with st.container(height=900,  border=True):
        #st.header(f"Tester Specific Info {st.session_state.tester_role}")
        #st.header(f"Scenario Specific  {st.session_state.scenario_role}")
        if (st.session_state.tester_role == "Red Teamer"):
            st.image("pres/pics/Slide7.png")
        else:
            st.image("pres/pics/Slide11.png")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("TV Spoiler"):
            st.session_state.role = "story4"
            st.session_state.scenario_role = "TV Spoiler"
            st.rerun()

    with col2:
        if st.button("Meal Planner"):
            st.session_state.role = "story4"
            st.session_state.scenario_role = "Meal Planner"
            st.rerun()

    with col3:
        if st.button("Pathfinder"):
            st.session_state.role = "story4"
            st.session_state.scenario_role = "Path Finder"
            st.rerun()

        

def story_4():
    #st.header("story step 4")
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("back"):
            st.session_state.role = "story3"
            st.session_state.messages = []
            response = ardi_api.StartSession()
            st.rerun()
    with col3:
        if st.button("Restart"):
            st.session_state.role = "story1"
            st.session_state.messages = []
            response = ardi_api.StartSession()
            st.rerun()

    col1, col2 = st.columns((2,8))


    with col1: 
        st.header(f"Begin your {st.session_state.tester_role} trial for {st.session_state.scenario_role}")

    with col2:
        with st.container(border=True):
            # Make container to display messages, appears above chat_input element
            messages = st.container(height=600, border = True)

            # Initialize chat history
            if "messages" not in st.session_state:
                st.session_state.messages = []

            # Display chat messages from history on app rerun
            for message in st.session_state.messages:
                messages.chat_message(message["role"]).markdown(message["content"])

            # Accept user input
            if prompt := st.chat_input("What is up?"):
                # Add user message to chat history
                st.session_state.messages.append({"role": "user", "content": prompt})
                # Display user message in messages container
                messages.chat_message("user").markdown(prompt)

                # Display assistant response in messages container
                response = ardi_api.GetResponse(prompt)
                messages.chat_message("assistent").write(response['response'])
                
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response})
            
        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("Reset the dialog"):
                st.session_state.messages = []
                response = ardi_api.StartSession()
                st.rerun()
        with col3:
            if st.button("End the session and move on to the survey"):
                st.session_state.role = "story5"
                st.session_state.tester_role = "Meal Planner"
                st.rerun()

def story_5():
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("back"):
            st.session_state.role = "story4"
            st.rerun()
    with col3:
        if st.button("Restart"):
            st.session_state.role = "story1"
            st.rerun()

    col1, col2 = st.columns((4,4))

    with col1:
        st.write("Session Log")        
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    with col2:
        with st.container(height=900,  border=True):
            st.write("Are you a human?")
            toggle = st.toggle("Toggle")
            st.select_slider("How likely are you to be a human?", options = ["very likely", "likely", "neutral", "unlikely", "very unlikely"])
        
role = st.session_state.role

story_page_1 = st.Page(story_1, title="Title story 1", default=(role == 'story1'))
story_page_2 = st.Page(story_2, title="Title Story 2", default=(role == 'story2'))
story_page_3 = st.Page(story_3, title="Title Story 3", default=(role == 'story3'))
story_page_4 = st.Page(story_4, title="Title Story 4", default=(role == 'story4'))
story_page_5 = st.Page(story_5, title="Title Story 5", default=(role == 'story5'))

page_dict = {}
page_dict["Story"] = [story_page_1]
if (st.session_state.role == "story2"):
    page_dict["Story"] = [story_page_2]
if (st.session_state.role == "story3"):
    page_dict["Story"] = [story_page_3]
if (st.session_state.role == "story4"):
    page_dict["Story"] = [story_page_4]
if (st.session_state.role == "story5"):
    page_dict["Story"] = [story_page_5]
# print("About to run")
# print(f"  Role: {st.session_state.role}") 
# print(f"  Tester Role: {st.session_state.tester_role}") 
# print(f"  Scenario Role: {st.session_state.scenario_role}") 
pg = st.navigation(page_dict)
pg.run()
