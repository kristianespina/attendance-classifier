from celery import Celery
from src.engines.chat.chat_engine import ChatEngine

app = Celery('tasks',
    broker='redis://host.docker.internal:6379',
    backend='redis://host.docker.internal:6379'
    # broker='redis://127.0.0.1:6379',
    # backend='redis://127.0.0.1:6379'
)

chat_engine = ChatEngine("Siri")

@app.task
def get_response(message: str):
    return chat_engine.generate_reply(message)