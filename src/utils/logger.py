import logging #### todo add transformer logs
import streamlit as st
#from transformers.utils import logging
# Configure the logging settings for transformers
transformers_logger = logging.getLogger("transformers.tools.agents")
transformers_logger.setLevel(logging.INFO)  # Set the desired logging level

log_enabled = True


##################################### logger #################################

 


def log_response(response):
    if log_enabled:
        with st.chat_message("ai"):
            st.markdown("Agent Response\n {}".format(response))
    print(response)

# Custom logging handler to append log messages to the chat
class ChatHandler(logging.Handler):
    def __init__(self):
        super().__init__()


    def emit(self, record):
        log_message = self.format(record)
        #with st.chat_message("ai"):
        st.markdown(f"Log: {log_message}")
        with st.chat_message("ai"):
            st.markdown("Agent Response\n {}".format(record))

# Add the custom handler to the transformers_logger
chat_handler = ChatHandler()
transformers_logger.addHandler(chat_handler)



import socket
import threading
import logging

class IRCLogger:
    def __init__(self, server, port, nickname, channel):
        self.server = server
        self.port = port
        self.nickname = nickname
        self.channel = channel
        self.socket = socket.socket()
        self.socket.connect((self.server, self.port))

        # Configure logging
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        # Create a stream handler and set its level to INFO
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)

        # Create a formatter and set the format
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        handler.setFormatter(formatter)

        # Add the handler to the logger
        self.logger.addHandler(handler)

        # Join the IRC channel
        self.join_channel()

        # Start a thread to handle incoming messages
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.start()

    def send_message(self, message):
        self.socket.send(bytes("PRIVMSG {} :{}\r\n".format(self.channel, message), "UTF-8"))

    def join_channel(self):
        self.socket.send(bytes("NICK {}\r\n".format(self.nickname), "UTF-8"))
        self.socket.send(bytes("USER {} 0 * :{}\r\n".format(self.nickname, self.nickname), "UTF-8"))
        self.socket.send(bytes("JOIN {}\r\n".format(self.channel), "UTF-8"))

    def receive_messages(self):
        while True:
            data = self.socket.recv(4096).decode("UTF-8")
            if data.startswith("PING"):
                self.socket.send(bytes("PONG {}\r\n".format(data.split()[1]), "UTF-8"))
            else:
                if not data.startswith("-"):
                    self.logger.info(data)

    def log_message(self, message):
        self.logger.info(message)
        self.send_message(message)

if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(level=logging.INFO)

    server = "irc.efnet.org"
    port = 6667
    nickname = "HFLogBB"
    channel = "#hflogs"

#    logger = IRCLogger(server, port, nickname, channel)
#    logger.log_message("This is a test log message from the IRC logger.")
