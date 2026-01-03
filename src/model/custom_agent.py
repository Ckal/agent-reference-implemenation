"""
Module: custom_agent

This module provides a custom class, CustomHfAgent, for interacting with the Hugging Face model API.

Dependencies:
- time: Standard Python time module for time-related operations.
- requests: HTTP library for making requests.
- transformers: Hugging Face's transformers library for NLP tasks.
- utils.logger: Custom logger module for logging responses.

Classes:
- CustomHfAgent: A custom class for interacting with the Hugging Face model API.

Reasono for making this https://github.com/huggingface/transformers/issues/28217 
Based on https://github.com/huggingface/transformers/blob/main/src/transformers/tools/agents.py

"return_full_text": False,

"""

import time
import requests
from transformers import Agent
#from transformers.tools.prompts import CHAT_MESSAGE_PROMPT

CHAT_MESSAGE_PROMPT = """
Human: <<task>>

Assistant: """

from utils.logger import log_response
    
from transformers import  AutoTokenizer


class CustomHfAgent(Agent):
    """A custom class for interacting with the Hugging Face model API."""




    def __init__(self, url_endpoint, token, chat_prompt_template=None, run_prompt_template=None, additional_tools=None, input_params=None):
        """
        Initialize the CustomHfAgent.

        Args:
        - url_endpoint (str): The URL endpoint for the Hugging Face model API.
        - token (str): The authentication token required to access the API.
        - chat_prompt_template (str): Template for chat prompts.
        - run_prompt_template (str): Template for run prompts.
        - additional_tools (list): Additional tools for the agent.
        - input_params (dict): Additional parameters for input.

        Returns:
        - None
        """
        super().__init__(
            chat_prompt_template=chat_prompt_template,
            run_prompt_template=run_prompt_template,
            additional_tools=additional_tools,
        )
        self.url_endpoint = url_endpoint
        self.token = token
        self.input_params = input_params

    def generate_one(self, prompt, stop):
        """
        Generate one response from the Hugging Face model.

        Args:
        - prompt (str): The prompt to generate a response for.
        - stop (list): A list of strings indicating where to stop generating text.

        Returns:
        - str: The generated response.
        """
        headers = {"Authorization": "Bearer " +self.token}
        max_new_tokens = self.input_params.get("max_new_tokens", 192)
        parameters = {"max_new_tokens": max_new_tokens, "return_full_text": False, "stop": stop, "padding": True, "truncation": True}
        inputs = {
            "inputs": prompt,
            "parameters": parameters,
        }
        print(inputs)
        try:
            response = requests.post(self.url_endpoint, json=inputs, headers=headers, timeout=300)
        except requests.Timeout:
            pass
        except requests.ConnectionError:
            pass
        if response.status_code == 429:
            log_response("Getting rate-limited, waiting a tiny bit before trying again.")
            time.sleep(1)
            return self.generate_one(prompt, stop)
        elif response.status_code != 200:
            raise ValueError(f"Errors {inputs} {response.status_code}: {response.json()}")
        log_response(response)
        result = response.json()[0]["generated_text"]
        for stop_seq in stop:
            if result.endswith(stop_seq):
                return result[: -len(stop_seq)]
        return result
###
    ### 
    ### https://github.com/huggingface/transformers/blob/main/src/transformers/tools/prompts.py -> run chat_template.txt 
    ### https://huggingface.co/datasets/huggingface-tools/default-prompts/blob/main/chat_prompt_template.txt
    ###
    def format_prompt(self, task, chat_mode=False):

        checkpoint = "bigcode/starcoder"
        tokenizer = AutoTokenizer.from_pretrained(checkpoint, token = self.token)
        #model = AutoModelForCausalLM.from_pretrained(checkpoint)  # You may want to use bfloat16 and/or move to GPU here

 

        description = "\n".join([f"- {name}: {tool.description}" for name, tool in self.toolbox.items()])
        
        if chat_mode:
            if self.chat_history is None:
                print("no histroy yet ")
                prompt = self.chat_prompt_template.replace("<<all_tools>>", description)
                prompt += CHAT_MESSAGE_PROMPT.replace("<<task>>", task)

                messages = [
                    {
                        "role": "user",
                        "content": prompt,
                    } 
                ]
                print("tokenized "+tokenizer.apply_chat_template(messages, add_generation_prompt=True, tokenize=False))
            #    prompt = tokenizer.apply_chat_template(messages, add_generation_prompt=True, tokenize=False)
            else:
                print(" chat histroy ")
                print(self.chat_history)
                prompt = self.chat_history
                prompt += CHAT_MESSAGE_PROMPT.replace("<<task>>", task)
                messages = [
                    {
                        "role": "user",
                        "content": prompt,
                    } 
                ]
                print("tokenized "+tokenizer.apply_chat_template(messages, add_generation_prompt=True, tokenize=False))

          #      prompt = tokenizer.apply_chat_template(messages, add_generation_prompt=True, tokenize=False)
          ##  prompt 
        else:
            print("else block not chat mode ")
            prompt = self.run_prompt_template.replace("<<all_tools>>", description)
            prompt = prompt.replace("<<prompt>>", task)
            messages = [
                    {
                        "role": "user",
                        "content": prompt,
                    } 
                ]
            print("tokenized "+tokenizer.apply_chat_template(messages, add_generation_prompt=True, tokenize=False))

           # prompt = tokenizer.apply_chat_template(messages, add_generation_prompt=True, tokenize=False)
        print("formatted propmpt ---- " + prompt)
        return prompt 