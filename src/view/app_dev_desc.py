# app_dev_desc.py
import streamlit as st

def app_dev_desc():
 # Developer-related content
    st.markdown(''' 

        # Hugging Face Agent and Tools Code Overview
        
        ## Overview
        The provided Python code implements an interactive Streamlit web application that allows users to interact with various tools through the Hugging Face API. The app integrates Hugging Face models and tools, enabling users to perform tasks such as text generation, sentiment analysis, and more.
        
        ## Imports
        The code imports several external libraries and modules, including:
        - `streamlit`: For building the web application.
        - `os`: For interacting with the operating system.
        - `base64`, `io`, `Image` (from `PIL`), `AudioSegment` (from `pydub`), `IPython`, `sf`: For handling images and audio.
        - `requests`: For making HTTP requests.
        - `pandas`: For working with DataFrames.
        - `matplotlib.figure`, `numpy`: For visualization.
        - `altair`, `Plot` (from `bokeh.models`), `px` (from `plotly.express`), `pdk` (from `pydeck`): For different charting libraries.
        - `time`: For handling time-related operations.
        - `transformers`: For loading tools and agents.
        
        ## ToolLoader Class
        The `ToolLoader` class is responsible for loading tools based on their names. It has methods to load tools from a list of tool names and handles potential errors during loading.
        
        ## CustomHfAgent Class
        The `CustomHfAgent` class extends the base `Agent` class from the `transformers` module. It is designed to interact with a remote inference API and includes methods for generating text based on a given prompt.
        
        ## Tool Loading and Customization
        - Tool names are defined in the `tool_names` list.
        - The `ToolLoader` instance (`tool_loader`) loads tools based on the provided names.
        - The `CustomHfAgent` instance (`agent`) is created with a specified URL endpoint, token, and additional tools.
        - New tools can be added by appending their names to the `tool_names` list.
        
        ## Streamlit App
        The Streamlit app is structured as follows:
        1. Tool selection dropdown for choosing the inference URL.
        2. An expander for displaying tool descriptions.
        3. An expander for selecting tools.
        4. Examples and instructions for the user.
        5. A chat interface for user interactions.
        6. Handling of user inputs, tool selection, and agent responses.
        
        ## Handling of Responses
        The code handles various types of responses from the agent, including images, audio, text, DataFrames, and charts. The responses are displayed in the Streamlit app based on their types.
        
        ## How to Run
        1. Install required dependencies with `pip install -r requirements.txt`.
        2. Run the app with `streamlit run <filename.py>`.
        
        ## Notes
        - The code emphasizes customization and extensibility, allowing developers to easily add new tools and interact with the Hugging Face API.
        - Ensure proper configuration, such as setting the Hugging Face token as an environment variable.

      ''')

