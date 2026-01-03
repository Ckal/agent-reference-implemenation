"""
Module: controller

This module provides a Controller class for handling user submissions and managing conversations.

Dependencies:
- app_agent_config: Module providing the AgentConfig class for configuring agents.
- utils.logger: Module providing logging functionalities.
- model.custom_agent: Module providing the CustomHfAgent class for interacting with Hugging Face models.
- model.conversation_chain_singleton: Module providing the ConversationChainSingleton class for managing conversation chains.

Classes:
- Controller: A class for handling user submissions and managing conversations.
"""
import os
from app_agent_config import AgentConfig  # Importing AgentConfig class from app_agent_config module
from utils.logger import log_response, IRCLogger     # Importing log_response function from utils.logger module
from model.custom_agent import CustomHfAgent  # Importing CustomHfAgent class from model.custom_agent module
from model.conversation_chain_singleton import ConversationChainSingleton  # Importing ConversationChainSingleton class from model.conversation_chain_singleton module

import logging

logging.basicConfig(level=logging.INFO)

server = "irc.efnet.org"
port = 6667
nickname = "HFLogAAA"
channel = "#hflogs"

logger = IRCLogger(server, port, nickname, channel)
#logger.log_message("This is a test log message from the IRC logger.")

def cut_text_after_keyword(text, keyword):
    """
    Cuts text after the occurrence of a keyword.

    Args:
    - text (str): The text to be processed.
    - keyword (str): The keyword to search for in the text.

    Returns:
    - str: The processed text.
    """
    index = text.find(keyword)
    if index != -1:
        return text[:index].strip()
    return text

def get_text_after_last_occurrence(text, delimiter):
    """
    Retrieves the text after the last occurrence of the specified delimiter.

    Args:
    - text (str): The input text.
    - delimiter (str): The delimiter to search for.

    Returns:
    - str: The text after the last occurrence of the delimiter, or an empty string if the delimiter is not found.
    """
    last_index = text.rfind(delimiter)
    if last_index != -1:
        return text[last_index + len(delimiter):].strip()
    return ""


class Controller:
    """
    Controller class for handling user submissions and managing conversations.
    """
    def __init__(self):
        self.agent_config = AgentConfig()  # Initialize AgentConfig instance
       # logger.log_message("This is a test log message from the IRC logger.")


    image = []  # Class attribute for storing image data

    def handle_submission(self, user_message):
        """
        Handles user submission and interaction with the Hugging Face model.

        Args:
        - user_message (str): The message submitted by the user.

        Returns:
        - str: The response from the Hugging Face model.
        """
       # logger.log_message("This is a test log message from the IRC logger.")
        log_response("User input \n {}".format(user_message))
        log_response("selected_tools \n {}".format(self.agent_config.s_tool_checkboxes))
        log_response("url_endpoint \n {}".format(self.agent_config.url_endpoint))
        log_response("document \n {}".format(self.agent_config.document))
        log_response("image \n {}".format(self.agent_config.image))
        log_response("context \n {}".format(self.agent_config.context))

        selected_tools = [self.agent_config.tool_loader.tools[idx] for idx, checkbox in enumerate(self.agent_config.s_tool_checkboxes) if checkbox]

        agent = CustomHfAgent(
            url_endpoint=self.agent_config.url_endpoint,
            token=os.environ['HF_token'],
            additional_tools=selected_tools,
            input_params={"max_new_tokens": 192},
        )

        agent_response = agent.chat(user_message, document=self.agent_config.document, image=self.agent_config.image, context=self.agent_config.context)

        log_response("Agent Response\n {}".format(agent_response))

        return agent_response

    def handle_submission_chat(self, user_message, agent_response):
        """
        Handles user messages and responses in a conversation chain.

        Args:
        - user_message (str): The message submitted by the user.
        - agent_response (str): The response from the agent.

        Returns:
        - str: The response from the conversation chain.
        """
        agent_chat_bot = ConversationChainSingleton().conversation_chain("tmp")
        print(agent_chat_bot)
        print("------------ msg -----------------------")
        print(user_message + " ---- " )
        print("------------ /msg -----------------------")
        if agent_response is not None:
            msg = "[INST] You are a friendly chatbot who always responds to the user input in the style of a pirate. USER_INPUT:  "+user_message+" HINT: In a previous step the following was generated. use this to answer the user. AGENT_RESPONSE: "+ agent_response+" [/INST]"
            text = agent_chat_bot.predict(input=msg)
        else:
            msg = "[INST] You are a friendly chatbot who always responds to the user input in the style of a pirate. USER_INPUT:  "+user_message+"[/INST]"
            text = agent_chat_bot.predict(input=msg)
        print("----- msg----")
        print(msg)
        print("------------ text -----------------------")
        print(text)
        print("------------ /result -----------------------")
        result = get_text_after_last_occurrence(text, "AI: ")
        print(result)
        logger.log_message("Result: "+result+ " "+user_message)
        return result
