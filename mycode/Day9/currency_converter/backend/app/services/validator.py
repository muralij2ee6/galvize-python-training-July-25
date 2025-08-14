import re
from decimal import Decimal, InvalidOperation


class InputValidator:
    @staticmethod
    def validate_currency_code(currency_code: str):
        if not re.match(r'^[A-Z]{3}$', currency_code):
            raise ValueError("Invalid currency code. Use 3-letter codes like USD, EUR")

    @staticmethod
    def validate_amount(amount_str: str):
        try:
            amount = Decimal(amount_str)
            if amount <= 0:
                raise ValueError("Amount must be positive")
            return amount
        except InvalidOperation:
            raise ValueError("Invalid amount. Please enter a positive number")