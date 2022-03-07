# Typing
from typing import TypedDict, Optional

# ML Libraries
import numpy as np
import pickle

# Parsing Time
from ctparse import ctparse
from datetime import datetime

from src.engines.chat.response import Intent

model_filename = "./models/attendance_classifier.pickle"
classifier = pickle.load(open(model_filename, 'rb'))
classes = classifier['classes']


def classify_intent(message: str) -> Optional[Intent]:
    prediction = classifier['model'].predict_proba([message])[0]
    predicted_class = np.where(prediction == np.amax(prediction))
    idx = predicted_class[0][0]

    confidence = float(prediction[idx])
    result = classes[idx]

    intent : Intent = { "intent": result, "confidence": confidence, "data": {}}
    return intent