City_1 = input("Please enter the name of the first city: ")
City_2 = input("Please enter the name of the second city: ")
Temperature_1 = float(input("Please enter the current temperature for Munich in Celsius: "))
Temperature_2 = float(input("Please enter the current temperature for Nürenberg in Celsius: "))
Average_Celsius = (Temperature_1 + Temperature_2) / 2
print (f"The average temperature between {City_1} and {City_2} is {Average_Celsius} °C,")
Average_Fahrenheit = (Average_Celsius * 9/5) + 32
print(f"that is {Average_Fahrenheit: } °F.")