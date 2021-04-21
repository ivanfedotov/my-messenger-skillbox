import requests
from flask import Flask, request, abort, jsonify
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

def countUsers():
    x = set()
    for e in db:
        x.add(e['name'])
    return len(x)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/status")
def status():
    return jsonify(
        {
            'status': True,
            'name': 'iMess',
            # 'time1': time.time(),
            # 'time2': time.asctime(),
            # 'time3': datetime.datetime.now(),
            # 'time4': datetime.datetime.now().isoformat(),
            # 'time5': datetime.datetime.fromtimestamp(time.time()),
            'time': datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M'),
            'messages': len(db),
            'users': countUsers(),
        }
    )

@app.route("/send", methods=['POST'])
def send_message():
    data = request.json

    if not isinstance(data, dict):
        return abort(400)
    if 'name' not in data or 'text' not in data:
        return abort(400)

    name = data['name']
    text = data['text']

    if not isinstance(name, str) or not isinstance(text, str):
        return abort(400)
    if name == '' or text == '':
        return abort(400)

    db.append({
        'name': name,
        'text': text,
        'time': time.time()
    })

    if text == '/info':
        db.append({
            'name': 'BOT',
            'text': 'I am bot, You are not bot!',
            'time': time.time()
        })

    return {'ok': True}

@app.route("/messages")
def get_messages():
    try:
        after = float(request.args['after'])
    except:
        return abort(400)
    messages = []
    for message in db:
        if message['time'] > after:
            messages.append(message)
    return {
        'messages': messages[:50]
    }

app.run()