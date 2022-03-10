import os

# Load PubNub Service
from pubnub.callbacks import SubscribeCallback
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

from typing import Callable

from src.types import Message

PUBNUB_PUBLISH_KEY = os.getenv('PUBNUB_PUBLISH_KEY')
PUBNUB_SUBSCRIBE_KEY = os.getenv('PUBNUB_SUBSCRIBE_KEY')
PUBNUB_SECRET_KEY = os.getenv('PUBNUB_SECRET_KEY')
PUBNUB_UUID = os.getenv('PUBNUB_UUID')
PUBNUB_CHANNEL = os.getenv('PUBNUB_CHANNEL')
PUBNUB_IDENTIFIER = os.getenv('PUBNUB_IDENTIFIER')

# Init PubNub Service
pnconfig = PNConfiguration()
pnconfig.subscribe_key = PUBNUB_SUBSCRIBE_KEY
pnconfig.publish_key = PUBNUB_PUBLISH_KEY
pnconfig.uuid = PUBNUB_UUID
pubnub = PubNub(pnconfig)
# pubnub.add_listener(OnReceiveEvent())

def publish_callback(envelope, status):
    if not status.is_error():
        pass
    else:
        pass

class OnReceiveEvent(SubscribeCallback):
    def __init__(self, on_message_callback: Callable):
        self.on_message_callback = on_message_callback

    def message(self, pubnub, message):
        publisher = message.publisher

        # Ignore own messages
        if publisher == PUBNUB_UUID:
            return;

        # Ignore if not the intended recipient
        if message.message["destination"] != PUBNUB_IDENTIFIER:
            return

        if self.on_message_callback:
            received_message : Message = message.message
            payload = self.on_message_callback(received_message)

            # Send response if there is any
            if payload:
                response: Message = {
                    "id": message.message["id"],
                    "source": PUBNUB_IDENTIFIER,
                    "destination": message.message["source"],
                    "payload": payload
                }
                pubnub.publish().channel(PUBNUB_CHANNEL).message(response).pn_async(publish_callback)

pubnub.subscribe().channels(PUBNUB_CHANNEL).execute()
