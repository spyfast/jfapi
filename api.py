import json
from datetime import datetime, timedelta

import requests

from config import api_url, token


# Проверка токена на валидность
def check_token(access_token):
    # Параметры запроса
    parameters = {
        'token': access_token
    }

    try:
        resp = requests.get(f'{api_url}/auth.check', parameters).json()

        if 'success' in json.dumps(resp):
            print('Токен валидный. Можно воркать')

        if 'error' in json.dumps(resp):
            print(f'У вас ошибка: {resp["error_msg"]}')

    except Exception as ex:
        print(f'Неизвестная ошибка: {ex}')

# Создание короткой ссылки
def create_short_link(url, short_name=None):
    # Параметры запроса
    parameters = {
        'link': url,
        'time': (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S'),
        'short' if short_name is not None else ''
        'token': token
    }

    try:
        resp = requests.get(f'{api_url}/reference.create.php', parameters).json()

        if 'success' in json.dumps(resp):
            print(f'Успешная генерация ссылки: {resp["link"]}')

        if 'error' in json.dumps(resp):
            print(f'У вас ошибка: {resp["error_msg"]}')
    except Exception as ex:
        print(f'Неизвестная ошибка: {ex}')


# Отправка письма на указанный эл. адрес
def send_to_mail(subject, msg, to_email):
    # Параметры запроса
    parameters = {
        'subject': subject,
        'message': msg,
        'email': to_email,
        'token': token
    }

    try:
        resp = requests.get(f'{api_url}/mailer.send.php', parameters).json()

        if 'success' in json.dumps(resp):
            print(f'Успешно отправлено сообщение на: {to_email}')
            return True

        if 'error' in json.dumps(resp):
            print(f'У вас ошибка: {resp["error_msg"]}')
            return False
    except Exception as ex:
        print(f'Неизвестная ошибка: {ex}')
        return False
