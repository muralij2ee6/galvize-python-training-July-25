# test_currency_converter.py
import pytest
from decimal import Decimal
from unittest.mock import patch, MagicMock
from fastapi import HTTPException
from your_module import CurrencyConverter  # Import the class to test


# Test: Successful rate fetching
@patch('your_module.requests.get')  # Mock the requests.get method
def test_get_rates_success(mock_get):
    """
    Test that get_rates() works correctly with valid input.
    This is the happy path where everything works as expected.
    """
    # Arrange - Setup our test data
    test_currency = "USD"
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "rates": {"EUR": 0.85, "GBP": 0.75},
        "base": "USD"
    }
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    # Act - Call the method we're testing
    result = CurrencyConverter.get_rates(test_currency)

    # Assert - Verify the results
    assert result["base"] == "USD"
    assert "EUR" in result["rates"]
    assert "GBP" in result["rates"]
    mock_get.assert_called_once_with(f"{CurrencyConverter.BASE_URL}{test_currency}")


# Test: Failed API request
@patch('your_module.requests.get')
def test_get_rates_failure(mock_get):
    """
    Test that get_rates() properly handles API failures.
    We simulate a failed API request to see if errors are handled correctly.
    """
    # Arrange - Make the request raise an error
    mock_get.side_effect = requests.exceptions.ConnectionError("API unavailable")

    # Act/Assert - Verify the exception is raised
    with pytest.raises(HTTPException) as exc_info:
        CurrencyConverter.get_rates("USD")

    assert "API unavailable" in str(exc_info.value.detail)
    assert exc_info.value.status_code == 400


# Test: Successful currency conversion
@patch('your_module.CurrencyConverter.get_rates')
def test_convert_success(mock_get_rates):
    """
    Test that convert() works correctly with valid input.
    Checks the math and proper rate application.
    """
    # Arrange - Setup test data and mock
    mock_get_rates.return_value = {
        "rates": {"EUR": 0.85, "GBP": 0.75},
        "base": "USD"
    }
    test_amount = Decimal("100")
    from_curr = "USD"
    to_curr = "EUR"

    # Act - Perform the conversion
    result = CurrencyConverter.convert(test_amount, from_curr, to_curr)

    # Assert - Verify the calculation
    assert result == Decimal("85.00")  # 100 * 0.85
    mock_get_rates.assert_called_once_with(from_curr)


# Test: Unsupported currency
@patch('your_module.CurrencyConverter.get_rates')
def test_convert_unsupported_currency(mock_get_rates):
    """
    Test that convert() rejects unsupported currency codes.
    Checks our error handling for invalid target currencies.
    """
    # Arrange - Setup mock with limited currencies
    mock_get_rates.return_value = {
        "rates": {"EUR": 0.85},
        "base": "USD"
    }
    test_amount = Decimal("100")
    from_curr = "USD"
    to_curr = "XYZ"  # Unsupported currency

    # Act/Assert - Verify the exception
    with pytest.raises(HTTPException) as exc_info:
        CurrencyConverter.convert(test_amount, from_curr, to_curr)

    assert f"Currency {to_curr} not supported" in str(exc_info.value.detail)
    assert exc_info.value.status_code == 400


# Test: Decimal precision handling
@patch('your_module.CurrencyConverter.get_rates')
def test_convert_decimal_precision(mock_get_rates):
    """
    Test that convert() handles decimal precision correctly.
    Important for financial calculations where precision matters.
    """
    # Arrange - Setup precise test data
    mock_get_rates.return_value = {
        "rates": {"JPY": 110.12345678},
        "base": "USD"
    }
    test_amount = Decimal("123.456789")

    # Act
    result = CurrencyConverter.convert(test_amount, "USD", "JPY")

    # Assert - Verify precise calculation
    expected = Decimal("123.456789") * Decimal("110.12345678")
    assert result == expected  # Verifies full precision is maintained