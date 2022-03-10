# Load Environment Variables
from dotenv import load_dotenv
load_dotenv()

# Message Type
from src.types import Message

# Chat Engine
from src.engines.chat.chat_engine import ChatEngine
chat_engine = ChatEngine("Siri")

# PubNub Service
from src.services.pubnub.service import pubnub, OnReceiveEvent

# Main
def on_message(message: Message):
    reply = chat_engine.generate_reply(message["payload"])
    if reply:
        return reply
    return

# Initialize listener
pubnub.add_listener(OnReceiveEvent(on_message))

print("Started listener")