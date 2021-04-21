from flask import Flask, jsonify
import time
import datetime

app = Flask(__name__)

db = [
    {
        'name': 'Nick',
        'text': 'Hello!',
        'time': time.time()
    },
    {
        'name': 'Ivan',
        'text': 'Hello, Nick!',
        'time': time.time()
    },
]

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/status")
def status():
    return jsonify(
        {
            'status': True,
            'name': 'iMess',
            'time': time.time(),
            'time2': time.asctime(),
            'time3': datetime.datetime.now(),
            'time4': datetime.datetime.now().isoformat(),
            'time5': datetime.datetime.fromtimestamp(time.time()),
            'time6': datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M'),
        }
    )

app.run()