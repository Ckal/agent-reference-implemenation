"""
Module: main

This module initializes the Streamlit app and sets up the user interface for interacting with the chatbot.

Dependencies:
- streamlit: The Streamlit library for building web applications.
- controller: Module providing the Controller class for handling user submissions and managing conversations.
- view.app_header: Module providing the app_header function for displaying the header section of the app.
- view.app_sidebar: Module providing the app_sidebar function for displaying the sidebar section of the app.
- view.app_chat: Module providing the app_chat function for displaying the main chat interface.

Usage:
- Run the Streamlit app using 'streamlit run main.py' command in the terminal.
"""

import streamlit as st
from controller import Controller
from view.app_header import app_header
from view.app_sidebar import app_sidebar
from view.app_chat import app_chat

# Streamlit configuration (holds the session and session history as well)
st.set_page_config(
    page_title="Custom Transformers can really do anything...",
    page_icon="👋" 
)

# Create an instance of Controller with agentConfig ## holds all data, config, and settings
controller = Controller()

# Sidebar for context & config
app_sidebar(controller)

# App header
app_header(controller)

# Main content - the chat interface
app_chat(controller)
