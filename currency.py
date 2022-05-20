import requests  # Модуль для обработки URL
from bs4 import BeautifulSoup  # Модуль для работы с HTML
import time  # Модуль для остановки программы
import smtplib  # Модуль для работы с почтой


# Основной класс
class Currency:
    # Ссылка на нужную страницу
    DOLLAR_RUB = 'https://is.gd/VDG2S6'
    EUR_RUB = 'https://is.gd/iqfO2R'
    BGN_RUB = 'https://is.gd/r7EI6n'
    TRY_RUB = 'https://is.gd/5htWFC'
    # Заголовки для передачи вместе с URL
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

    current_converted_price = 0

    def __init__(self):
        # Установка курса валюты при создании объекта
        self.current_converted_price = float(self.get_usd().replace(",", "."))

    # Метод для получения курса валюты
    def get_usd(self):
        # Парсим всю страницу
        full_pageusd = requests.get(self.DOLLAR_RUB, headers=self.headers)

        # Разбираем через BeautifulSoup
        soup = BeautifulSoup(full_pageusd.content, 'html.parser')

        # Получаем нужное для нас значение и возвращаем его
        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
        return convert[0].text

    def get_eur(self):
        # Парсим всю страницу
        full_pageusd = requests.get(self.EUR_RUB, headers=self.headers)

        # Разбираем через BeautifulSoup
        soup = BeautifulSoup(full_pageusd.content, 'html.parser')

        # Получаем нужное для нас значение и возвращаем его
        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
        return convert[0].text

    def get_bgn(self):
        # Парсим всю страницу
        full_pageusd = requests.get(self.BGN_RUB, headers=self.headers)

        # Разбираем через BeautifulSoup
        soup = BeautifulSoup(full_pageusd.content, 'html.parser')

        # Получаем нужное для нас значение и возвращаем его
        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
        return convert[0].text

    def get_try(self):
        # Парсим всю страницу
        full_pageusd = requests.get(self.TRY_RUB, headers=self.headers)

        # Разбираем через BeautifulSoup
        soup = BeautifulSoup(full_pageusd.content, 'html.parser')

        # Получаем нужное для нас значение и возвращаем его
        convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
        return convert[0].text

    # Проверка изменения валюты
    def check_currency(self):
        usd = float(self.get_usd().replace(",", "."))
        eur = float(self.get_eur().replace(",", "."))
        bgn = float(self.get_bgn().replace(",", "."))
        lir = float(self.get_try().replace(",", "."))
        return {"usd": usd, "eur": eur, "bgn": bgn, "try": lir}


if __name__ == "__main__":
    currency = Currency()
    print(currency.check_currency())
