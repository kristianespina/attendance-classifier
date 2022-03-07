# Parsing Time
from ctparse import ctparse
from datetime import datetime, timezone
import arrow

from src.models.attendance.predict import Intent

LOCAL_TIMEZONE = datetime.now(timezone.utc).astimezone().tzinfo

def transform_attendance(intent: Intent, message: str) -> Intent:
    return get_relative_time(intent, message)

def get_relative_time(_intent: Intent, message: str) -> Intent:
    intent = _intent

    # Parse if there is a date or timestamp attached in the message
    now = datetime.now().replace(tzinfo=LOCAL_TIMEZONE)
    timestamp = now
    try:
        # Check if there is an attached timestamp
        timestamp = ctparse(message, ts=now).resolution.dt

    except:
        timestamp = now
    

    timestamp = timestamp.replace(tzinfo=LOCAL_TIMEZONE)
    time_difference = (timestamp - now).total_seconds()

    # Categorize the time as past if -2 minutes
    if time_difference < -120:
        intent["intent"] += ".past"
    elif time_difference > 120:
        intent["intent"] += ".future"
    else:
        intent["intent"] += ".present"

    # Append timestamp data
    relative_time = arrow.get(timestamp.isoformat()).humanize()

    intent["data"]["relative_time"] = relative_time
    intent["data"]["timestamp"] = timestamp.isoformat()
    
    return intent