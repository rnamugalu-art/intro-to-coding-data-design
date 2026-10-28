"""
Exercise 2:
Now extend the program and ask for the temperature in two cities.

1. Ask the user for the name of two cities and the current temperatures in Fahrenheit.
2. Convert the temperatures to Celsius.
3. If the temperature in both cities is below freezing point (32 °F),
    print a warning message saying "Alert: The temperatures in both cities are below freezing point."
else if the temperature in only one of the cities is below freezing point,
    print a warning message saying "Alert: The temperature in one of the cities is below freezing point."
Otherwise, print a message saying
    "The temperatures in both cities are above the freezing point."
4. Lastly, always print the temperatures in Celsius (up to one decimal point).

PS:
The formula for converting Fahrenheit to Celsius is:
C = (F - 32) * 5/9
"""

City1 = input("Please enter name of the first city: ")
City2 = input("Please enter name of the second city: ")

Temp_F1 = float(input(f"Please enter the current temperature for {City1} in Fahrenheit: "))
Temp_F2 = float(input(f"Please enter the current temperature for {City2} in Fahrenheit: "))

Celsius1 = (Temp_F1 - 32) *5/9
Celsius2 = (Temp_F2 - 32) *5/9

if Celsius1 < 0 and Celsius2 < 0:
 print("Alert: The temperature in both cities is below freezing point.")
elif Celsius1 < 0 or Celsius2 < 0:
 print("Alert: The temperature in one of the cities is below freezing point.")
else:
 print("The temperatures in both cities are above the freezing point.")

print(f"The current temperature in {City1} is {Celsius1:f} °C.")
print(f"The current temperature in {City2} is {Celsius2:f} °C.")
