"""
Exercise 1:
Extend the program from last week to convert the temperature from Fahrenheit
to Celsius.

1. Ask the user for the name of a city and the current temperature in Fahrenheit.
2. Convert the temperature to Celsius.
3. If the temperature is below freezing point (0 °C),
    print a warning message saying "Alert: The temperature is below freezing point."
Otherwise, print a message saying
    "The temperature is above the freezing point."  
PS:
The formula for converting Fahrenheit to Celsius is:
C = (F - 32) * 5/9
"""

City = input("Please enter name of the city: ")
Temp_F = float(input("Please enter the current temperature in Fahrenheit:"))
Celsius = (Temp_F - 32) *5/9
if Celsius > 0 :
 print("Alert: The temperature is below freezing point.")
else:
 print("The temperature is above the freezing point!")
print(f"This is current temperature in {City} is {Celsius:f} °C.")
