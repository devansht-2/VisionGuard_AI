# backend/chatbot_handler.py

from chatbot_script import get_response

def chatbot_start(stage):
    return get_response(stage, "start")

def chatbot_reply(stage, user_message):
    return get_response(stage, user_message)