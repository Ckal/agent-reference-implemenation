# app_description.py

import streamlit as st

def app_user_desc():
    st.markdown('''
        # Hugging Face Agent and Tools App
                
        ## Description
        Welcome to the Hugging Face Agent and Tools app! This app provides an interactive interface for utilizing various tools through the Hugging Face API. You can choose an inference URL and select from a variety of tools to perform different tasks.
        
        ## Examples
        1. **Generate a Random Character**:
           - Choose the desired URL and the 'Random Character Tool'.
           - Then type 'Genarate random Character' 
           
        2. **Sentiment Analysis**:
           - Choose the desired URL and the 'Sentiment Analysis Tool'.
           - Sample: What is the sentiment for "Hello, I am happy"?
        
        3. **Word Count**:
           - Choose the desired URL and the 'Word Counter Tool'.
           - Sample: Count the words in "Hello, I am Christof".
        Other samples:
        
        - Generate a random character. 
        - What is the sentiment for "Hello I am happy"
        - Count the words of "Hello I am Christof”
        - What is the most downloaded model for text2image
        - Use ner_tool to find the information in the following text:"Hello I am Christof.".
        - Download the text from https://docs.streamlit.io/get-started/installation
        - Scrape source code from https://docs.streamlit.io/get-started/installation
        - label for text="Hello I am Christof" classifies greeting
        
        ## Tools
        To interact with the tools, expand the section below to see tool descriptions and select the tools you want to use.
        
        Expand to see tool descriptions 
        
        ### Tool Descriptions
        - **random-character-tool:** Generates a random character.
        - **text-generation-tool:** Generates text based on a prompt.
        - **sentiment-tool:** Analyzes the sentiment of a given text.
        - **token-counter-tool:** Counts the tokens in a text.
        - **most-downloaded-model:** Provides information about the most downloaded model.
        - **rag-tool:** Utilizes Retrieval-Augmented Generation (RAG) for text generation.
        - **word-counter-tool:** Counts the words in a text.
        - **sentence-counter-tool:** Counts the sentences in a text.
        - **EmojifyTextTool:** Emojifies the given text.
        - **NamedEntityRecognitionTool:** Identifies named entities in a text.
        - **TextDownloadTool:** Downloads text from a given URL.
        - **source-code-retriever-tool:** Retrieves source code from a given URL.
        - **text-to-image:** Generates an image from text.
        - **text-to-video:** Generates a video from text.
        - **image-transformation:** Applies transformations to images.
        - **latent-upscaler-tool:** Upscales images using latent space.
         
        ## Usage
        1. Choose the desired inference URL from the dropdown.
        2. Expand the tool selection section and choose the tools you want to use.
        3. Enter a message in the chat input to interact with the Hugging Face Agent.
        4. View the assistant's responses, which may include images, audio, text, or other visualizations based on the selected tools.
        
        Feel free to explore and experiment with different tools to achieve various tasks!
    ''')
