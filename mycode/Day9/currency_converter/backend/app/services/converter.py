import requests
from decimal import Decimal
from fastapi import HTTPException


class CurrencyConverter:
    BASE_URL = 'https://api.exchangerate-api.com/v4/latest/'

    @staticmethod
    def get_rates(base_currency: str):
        try:
            response = requests.get(f"{CurrencyConverter.BASE_URL}{base_currency}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise HTTPException(status_code=400, detail=f"Error fetching exchange rates: {e}")

    @staticmethod
    def convert(amount: Decimal, from_currency: str, to_currency: str):
        rates_data = CurrencyConverter.get_rates(from_currency)
        if to_currency not in rates_data['rates']:
            raise HTTPException(status_code=400, detail=f"Currency {to_currency} not supported")

        rate = Decimal(str(rates_data['rates'][to_currency]))
        return amount * rate