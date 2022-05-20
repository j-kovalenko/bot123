from flask import Flask, request
import requests
import os
from currency import Currency
from random import choice as ch
from secret_files import TOKEN, WEATHER_TOKEN
# токен тг-бота можно получить у botfather, для погоды - на weatherstack.com

app = Flask(__name__)


def send(id, message):
    token = TOKEN
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    data = {"chat_id": id, "text": message}
    requests.post(url, data=data)


@app.route('/', methods=['GET', 'POST'])
def bot():
    print(request.json)
    id = request.json['message']['chat']['id']
    if 'text' in request.json['message']:
        text = request.json['message']['text']
        if text == '/start':
            send(id, 'Привет!\nПришли мне /currency для получения курса валют или /weather для получения погоды!')
        elif text == '/currency':
            send(id, "Подождите...")
            currency = Currency()
            json_cur = currency.check_currency()
            reply = f"EUR: {json_cur['eur']}₽\nUSD: {json_cur['usd']}₽\nBGN: {json_cur['bgn']}₽\nTRY: {json_cur['try']}₽\nпо ЦБ РФ"
            send(id, reply)
        elif text == '/weather':
            reply = ''
            for city in ['Moscow', 'Sofia', 'Antalya']:
                params = {"access_key": "4757691b2af74089ebb6d2b398420b9e", "query": city}
                api_result = requests.get('http://api.weatherstack.com/current', params)
                api_response = api_result.json()
                reply += f"{city}: {api_response['current']['temperature']}°\n"
            send(id, reply)
        elif '/random' in text:
            if len(text.split()) == 1:
                num(id)
            else:
                args = text.split()[1:]
                try:
                    if len(args) > 2:
                        send(id, 'error: too many args')
                    elif len(args) == 2:
                        num(id, r=[0, int(args[1]) + 1])
                    elif len(args) == 3:
                        n1 = int(args[1])
                        n2 = int(args[2])
                        if n2 > n1:
                            num(id, r=[n1, n2])
                        else:
                            send(id, "error: number2 less that number1")
                except ValueError:
                    send(id, 'error: wrong literal')
        elif text == '/caesar':
            pass
        else:
            send(id, f"you wrote: {text}\nreversed: {text[::-1]}")
    else:
        send(id, 'я пока не понимаю этот формат')
    return {"ok": True}


def notification():
    f = open('users.txt', 'r', encoding='utf-8')
    for line in f.readlines():
        for id in line.split(', '):
            currency = Currency()
            json_cur = currency.check_currency()
            reply = ''
            for city in ['Moscow', 'Sofia', 'Antalya']:
                params = {"access_key": WEATHER_TOKEN, "query": city}
                api_result = requests.get('http://api.weatherstack.com/current', params)
                api_response = api_result.json()
                reply += f"{city}: {api_response['current']['temperature']}°\n"
            message = f'''Доброе утро!
Сегодня такие курсы валют:
EUR: {json_cur['eur']}₽\nUSD: {json_cur['usd']}₽\nBGN: {json_cur['bgn']}₽\nTRY: {json_cur['try']}₽\nпо ЦБ РФ
Также сегодня вот такая погода:\n''' + reply
            send(id, message)
    print('done')


def num(id, r=[]):
    if len(r) == 2:
        n = ch(range(r[0], r[1]))
    else:
        n = ch(range(0, 1000000))
    send(id, f"random number: {n}")


def caesar(id, y, x):
    x = x.replace('ё', 'е').replace('Ё', 'Е')
    res = ''
    for i in range(0, len(x)):
        if ord('А') <= ord(x[i]) <= ord('Я'):
            b = ((ord(x[i]) + y - ord('А')) % 32) + ord('А')
            res += chr(b)
        elif ord('а') <= ord(x[i]) <= ord('я'):
            a = ((ord(x[i]) + y - ord('а')) % 32) + ord('а')
            res += chr(a)
        elif ord('A') <= ord(x[i]) <= ord('Z'):
            b = ((ord(x[i]) + y - ord('A')) % 26) + ord('A')
            res += chr(b)
        elif ord('a') <= ord(x[i]) <= ord('z'):
            a = ((ord(x[i]) + y - ord('a')) % 26) + ord('a')
            res += chr(a)
        else:
            res += x[i]
    send(id, res)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)