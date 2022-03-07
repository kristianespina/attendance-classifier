import random
from typing import List, Optional, TypedDict

class Dialog(TypedDict):
    language: str
    intent: str
    responses: List[str]

def load_dialogs() -> List[Dialog]:
    dialogs : List[Dialog] = [
        # Time In
        { "language": "en", "intent": "attendance.timein.past",  "responses": ["🤩 You have successfully timed in <relative_time>."]},
        { "language": "en", "intent": "attendance.timein.present",  "responses": ["You have successfully timed in 🍻"]},
        { "language": "en", "intent": "attendance.timein.future",  "responses": ["Okay! We'll wait for you <relative_time> 👋"]},
        # Time Out
        { "language": "en", "intent": "attendance.timeout.past",  "responses": ["Understood! You were out <relative_time>."]},
        { "language": "en", "intent": "attendance.timeout.present",  "responses": ["You have successfully timed out. 👋"]},
        { "language": "en", "intent": "attendance.timeout.future",  "responses": ["You would have timed out <relative_time>."]},
        # Break
        { "language": "en", "intent": "attendance.break.past",  "responses": ["Got it! You were on a mukbang break <relative_time> :shallow_pan_of_food:"]},
        { "language": "en", "intent": "attendance.break.present",  "responses": ["Please enjoy your break :coffee:"]},
        { "language": "en", "intent": "attendance.break.future",  "responses": ["Yosh! You'll be on a break <relative_time> 🍻"]},
        # Resume
        { "language": "en", "intent": "attendance.resume.past",  "responses": ["Oops! You were back na pala <relative_time> 😅"]},
        { "language": "en", "intent": "attendance.resume.present",  "responses": ["🥳 🎉 We're glad you're back!"]},
        { "language": "en", "intent": "attendance.resume.future",  "responses": ["We'll wait for you to be back <relative_time> 🥺"]},
        # Default
        { "language": "en", "intent": "default",  "responses": ["I'm sorry but I couldn't understand you. Please rephrase your query"]},
    ]

    return dialogs

def get_responses_by_intent(intent: str, language: str = "en" ) -> List[str]:
    try:
        dialogs = load_dialogs()
        dialog = next(d for d in dialogs if d["intent"] == intent and d["language"] == language)

        return dialog["responses"]
    except:
        # Return default dialog
        dialog = next(d for d in dialogs if d["intent"] == "default" and d["language"] == language)
        return dialog["responses"]

def get_response_by_intent(intent: str, language: str = "en" ) -> List[str]:
    responses = get_responses_by_intent(intent, language)
    return random.choice(responses)