import os
import requests
import streamlit as st
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()


def get_weather(city):
    """
    Fetch current weather information from OpenWeather.
    
    Returns:
        Dictionary containing weather information
        or a dictionary containing an error message.
    """

    # Get API key
    api_key = os.getenv("OPENWEATHER_API_KEY")

    # Check API key
    if not api_key:
        return {
            "error": "OPENWEATHER_API_KEY was not found."
        }

    # Clean city name
    city = city.strip()

    if not city:
        return {
            "error": "Please enter a city or district name."
        }

    # OpenWeather current weather API
    url = "https://api.openweathermap.org/data/2.5/weather"

    # API parameters
    params = {
        "q": f"{city},IN",
        "appid": api_key,
        "units": "metric"
    }

    try:

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        # Successful response
        if response.status_code == 200:

            data = response.json()

            # Temperature
            temperature = data["main"]["temp"]

            # Feels like temperature
            feels_like = data["main"]["feels_like"]

            # Humidity
            humidity = data["main"]["humidity"]

            # Atmospheric pressure
            pressure = data["main"]["pressure"]

            # Weather description
            description = data["weather"][0]["description"]

            # Weather main condition
            condition = data["weather"][0]["main"]

            # Wind speed
            wind_speed = data["wind"]["speed"]

            # Cloud percentage
            clouds = data["clouds"]["all"]

            # Rainfall
            # Rain may not exist in every API response
            rain_data = data.get("rain", {})

            rainfall_1h = rain_data.get("1h", 0)

            rainfall_3h = rain_data.get("3h", 0)

            return {
                "success": True,
                "city": data.get("name", city),
                "country": data.get("sys", {}).get("country", "IN"),
                "temperature": temperature,
                "feels_like": feels_like,
                "humidity": humidity,
                "pressure": pressure,
                "description": description,
                "condition": condition,
                "wind_speed": wind_speed,
                "clouds": clouds,
                "rainfall_1h": rainfall_1h,
                "rainfall_3h": rainfall_3h
            }

        # Invalid API key
        elif response.status_code == 401:

            return {
                "error": "OpenWeather API key is invalid or inactive."
            }

        # City not found
        elif response.status_code == 404:

            return {
                "error": f"City or district '{city}' was not found."
            }

        # Too many requests
        elif response.status_code == 429:

            return {
                "error": "OpenWeather API request limit exceeded."
            }

        # Other API errors
        else:

            return {
                "error": (
                    f"OpenWeather error: "
                    f"{response.status_code} - "
                    f"{response.text}"
                )
            }

    except requests.exceptions.Timeout:

        return {
            "error": "Weather request timed out. Please try again."
        }

    except requests.exceptions.ConnectionError:

        return {
            "error": "Could not connect to OpenWeather."
        }

    except requests.exceptions.RequestException as e:

        return {
            "error": f"Weather request failed: {str(e)}"
        }

    except Exception as e:

        return {
            "error": f"Unexpected error: {str(e)}"
        }
