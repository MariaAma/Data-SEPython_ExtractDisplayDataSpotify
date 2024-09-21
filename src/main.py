import streamlit as st  
from streamlit_option_menu import option_menu
import introduction, first_analysis
import time


st.set_page_config(page_title="Spotify Extract&Analysis Project", page_icon="🎵")


class MultiApp:  

    def __init__(self):
        self.apps = []

    #def add_apps(self, title, function): self.app.append({'title': title,'function': function})

    def run():
        with st.sidebar:
            app = option_menu(
                menu_title= 'Music App',
                options = ['Introduction','Login','Analysis of Latest Songs','Textbox'],
                menu_icon='rocket-takeoff',
                icons = ["x",'x','x','x','x'],
                styles = { "backgroundColor": "#FFFFFF", "color": "#A7A6BA" }
            )
            
        if app == 'Introduction':
            introduction.app()  

        elif app == 'Login': 
                first_analysis.log()

        elif  app == 'Analysis of Latest Songs':
                first_analysis.first_function()

        elif app == 'Textbox':
                first_analysis.chatbot()
    run()
