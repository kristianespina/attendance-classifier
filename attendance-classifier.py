from celery import Celery
# ML Libraries
import numpy as np
import pickle

app = Celery('tasks',
    broker='redis://host.docker.internal:6379',
    backend='redis://host.docker.internal:6379'
)

model_filename = "models/attendance_classifier.pickle"
classifier = pickle.load(open(model_filename, 'rb'))

@app.task
def classify(command):
    classes = classifier['classes']
    prediction = classifier['model'].predict_proba([command])[0]
    predicted_class = np.where(prediction == np.amax(prediction))
    idx = predicted_class[0][0]
    result = { "type": classes[idx], "confidence": float(prediction[idx]) }
    return result