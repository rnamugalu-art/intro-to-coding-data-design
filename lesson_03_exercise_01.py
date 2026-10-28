"""Homework 1

Improve your program from last week to handle multiple cities. The user should
be able to enter the names and temperatures of as many cities as they want. Use
a loop to facilitate this and print out all the cities along with
their temperatures in Celsius and Fahrenheit. Again, give a warning if the
temperature is below the freezing point. To stop the loop, the user should
be able to enter "exit" as the city name.

Example output:
Please enter the name of a city: Munich
Please enter the current temperature in Farenheit in Munich: 14
The current temperature in Munich is 14°F or -10°C.
Warning: The temperature is below freezing point.

Please enter the name of a city: exit
"""

    # Ask the user for the current temperature in Fahrenheit
    

    # Convert the temperature to Celsius
    

    # Print the user input in a formatted string
    
    # Check if the temperature is below freezing point
    

    # Ask the user for the city name


while True:

 city = input("Please enter the name of a City: ")
 if city.lower() == "exit":
   break

fahrenheit = float(
   input(f"Please enter the current temperature in Fahrenheit in {city}: "))

celsius = (fahrenheit - 32) * 5 / 9

print(f"The current temperature in {city} is ")
print (f"{fahrenheit:g}°F or {celsius:.0f}°C.")

if celsius < 0:
    print("Warning: The temperature is below freezing point.")

print()
