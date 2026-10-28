"""Exercise 2

Add a new functionality to your program from homework_01.py.
After the program is finished, print a summary containing the highest and lowest
temperatures in degrees Celcius and the corresponding city names.

Example output:
Please enter the name of a city: Munich
Please enter the current temperature in Farenheit in Munich: 14
The current temperature in Munich is 14°F or -10°C.
Warning: The temperature is below freezing point.

Please enter the name of a city: Berlin
Please enter the current temperature in Farenheit in Berlin: 100
The current temperature in Berlin is 100°F or 37.7°C.

Please enter the name of a city: Hamburg
Please enter the current temperature in Farenheit in Hamburg: 0
The current temperature in Berlin is 0°F or -17.8°C.

Please enter the name of a city: exit

Summary:
The highest temperature is 37.7°C in Berlin.
The lowest temperature is -17.8°C in Hamburg.
"""

# Init variables for the highest and lowest temperatures and the corresponding city names

    # Ask the user for the current temperature in Fahrenheit
    

    # Convert the temperature to Celsius
    

    # Print the user input in a formatted string
    

    # Check if the temperature is below freezing point
    

    # Check if the current temperature is the highest or lowest temperature
    
    # Ask the user for the city name
    

# Print the summary


# Initialize variables
highest_celsius = None
lowest_celsius = None
highest_city = ""
lowest_city = ""

while True:

    city = input("Please enter the name of a city: ")

    if city.lower() == "exit":
        break

    fahrenheit = float(input(f"Please enter the current temperature in Fahrenheit in {city}: "))

    celsius = (fahrenheit - 32) * 5 / 9

    print(f"The current temperature in {city} is {fahrenheit:g}°F or {celsius:.1f}°C.")

    if celsius < 0:
        print("Warning: The temperature is below freezing point.")

    if highest_celsius is None or celsius > highest_celsius:
        highest_celsius = celsius
        highest_city = city

    if lowest_celsius is None or celsius < lowest_celsius:
        lowest_celsius = celsius
        lowest_city = city

    print()

if highest_celsius is not None:
    print("Summary:")
    print(f"The highest temperature is {highest_celsius:.1f}°C in {highest_city}.")
    print(f"The lowest temperature is {lowest_celsius:.1f}°C in {lowest_city}.")
else:
    print("No cities were entered.")
