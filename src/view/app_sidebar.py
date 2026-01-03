"""
Module: app_sidebar

This module defines the app_sidebar function for managing the sidebar interface.

Dependencies:
- streamlit: The Streamlit library for building web applications.
- PIL: Python Imaging Library for image processing.
- numpy: Library for numerical computing.
- pandas: Library for data manipulation and analysis.

Functions:
- app_sidebar: Function for managing the sidebar interface.
- configure: Function for configuring the agent and tools.
- content_and_context: Function for setting the content and context.
"""

import streamlit as st
from PIL import Image 
import numpy as np
import pandas as pd

def app_sidebar(controller):
    """
    Function for managing the sidebar interface.

    Args:
    - controller (Controller): An instance of the Controller class for handling user submissions and managing conversations.

    Returns:
    - None
    """
    with st.sidebar:
        st.header("Set Tools and Option. ")
        with st.expander("Configure the agent and tools"):
            configure(controller.agent_config)
        with st.expander("Set the Content and Context"):
            content_and_context(controller.agent_config)

def configure(agent_config):
    """
    Function for configuring the agent and tools.

    Args:
    - agent_config (AgentConfig): An instance of the AgentConfig class for managing configuration settings for the agent.

    Returns:
    - None
    """
    st.markdown("Change the agent's configuration here.")

    agent_config.url_endpoint = st.selectbox("Select Inference URL", agent_config.agent_urls)
    
    agent_config.log_enabled = st.checkbox("Enable Logging")

    agent_config.s_tool_checkboxes = [st.checkbox(f"{tool.name} --- {tool.description} ") for tool in agent_config.tool_loader.tools]

def content_and_context(agent_config):
    """
    Function for setting the content and context.

    Args:
    - agent_config (AgentConfig): An instance of the AgentConfig class for managing configuration settings for the agent.

    Returns:
    - None
    """
    agent_config.context = st.text_area("Context")

    agent_config.image = st.camera_input("Take a picture")

    img_file_buffer = st.file_uploader('Upload a PNG image', type='png')

    if img_file_buffer is not None:
        image_raw = Image.open(img_file_buffer)
        agent_config.image = np.array(image_raw)
        st.image(agent_config.image)
        
    uploaded_file = st.file_uploader("Choose a pdf", type='pdf')
    if uploaded_file is not None:
        agent_config.document = uploaded_file.getvalue()  
        st.write(agent_config.document)
        
    uploaded_txt_file = st.file_uploader("Choose a txt", type='txt')
    if uploaded_txt_file is not None:
        agent_config.document = uploaded_txt_file.getvalue() 
        st.write(agent_config.document)
        
    uploaded_csv_file = st.file_uploader("Choose a csv", type='csv')
    if uploaded_csv_file is not None:
        agent_config.document = uploaded_csv_file.getvalue() 
        st.write(agent_config.document)
                    
    uploaded_csv_file = st.file_uploader("Choose audio", type='wav')
    if uploaded_csv_file is not None:
        agent_config.document = uploaded_csv_file.getvalue() 
        st.write(agent_config.document)
        
    uploaded_csv_file = st.file_uploader("Choose video", type='avi')
    if uploaded_csv_file is not None:
        agent_config.document = uploaded_csv_file.getvalue() 
        st.write(agent_config.document)
                
