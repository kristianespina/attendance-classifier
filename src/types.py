from typing import TypedDict, Any

class Message(TypedDict):
    id: str
    source: str
    destination: str
    payload: Any