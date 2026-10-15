"""
Exercise 1

Improve your weather forecast program to handle multiple cities ad more information.

All cities should be stored in a dictionary. The city name should be the key
and the value should be another dictionary containing the following information:
- current temperature in Celsius
- current temperature in Fahrenheit
- is it raining? ("yes" or "no")
- is the sun shining? ("yes" or "no")

The user should be able to finish the program by entering "exit" as city name

Once the user is finished, print a summary for each city with the information above.
If the temperature is below 0°C, print a warning message.
If it is both raining and the sun is shining, print a notification that there is a rainbow.
"""

cities = {}
while True:
    city = input("Please enter the name of a city: ").strip()
    if city.lower() == "exit":
        break
    while True:
        unit = input(
            "Would you like to enter the temperature in Fahrenheit or Celsius?: "
        ).strip().lower()

        if unit in ("fahrenheit", "f", "celsius", "c"):
            break
        else:
            print("Please enter Fahrenheit or Celsius.")
    if unit in ("celsius", "c"):
        temperature_c = float(
            input(f"Please enter the current temperature in Celsius in {city}: ")
        )
        temperature_f = temperature_c * 9 / 5 + 32
    else:
        temperature_f = float(
            input(f"Please enter the current temperature in Fahrenheit in {city}: ")
        )
        temperature_c = (temperature_f - 32) * 5 / 9
    while True:
        raining = input(f"Is it raining in {city}? (yes/no): ").strip().lower()
        if raining in ("yes", "no"):
            break
        print("Please answer yes or no.")
    while True:
        sunny = input(f"Is the sun shining in {city}? (yes/no): ").strip().lower()
        if sunny in ("yes", "no"):
            break
        print("Please answer yes or no.")
    cities[city] = {
        "celsius": temperature_c,
        "fahrenheit": temperature_f,
        "raining": raining,
        "sunny": sunny
    }
print("\nSummary:")

for city, weather in cities.items():
    # Choose readable words for the summary.
    sun_text = "sun" if weather["sunny"] == "yes" else "no sun"
    rain_text = "rain" if weather["raining"] == "yes" else "no rain"
    print(
        f"{city}: {round(weather['celsius'])}°C, "
        f"{round(weather['fahrenheit'])}°F, "
        f"{sun_text} and {rain_text}"
    )
    if weather["celsius"] < 0:
        print(f"Warning: The temperature in {city} is below the freezing point")
    if weather["raining"] == "yes" and weather["sunny"] == "yes":
        print(f"There is a rainbow in {city}.")
    print()

