"""Weather forecast app:

In this homework, you will finalize your weather app with real live data.
We use https://open-meteo.com, a free, open-source weather service for this.

To get data from the website, we have to do API calls. This means that we send
a request to the website and get a response in JSON format.
JSON can be easily converted to a Python dictionary.
For this we need the requests library. You can install it with pip:
python -m pip install requests

An API call is a URL that we send to the website. The URL contains information
about what we want to get from the website.

We already implemented a function (get_coordinates) for you that will get the
geo-coordinates (latitude, longitude and elevation) of a city.

You can find more information on how to use the API here:
https://open-meteo.com/en/docs


1. Your task is to implement a function (get_weather) that will get the current
weather and temperature of a city.
You can get the temperature from the API response.
You can also get the weather code from the API response.
You can use the weather code to get the weather description from the WEATHER_CODES
get_weather should return two variables: weather (str) and temperature (float).

2. In your program, ask the user for the name of a city.
Then call the get_weather function and print the weather and temperature.
The program should continue in a loop until the user enters "exit".

Example output:
Please enter the name of a city: Munich
The current weather in Munich is Partly cloudy and the temperature is 21.5°C.
Please enter the name of a city: Berlin
The current weather in Berlin is Clear sky and the temperature is 23.6°C.
Please enter the name of a city: exit
"""

import requests


#dictionary with the weather codes from https://open-meteo.com
WEATHER_CODES = {
    0: "Clear sky",
    1: "Manily clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    56: "Light freezing drizzle",
    57: "Dense freezing drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Light freezing rain",
    67: "Heavy freezing rain",
    71: "Slight snow fall",
    73: "Moderate snow fall",
    75: "Heavy snow fall",
    77: "Snow grains",
    80: "Slight rain shower",
    81: "Moderate rain shower",
    82: "Violent rain shower",
    85: "Slight snow shower",
    86: "Heavy snow shower",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail",
}


def get_coordinates(city_name):
    """Returns the latitude, longitude and elevation of a city."""
    # Create the API call URL
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=en&format=json"
    # Send the request to the website and get the response
    response = requests.get(url)
    # Convert the response from JSON to a Python dictionary
    data = response.json()
    # Check if the city was found
    if "results" not in data:
        raise Exception("City not found.")
    # Get the latitude, longitude and elevation from the response
    latitude = data["results"][0]["latitude"]
    longitude = data["results"][0]["longitude"]
    elevation = data["results"][0]["elevation"]
    return latitude, longitude, elevation


def get_weather(city_name):
    # Error handling when the city is not found
    try:
        latitude, longitude, elevation = get_coordinates(city_name)
    except Exception as e:
        print(e)
        return "Error", float("nan")
    # Create the API call URL
    url = "https://api.open-meteo.com/v1/forecast?"
    url += "current_weather=true"  # Add current_weather to request URL
    url += f"&latitude={latitude:.2f}"  # Add latitude to request URL
    # TODO: finish the function
    
    # 1. Add longitude and elevation to the request URL
    # 2. Send the request to the website and get the response
    # 3. Convert the response from JSON to a Python dictionary
    # 4. Get the temperature and weather code from the response
    # 5. Get the weather description from the WEATHER_CODES dictionary
    # YOUR CODE
    url += f"&longitude={longitude:.2f}"
    url += f"&elevation={elevation}"

    response = requests.get(url)
    data = response.json()

    temperature = data["current_weather"]["temperature"]
    weather_code = data["current_weather"]["weathercode"]
    weather = WEATHER_CODES[weather_code]

    # YOUR CODE END
    return weather, temperature


if __name__ == "__main__":
    # TODO: Implement the weather forecast app here
    # YOUR CODE

    while True:
        city = input("Please enter the name of a city: ")

        if city.lower() == "exit":
            break

        weather, temperature = get_weather(city)

        print(
            f"The current weather in {city} is {weather} "
            f"and the temperature is {temperature}°C."
        )


    # YOUR CODE END