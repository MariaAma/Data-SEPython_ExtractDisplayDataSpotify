import streamlit as st  
from streamlit_option_menu import option_menu
import introduction, pages
import time


st.set_page_config(page_title="Spotify Extract&Analysis Project", page_icon="🎵")

if "processing" not in st.session_state:
    st.session_state["processing"] = False 

class MultiApp: 

    def __init__(self):
        self.apps = []

    def add_apps(self, title, function):
        self.app.append({
            'title': title,
            'function': function
        })

    def run():
        with st.sidebar:
            app = option_menu(
                menu_title= 'Music App',
                options = ['Introduction','Login','Analysis of Latest Songs','Chatbot'],
                menu_icon='rocket-takeoff',
                icons = ["x",'x','x','x','x'],
                default_index= 0,
                styles = { "backgroundColor": "#FFFFFF", "color": "#A7A6BA" }
            )
            
        if app == 'Introduction':
            if not st.session_state["processing"]:  
                introduction.app()  
        elif app == 'Login':
            if not st.session_state["processing"]:  
                st.session_state["processing"] = True  
                try:
                    pages.log()
                finally:
                    st.session_state["processing"] = False 
            else:
                time.sleep(3)
                st.session_state["processing"] = True 
                pages.log()

        elif  app == 'Analysis of Latest Songs':
            if not st.session_state["processing"]:  
                st.session_state["processing"] = True  
                try:
                    pages.first_function()
                finally:
                    st.session_state["processing"] = False 
            else:
                time.sleep(3)
                st.session_state["processing"] = True 
                pages.first_function()
        elif app == 'Chatbot':
                pages.chatbot()
    run()
