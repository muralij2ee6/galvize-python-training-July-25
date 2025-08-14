"""
test_weather.py - Unit tests for weather CLI application
Follows TDD practices with pytest
"""

import pytest
from unittest.mock import Mock, patch
from weather_cli import WeatherForecast, WeatherData


# Fixture for mock API responses
@pytest.fixture
def mock_weather_response():
    return {
        "name": "London",
        "main": {"temp": 15.5, "humidity": 72},
        "weather": [{"description": "cloudy"}],
        "wind": {"speed": 3.2}
    }


@pytest.fixture
def mock_forecast_response():
    return {
        "city": {"name": "London"},
        "list": [
            {
                "main": {"temp": 15.5, "humidity": 72},
                "weather": [{"description": "cloudy"}],
                "wind": {"speed": 3.2}
            } for _ in range(40)  # 5 days of data
        ]
    }


def test_weather_data_display():
    """Test WeatherData display formatting"""
    weather = WeatherData(
        city="Paris",
        temperature=22.5,
        condition="sunny",
        humidity=45,
        wind_speed=2.1,
        units="metric"
    )
    display = weather.display()
    assert "Paris" in display
    assert "22.5°C" in display
    assert "sunny" in display
    assert "45%" in display
    assert "2.1 m/s" in display


@patch('requests.get')
def test_get_current_weather_success(mock_get, mock_weather_response):
    """Test successful current weather fetch"""
    mock_get.return_value = Mock(
        status_code=200,
        json=lambda: mock_weather_response
    )

    weather = WeatherForecast("dummy_key")
    result = weather.get_current_weather("London")

    assert result.city == "London"
    assert result.temperature == 15.5
    assert result.condition == "cloudy"
    assert result.humidity == 72
    assert result.wind_speed == 3.2


@patch('requests.get')
def test_get_current_weather_failure(mock_get):
    """Test failed weather fetch"""
    mock_get.return_value = Mock(
        status_code=404,
        raise_for_status=Mock(side_effect=requests.exceptions.HTTPError)
    )

    weather = WeatherForecast("dummy_key")
    with pytest.raises(ValueError):
        weather.get_current_weather("InvalidCity")


@patch('requests.get')
def test_get_forecast(mock_get, mock_forecast_response):
    """Test 5-day forecast fetch"""
    mock_get.return_value = Mock(
        status_code=200,
        json=lambda: mock_forecast_response
    )

    weather = WeatherForecast("dummy_key")
    forecasts = weather.get_forecast("London")

    assert len(forecasts) == 40  # 5 days * 8 readings per day
    assert all(f.city == "London" for f in forecasts)


def test_set_units():
    """Test unit system change"""
    weather = WeatherForecast("dummy_key")
    weather.set_units("imperial")
    assert weather.units == "imperial"

    with pytest.raises(ValueError):
        weather.set_units("invalid")


# Integration test (requires actual API key)
@pytest.mark.integration
def test_live_api_integration():
    """Integration test with real API (requires network)"""
    import os
    api_key = os.getenv("OWM_API_KEY")
    if not api_key:
        pytest.skip("No API key provided")

    weather = WeatherForecast(api_key)
    result = weather.get_current_weather("London")

    assert isinstance(result, WeatherData)
    assert result.city == "London"
    assert isinstance(result.temperature, float)