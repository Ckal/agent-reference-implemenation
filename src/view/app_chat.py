"""
Module: app_chat

This module defines the app_chat function for managing user interactions in the chat interface.

Dependencies:
- streamlit: The Streamlit library for building web applications.
- pandas: Library for data manipulation and analysis.
- PIL: Python Imaging Library for image processing.
- pydub: Library for audio manipulation.
- controller: Module providing the Controller class for handling user submissions and managing conversations.

Functions:
- app_chat: Function for managing user interactions in the chat interface.
"""

import streamlit as st
import pandas as pd
from PIL import Image
from pydub import AudioSegment
from controller import Controller

def app_chat(controller):
    """
    Function for managing user interactions in the chat interface.

    Args:
    - controller (Controller): An instance of the Controller class for handling user submissions and managing conversations.

    Returns:
    - None
    """
    agent_config = controller.agent_config

    # Chat code (user input, agent responses, etc.)
    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.markdown("Hello there! How can I assist you today?")

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if user_message := st.chat_input("Enter message"):
        st.chat_message("user").markdown(user_message)
        st.session_state.messages.append({"role": "user", "content": user_message, "avatar": "🤗"})

        response = ""
        chat_response = ""
        with st.spinner('Please stand by ...'):
            response = controller.handle_submission(user_message)

        with st.chat_message("assistant"):
            if response is None:
                chat_response = controller.handle_submission_chat(user_message, response)
                st.write(chat_response)
            elif isinstance(response, Image.Image):
                agent_config.image = response
                chat_response = controller.handle_submission_chat(user_message, "No context. Created an image.")
                st.write(chat_response)
                st.image(response)
            elif isinstance(response, AudioSegment):
                agent_config.audio = response
                chat_response = controller.handle_submission_chat(user_message, "Agent Tool created audio file.")
                st.write(chat_response)
                st.audio(response)
            elif isinstance(response, int): 
                chat_response = controller.handle_submission_chat(user_message, response)
                st.write(chat_response)
                st.markdown(response)
            elif isinstance(response, str):
                if "emojified_text" in response: 
                    chat_response = controller.handle_submission_chat(user_message, "Agent Tool created the text with emojis.")
                    st.write(chat_response)
                    st.markdown(f"{response['emojified_text']}")
                else:
                    chat_response = controller.handle_submission_chat(user_message, response)
                    st.write(chat_response)
                    st.markdown(response)
            elif isinstance(response, list):
                chat_response = controller.handle_submission_chat(user_message, "Agent Tool produced a list")
                for item in response:
                    st.markdown(item)  # Assuming the list contains strings
                st.write(chat_response)
            elif isinstance(response, pd.DataFrame):
                chat_response = controller.handle_submission_chat(user_message, "Agent Tool produced a pd.DataFrame")
                st.write(chat_response) 
                st.dataframe(response)
            elif isinstance(response, pd.Series):
                chat_response = controller.handle_submission_chat(user_message, "Agent Tool produced a pd.Series")
                st.write(chat_response) 
                st.table(response.iloc[0:10])
            elif isinstance(response, dict):
                chat_response = controller.handle_submission_chat(user_message, "Agent Tool produced a dict")
                st.write(chat_response) 
                st.json(response)
            else:
                st.warning("Unrecognized response type. Please try again. e.g. Generate an image of a flying horse.")

        st.session_state.messages.append({"role": "assistant", "content": chat_response, "avatar": "🦖"})
        st.session_state.messages.append({"role": "assistant", "content": response, "avatar": "🤖"})
              
"""          elif isinstance(response, st.graphics_altair.AltairChart):
                chat_respone = controller.handle_submission_chat(user_message, "Agent Tool produced a st.graphics_altair.AltairChart")
                st.write(chat_respone) 
                st.altair_chart(response)
            elif isinstance(response, st.graphics_bokeh.BokehChart):
                chat_respone = controller.handle_submission_chat(user_message, "Agent Tool produced a st.graphics_bokeh.BokehChart")
                st.write(chat_respone) 
                st.bokeh_chart(response)
            elif isinstance(response, st.graphics_graphviz.GraphvizChart):
                chat_respone = controller.handle_submission_chat(user_message, "Agent Tool produced a st.graphics_graphviz.GraphvizChart")
                st.write(chat_respone) 
                st.graphviz_chart(response)
            elif isinstance(response, st.graphics_plotly.PlotlyChart):
                chat_respone = controller.handle_submission_chat(user_message, "Agent Tool produced a st.graphics_plotly.PlotlyChart")
                st.write(chat_respone) 
                st.plotly_chart(response)
            elif isinstance(response, st.graphics_pydeck.PydeckChart):
                chat_respone = controller.handle_submission_chat(user_message, "Agent Tool produced a  st.graphics_pydeck.PydeckChart")
                st.write(chat_respone) 
                st.pydeck_chart(response)
            elif isinstance(response, matplotlib.figure.Figure):
                chat_respone = controller.handle_submission_chat(user_message, "Agent Tool produced a matplotlib.figure.Figure")
                st.write(chat_respone) 
                st.pyplot(response)
            elif isinstance(response, st.graphics_vega_lite.VegaLiteChart):
                chat_respone = controller.handle_submission_chat(user_message, "Agent Tool produced a VegaLiteChart")
                st.write(chat_respone) 
                st.vega_lite_chart(response)  """

  
