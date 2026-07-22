#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Script:
    ui.py
Description:
    Streamlit Graphical USer Interface.
Author:
    Jose Miguel Rios Rubio
Date:
    2024-06-10
Version:
    1.0.0
'''

###############################################################################
# Standard Libraries
###############################################################################

# Logging Library
import logging

# Operating System Library
from os import path as os_path

# Error Traceback Library
from traceback import format_exc


###############################################################################
# Third-Party Libraries
###############################################################################

# StreamLit
import streamlit as st


###############################################################################
# Project Local Libraries
###############################################################################

# None


###############################################################################
# Logger Setup
###############################################################################

logger = logging.getLogger(__name__)


###############################################################################
# Constants
###############################################################################

# Actual constants.py full path directory name
PWD = os_path.dirname(os_path.realpath(__file__))

# Path to external resource file that has some example text
FILE_RES_EXAMPLE = f"{PWD}/../res/example.md"


###############################################################################
# Auxiliary Classes
###############################################################################

class CallbackType():
    '''Types of callback class.'''
    def __init__(self, app=None, ui=None):
        self.ui = ui
        self.app = app


class Callbacks():
    '''UI Elements Callbacks class.'''
    def __init__(self):
        self.sidebar_btn_0 = CallbackType()
        self.sidebar_btn_1 = CallbackType()
        self.sidebar_btn_2 = CallbackType()
        self.sidebar_btn_3 = CallbackType()
        self.btn_clickme = CallbackType()


class Button():
    '''Button UI element class.'''
    def __init__(self, uid, label, callback_app=None, callback_ui=None):
        self.uid = uid
        self.label = label
        self.callback = CallbackType(callback_app, callback_ui)


class Footbar():
    '''Footbar UI element class.'''
    def __init__(self, text=""):
        self.text = text
        self.style = """
        <style>
            .footer {
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                background-color: #1D6AB8;
                color: white;
                z-index: 1000;
                padding-right: 20px;
                height: 30px;
                text-align: right;
            }
        </style>
        """
        self.bar = ""

    def set_text(self, text):
        self.text = text
        self.bar = f"{self.style}<div class='footer'><p>{self.text}</p></div>"

    def update(self):
        '''Draw Page Footer.'''
        st.markdown(self.bar, unsafe_allow_html=True)


###############################################################################
# UI Class
###############################################################################

class UserInterface():
    '''
    Graphical User Interface Class that defines all the visual elements
    of an Application.
    '''

    def __init__(self):
        '''UserInterface Constructor.'''
        # Setup Attributes
        self.callbacks = Callbacks()
        self.footbar = Footbar()
        self.title = ""
        self.sidebar_btn_id = 0
        self.cb_buttons = {}
        # Bind UI Callbacks
        self.callbacks.sidebar_btn_0.ui = self.show_content_text
        self.callbacks.sidebar_btn_1.ui = self.show_content_io
        self.callbacks.sidebar_btn_2.ui = self.show_content_selector
        self.callbacks.sidebar_btn_3.ui = self.show_content_other
        # Initialize session variables
        self.session_set("menu_option", 0)
        self.session_set("menu_option_previous", 0)
        # Load resources from external files
        self.example_text = self.file_read(FILE_RES_EXAMPLE)

    def session_set(self, key, value):
        '''
        Create a new session variable with specified key and value.
        Do nothing if session variable already exists.
        '''
        if key not in st.session_state:
            st.session_state[key] = value

    def session_update(self, key, value):
        '''Update a session variable with specified key and value.'''
        st.session_state[key] = value

    def session_get(self, key):
        '''
        Get a current session stored variable of specified key.
        Return None if it doesn't exists.
        '''
        value = None
        if key in st.session_state:
            value = st.session_state[key]
        return value

    def file_read(self, file_path):
        '''Read full content of a text file.'''
        read_text = ""
        try:
            with open(file_path, "r", encoding="utf-8") as file_reader:
                read_text = file_reader.read()
        except Exception:
            logger.error(format_exc())
            logger.error("Fail to read binary file %s", file_path)
        return read_text

    def hide_deploy_button(self):
        '''
        Notice: At 01/06/2024, Streamlit doesn't provide an API function
        to hide the Deploy button, so it's done modifying the CSS style
        of that element (this approach could be invalid in the future).
        '''
        btn_style = "<style>.stDeployButton {display:none;}</style>"
        st.markdown(btn_style, unsafe_allow_html=True)

    def set_sidebar_button(self, label, callback):
        '''Set a button on the left sidebar menu.'''
        btn = Button(self.sidebar_btn_id, label, callback.app, callback.ui)
        self.sidebar_btn_id = self.sidebar_btn_id + 1
        self.cb_buttons[btn.uid] = btn
        if st.sidebar.button(label, btn.uid):
            if btn.callback.app:
                btn.callback.app()
            self.session_update("menu_option", btn.uid)

    def setup_page(self, title, layout, about, footbar_text, icon=None):
        '''
        Setup Streamlit Web Page Configuration and General Stuffs.
        Layout: "centered" or "wide".
        '''
        # Page Configuration
        self.title = title
        st.set_page_config(page_title=title, page_icon=icon, layout=layout,
            menu_items={"Get help": None, "Report a Bug": None, "About": about}
        )
        self.hide_deploy_button()
        # Draw SideBar
        self.setup_sidebar()
        # Draw Content based on session sidebar menu option
        self.cb_buttons[self.session_get("menu_option")].callback.ui()
        # Draw Footbar
        self.footbar.set_text(footbar_text)
        self.footbar.update()

    def setup_header(self, text=""):
        '''Setup Page Header.'''
        st.title(self.title)
        st.header(text)
        st.markdown("---")

    def setup_sidebar(self):
        '''Setup SideBar Menu.'''
        # Sidebar Title
        st.sidebar.title("Menu")
        st.sidebar.markdown("---")
        # Create Buttons
        self.set_sidebar_button("Texts", self.callbacks.sidebar_btn_0)
        self.set_sidebar_button("Input & Output", self.callbacks.sidebar_btn_1)
        self.set_sidebar_button("Selectors", self.callbacks.sidebar_btn_2)
        self.set_sidebar_button("Others", self.callbacks.sidebar_btn_3)

    def show_content_text(self):
        '''Show Page Content: Text.'''
        # Set Header
        self.setup_header("A variety of Streamlit Elements")
        # Text Label: Standard
        st.subheader("Standard Text")
        st.write("This demo shows a some Streamlit elements in action.")
        st.markdown("---")
        # Text Label: Markdown
        st.subheader("Markdown Text")
        st.markdown("This is an *example* of **markdown** text.")
        st.markdown("---")
        # Text Label: Code
        st.subheader("Code Text")
        st.code("print('Hello, World!')")
        st.markdown("---")
        # Text Label: LaTeX
        st.subheader("LaTeX")
        st.latex(r'''a + ar + ar^2 + ar^3 + \cdots + ar^n''')
        st.markdown("---")
        # Resource file text
        st.markdown(self.example_text, unsafe_allow_html=True)
        st.markdown("---")

    def show_content_io(self):
        '''Show Page Content: Inputs / Outputs.'''
        # Set Header
        self.setup_header("Inputs / Outputs Elements")
        # Text Input
        st.subheader("Text Input")
        name = st.text_input("Enter your name:")
        if name:
            st.write(f"Hello, {name}!")
        st.markdown("---")
        # Button
        st.subheader("Button")
        if st.button("Click Me"):
            if self.callbacks.btn_clickme.app:
                self.callbacks.btn_clickme.app()
            st.write("Button clicked!")
        st.markdown("---")
        # Checkbox
        st.subheader("CheckBox")
        checkvalue = st.checkbox("Show/Hide")
        if checkvalue:
            checkvalue = "checked"
        else:
            checkvalue = "not-checked"
        st.write(f"Checkbox: {checkvalue}")

    def show_content_selector(self):
        '''Show Page Content: Selector.'''
        # Set Header
        self.setup_header("Selectors Elements")
        # SelectBox
        st.subheader("SelectBox")
        option1 = st.selectbox("Select Option",
                            ["Option 1", "Option 2", "Option 3"])
        st.write(f"Selected options: {option1}")
        st.markdown("---")
        # SelectSlide
        st.subheader("SelectSlide")
        option2 = st.select_slider("Select Slider Option",
                                ["Option 1", "Option 2", "Option 3"])
        st.write(f"Selected options: {option2}")
        st.markdown("---")
        # SelectMultiple
        st.subheader("SelectMultiple")
        options = st.multiselect("Select Multiple Options",
                                ["Option 1", "Option 2", "Option 3"])
        st.write(f"Selected options: {options}")
        st.markdown("---")

    def show_content_other(self):
        '''Show Page Content: Others.'''
        # Set Header
        self.setup_header("Other Elements")
        # Slider
        st.subheader("Slider")
        slider_val = st.slider("Select a value", 0, 100)
        st.write(f"Slider value: {slider_val}")
