# test_input_validator.py
import pytest
from decimal import Decimal, InvalidOperation
from your_module import InputValidator  # Import the class to test

# Test: Valid currency codes
@pytest.mark.parametrize("currency_code", [
    "USD",  # US Dollar
    "EUR",  # Euro
    "JPY",  # Japanese Yen
    "GBP",  # British Pound
    "CAD",  # Canadian Dollar
])
def test_validate_currency_code_valid(currency_code):
    """
    Test that valid 3-letter uppercase currency codes pass validation.
    These are all real currency codes that should work.
    """
    # This should not raise an exception
    InputValidator.validate_currency_code(currency_code)

# Test: Invalid currency codes
@pytest.mark.parametrize("currency_code,expected_error", [
    ("usd", "Invalid currency code"),  # Lowercase
    ("USD ", "Invalid currency code"),  # Trailing space
    ("US", "Invalid currency code"),   # Too short
    ("USDA", "Invalid currency code"), # Too long
    ("123", "Invalid currency code"),  # Numbers
    ("", "Invalid currency code"),     # Empty string
])
def test_validate_currency_code_invalid(currency_code, expected_error):
    """
    Test that invalid currency codes are rejected with the right error message.
    """
    with pytest.raises(ValueError) as excinfo:
        InputValidator.validate_currency_code(currency_code)
    assert expected_error in str(excinfo.value)

# Test: Valid amounts
@pytest.mark.parametrize("amount_str,expected", [
    ("100", Decimal("100")),       # Whole number
    ("100.00", Decimal("100.00")), # Decimal format
    ("0.01", Decimal("0.01")),     # Small amount
    ("999999.99", Decimal("999999.99")), # Large amount
    ("1.23456789", Decimal("1.23456789")), # High precision
])
def test_validate_amount_valid(amount_str, expected):
    """
    Test that valid positive amounts pass validation and return correct Decimal.
    """
    result = InputValidator.validate_amount(amount_str)
    assert result == expected

# Test: Invalid amounts
@pytest.mark.parametrize("amount_str,expected_error", [
    ("0", "Amount must be positive"),         # Zero
    ("-100", "Amount must be positive"),      # Negative
    ("one hundred", "Invalid amount"),        # Non-numeric
    ("", "Invalid amount"),                   # Empty string
    ("100,00", "Invalid amount"),             # Comma decimal
    ("1O0", "Invalid amount"),                # Letter 'O' instead of zero
])
def test_validate_amount_invalid(amount_str, expected_error):
    """
    Test that invalid amounts are rejected with the right error message.
    """
    with pytest.raises(ValueError) as excinfo:
        InputValidator.validate_amount(amount_str)
    assert expected_error in str(excinfo.value)

# Test: Edge cases
def test_validate_amount_extremely_small():
    """
    Test very small positive amounts still pass validation.
    """
    result = InputValidator.validate_amount("0.00000001")
    assert result == Decimal("0.00000001")

def test_validate_amount_max_precision():
    """
    Test that maximum precision amounts are handled correctly.
    """
    amount_str = "1." + "9" * 50  # 50 decimal places
    result = InputValidator.validate_amount(amount_str)
    assert str(result) == amount_str