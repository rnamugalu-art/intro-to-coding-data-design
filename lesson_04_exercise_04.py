"""Exercise 4
Create a list of even numbers from 2 to 20 (inclusive) using a loop.
Print the list.
"""

even_numbers = []

for number in range(2, 21, 2): #2 is the starting number, and keeps increasing by 2. it stops before 21.
    even_numbers.append(number)

print(even_numbers)
