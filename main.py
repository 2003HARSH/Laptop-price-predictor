import streamlit as st

from streamlit_option_menu import option_menu
import home , about 

st.set_page_config(
        page_title="Laptop Price Predictor",
)

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        with st.sidebar:
            app =option_menu(
                menu_title=None,
                options=['Home','About'],
                icons=['house','file-person']
            )

        
        if app == "Home":
            home.app()  
        if app == 'About':
            about.app()    
             
          
             
    run()            
         