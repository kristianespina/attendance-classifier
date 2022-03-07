from typing import TypedDict

class Intent(TypedDict):
    intent: str
    confidence: float
    data: dict

class Response(TypedDict):
    intent: str
    response: str
    confidence: float
    data: dict

def create_response(intent: str, response: str, confidence: float, data: dict):
    return {
        "intent": intent,
        "response": response,
        "confidence": confidence,
        "data": data
    }