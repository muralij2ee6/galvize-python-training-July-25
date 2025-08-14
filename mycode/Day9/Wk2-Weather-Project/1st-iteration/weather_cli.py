"""
weather_cli.py - Command-line weather forecast application
Uses OpenWeatherMap API (https://openweathermap.org/api)
"""

import requests
import json
from dataclasses import dataclass
from typing import Optional, Dict, List


# Data class to structure weather information
@dataclass
class WeatherData:
    city: str
    temperature: float
    condition: str
    humidity: int
    wind_speed: float
    units: str = "metric"

    def display(self) -> str:
        """Format weather data for display"""
        return (
            f"Weather in {self.city}:\n"
            f"- Temperature: {self.temperature}°{self.units_symbol()}\n"
            f"- Condition: {self.condition}\n"
            f"- Humidity: {self.humidity}%\n"
            f"- Wind Speed: {self.wind_speed} {self.speed_unit()}"
        )

    def units_symbol(self) -> str:
        """Get temperature unit symbol"""
        return "C" if self.units == "metric" else "F"

    def speed_unit(self) -> str:
        """Get wind speed unit"""
        return "m/s" if self.units == "metric" else "mph"


class WeatherForecast:
    BASE_URL = "https://api.openweathermap.org/data/2.5"

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.units = "metric"

    def get_current_weather(self, city: str) -> WeatherData:
        """
        Fetch current weather for a city
        Args:
            city: City name to get weather for
        Returns:
            WeatherData object with current conditions
        Raises:
            ValueError: If city is invalid or API request fails
        """
        try:
            response = requests.get(
                f"{self.BASE_URL}/weather",
                params={
                    "q": city,
                    "appid": self.api_key,
                    "units": self.units
                },
                timeout=5
            )
            response.raise_for_status()
            data = response.json()

            return WeatherData(
                city=data["name"],
                temperature=data["main"]["temp"],
                condition=data["weather"][0]["description"],
                humidity=data["main"]["humidity"],
                wind_speed=data["wind"]["speed"],
                units=self.units
            )
        except requests.exceptions.RequestException as e:
            raise ValueError(f"Failed to fetch weather data: {str(e)}")

    def get_forecast(self, city: str, days: int = 5) -> List[WeatherData]:
        """
        Get multi-day weather forecast
        Args:
            city: City name
            days: Number of days to forecast (1-5)
        Returns:
            List of WeatherData objects
        """
        try:
            response = requests.get(
                f"{self.BASE_URL}/forecast",
                params={
                    "q": city,
                    "appid": self.api_key,
                    "units": self.units,
                    "cnt": days * 8  # 8 forecasts per day
                },
                timeout=5
            )
            response.raise_for_status()
            data = response.json()

            forecasts = []
            for item in data["list"]:
                forecasts.append(WeatherData(
                    city=data["city"]["name"],
                    temperature=item["main"]["temp"],
                    condition=item["weather"][0]["description"],
                    humidity=item["main"]["humidity"],
                    wind_speed=item["wind"]["speed"],
                    units=self.units
                ))
            return forecasts
        except requests.exceptions.RequestException as e:
            raise ValueError(f"Failed to fetch forecast: {str(e)}")

    def set_units(self, units: str):
        """Set temperature units (metric/imperial)"""
        if units not in ["metric", "imperial"]:
            raise ValueError("Units must be 'metric' or 'imperial'")
        self.units = units


def main():
    import sys
    from getpass import getpass

    # Get API key securely
    api_key = getpass("Enter your OpenWeatherMap API key: ")
    weather = WeatherForecast(api_key)

    while True:
        print("\nWeather Forecast CLI")
        print("1. Current weather")
        print("2. 5-day forecast")
        print("3. Change units")
        print("4. Exit")

        choice = input("Select option: ")

        if choice == "1":
            city = input("Enter city name: ")
            try:
                current = weather.get_current_weather(city)
                print("\n" + current.display())
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            city = input("Enter city name: ")
            try:
                forecasts = weather.get_forecast(city)
                print(f"\n5-day forecast for {city}:")
                for i, forecast in enumerate(forecasts[:5 * 8:8]):  # Show one per day
                    print(f"\nDay {i + 1}:")
                    print(forecast.display())
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "3":
            units = input("Enter units (metric/imperial): ")
            try:
                weather.set_units(units)
                print(f"Units changed to {units}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "4":
            sys.exit(0)

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()