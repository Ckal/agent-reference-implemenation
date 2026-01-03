"""
Module: tool_loader

This module defines the ToolLoader class for loading tools.

Dependencies:
- logging: Standard Python logging library for logging messages.
- transformers: Library for natural language processing with pre-trained models.
- utils.logger: Module providing logging functionalities.
- utils.tool_config: Module providing tool_names for configuration.

Classes:
- ToolLoader: A class for loading tools.
"""

import logging
from transformers import load_tool
from utils.logger import log_response  # Import the logger
from utils.tool_config import tool_names   

class ToolLoader:
    """
    A class for loading tools.
    """
    def __init__(self, tool_names):
        """
        Initializes an instance of the ToolLoader class.

        Args:
        - tool_names (list): A list of tool names to load.

        Returns:
        - None
        """
        self.tools = self.load_tools(tool_names)

    def load_tools(self, tool_names):
        """
        Loads tools based on the provided tool names.

        Args:
        - tool_names (list): A list of tool names to load.

        Returns:
        - list: A list of loaded tools.
        """
        loaded_tools = []
        for tool_name in tool_names:
            try:
                tool = load_tool(tool_name)
                loaded_tools.append(tool)
            except Exception as e:
                log_response(f"Error loading tool '{tool_name}': {e}")
        return loaded_tools
