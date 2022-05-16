from flask import Flask, request
import requests
from dotenv import load_dotenv
import os
from os.path import join, dirname

app = Flask(__name__)


def get_env(key):
    path = join(dirname(__file__), '.env')
    load_dotenv(path)
    return os.environ.get(key)


def send(id, message):
    token = get_env('TOKEN')
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    data = {"chat_id": id, "text": message}
    requests.post(url, data=data)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    print(request.json)
    id = request.json['message']['chat']['id']
    text = request.json['message']['text']
    send(id, f"you wrote: {text}\nreversed: {text[::-1]}")
    return {"ok": True}


if __name__ == '__main__':
    app.run()