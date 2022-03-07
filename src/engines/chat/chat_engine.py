"""
    Chat Engine
"""
from typing import Optional
from src.engines.chat.dialog import get_response_by_intent
from src.engines.chat.response import Response, create_response
from src.engines.chat.tokens.hydrate import get_hydrated_response
from src.engines.chat.transform import transform_intent
from src.models.attendance.predict import classify_intent, Intent

class ChatEngine:
    def __init__(self, name: str):
        self.name = name
        # self.model = new Model()

    def generate_reply(self, message) -> Response:
        # Classify intention
        intent : Optional[Intent] = classify_intent(message)

        # intent is not defined / unknown
        if intent is None:
            response_object = create_response (
                "unknown",
                "No response",
                0.00,
                {}
            )
            return response_object
        
        # Transform intent
        transformed_intent = transform_intent(intent, message)
        
        # intent is defined -> get responses
        response = get_response_by_intent(intent["intent"], language="en") 

        # Hydrate tokens with data
        hydrated_response = get_hydrated_response(response, transformed_intent["data"])

        # Create response
        response_object = create_response(
            transformed_intent["intent"],
            hydrated_response,
            transformed_intent["confidence"],
            transformed_intent["data"]
        )

        return response_object
        
