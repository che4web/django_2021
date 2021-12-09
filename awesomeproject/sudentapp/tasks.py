
from sudentapp.models import Dish
from awesomeproject.celery import app
import time
import channels.layers
from asgiref.sync import async_to_sync

@app.task
def some_task(text):
    channel_layer = channels.layers.get_channel_layer()
    print("==================== before sleep")
    time.sleep(5)
    print("====================hello-from celery"+text)
    async_to_sync(channel_layer.send)('test_channel', {'type': 'hello from task'})

