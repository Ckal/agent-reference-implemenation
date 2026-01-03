"""
Module: app_agent_config

This module defines the AgentConfig class, which holds configuration settings for the agent.

Dependencies:
- utils.tool_loader: Module providing the ToolLoader class for loading tools.
- utils.tool_config: Module providing tool_names for configuration.

Classes:
- AgentConfig: A class for managing configuration settings for the agent.
"""

from utils.tool_loader import ToolLoader  # Importing ToolLoader class from utils.tool_loader module
from utils.tool_config import tool_names   # Importing tool_names from utils.tool_config module

class AgentConfig:
    """
    A class for managing configuration settings for the agent.
    """
    def __init__(self):
        """
        Initializes an instance of the AgentConfig class.

        Attributes:
        - url_endpoint (str): The URL endpoint for the agent.
        - tool_checkboxes (list): Checkboxes for available tools.
        - s_tool_checkboxes (list): Selected checkboxes for tools.
        - image (list): Image data.
        - document (str): Document data.
        - log_enabled (bool): Flag indicating whether logging is enabled.
        - context (str): Context data.
        - tool_loader (ToolLoader): Instance of ToolLoader class for loading tools.
        - agent_urls (list): URLs for different agents.
        """
        self.url_endpoint = ""
        self.tool_checkboxes = []
        self.s_tool_checkboxes = []
        self.image = []
        self.document = ""
        self.log_enabled = False
        self.context = ""
        self.tool_loader = ToolLoader(tool_names)
        self.agent_urls = [
            "https://api-inference.huggingface.co/models/bigcode/starcoder",
            "https://api-inference.huggingface.co/models/OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5",
            "https://api-inference.huggingface.co/models/gpt2"
        ]
