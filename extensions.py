import requests
import json
from config import keys
class ConvertionException(Exception):
    pass


class CryptoCovreter:
    @staticmethod
    def covert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Валюты одинаковые {base}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать колличество{amount}')



