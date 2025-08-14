# test_currency_converter.py
import pytest
from fastapi.testclient import TestClient
from decimal import Decimal
from unittest.mock import patch
from main import app  # Import our FastAPI application
from models.schemas import ConversionInput

# Create a test client for making requests to our API
client = TestClient(app)


# Test: Successful currency conversion
@patch("main.CurrencyConverter")  # Mock the CurrencyConverter class
def test_convert_currency_success(mock_converter):
    """
    Test that currency conversion works with valid input.
    This is testing the happy path where everything works correctly.
    """
    # Arrange - Setup our test data and mocks
    test_data = {
        "amount": "100",
        "from_currency": "USD",
        "to_currency": "EUR"
    }

    # Mock the converter to return specific values
    mock_converter.convert.return_value = Decimal("85.50")
    mock_converter.get_rates.return_value = {
        "rates": {"EUR": 0.8550}
    }

    # Act - Make the API request
    response = client.post("/convert", json=test_data)

    # Assert - Verify the response
    assert response.status_code == 200  # Success status code
    assert response.json() == {
        "original_amount": "100",
        "from_currency": "USD",
        "converted_amount": "85.50",
        "to_currency": "EUR",
        "rate": "0.8550"
    }


# Test: Invalid currency code
def test_convert_invalid_currency():
    """
    Test that the API rejects invalid currency codes.
    This checks our input validation works.
    """
    # Arrange - Bad data with invalid currency code
    test_data = {
        "amount": "100",
        "from_currency": "USX",  # Invalid code
        "to_currency": "EUR"
    }

    # Act
    response = client.post("/convert", json=test_data)

    # Assert
    assert response.status_code == 400  # Bad request status code
    assert "Invalid currency code" in response.json()["detail"]


# Test: Invalid amount
def test_convert_invalid_amount():
    """
    Test that the API rejects invalid amounts.
    Checks our amount validation works.
    """
    # Arrange - Bad data with invalid amount
    test_data = {
        "amount": "not_a_number",  # Invalid amount
        "from_currency": "USD",
        "to_currency": "EUR"
    }

    # Act
    response = client.post("/convert", json=test_data)

    # Assert
    assert response.status_code == 400
    assert "Invalid amount" in response.json()["detail"]


# Test: Get common currencies
def test_get_currencies():
    """
    Test that the currencies endpoint returns the expected data.
    This is a simple endpoint that should always return the same list.
    """
    # Act
    response = client.get("/currencies")

    # Assert
    assert response.status_code == 200
    assert "USD" in response.json()["common_currencies"]
    assert len(response.json()["common_currencies"]) > 0


# Test: API key endpoint
@patch.dict("os.environ", {"API_KEY": "test_key_123"})
def test_get_api_key():
    """
    Test that the API key endpoint returns the key from environment.
    We mock the environment variable for this test.
    """
    # Act
    response = client.get("/api-key")

    # Assert
    assert response.status_code == 200
    assert response.json()["api_key"] == "test_key_123"


# Test: Server error handling
@patch("main.CurrencyConverter.convert")
def test_server_error(mock_convert):
    """
    Test that the API handles internal server errors properly.
    We force an error to see if it's handled gracefully.
    """
    # Arrange - Make the converter raise an error
    mock_convert.side_effect = Exception("Database connection failed")

    # Act
    response = client.post("/convert", json={
        "amount": "100",
        "from_currency": "USD",
        "to_currency": "EUR"
    })

    # Assert
    assert response.status_code == 500  # Internal server error
    assert "Database connection failed" in response.json()["detail"]