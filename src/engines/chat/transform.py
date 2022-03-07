from src.engines.chat.response import Intent
from src.engines.chat.transformers.attendance import transform_attendance

def transform_intent(intent: Intent, message: str) -> Intent:
    if "attendance" in intent["intent"]:
        return transform_attendance(intent, message)

    # Do nothing
    return intent