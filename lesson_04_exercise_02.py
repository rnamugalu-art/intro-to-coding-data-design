"""Exercise 2
1. Create a list of your favorite fruits. Print the third fruit on the list.
2. Append two new fruits to your favorite fruits. Print the updated list
3. Remove the second fruit from the list and print the updated list.
"""

favorite_fruits = ["pear", "grape", "mango","apple"]
print(favorite_fruits[2])

favorite_fruits.append("banana") #adding item
favorite_fruits.append("jackfruit") #adding item

print(favorite_fruits)

favorite_fruits.pop(1) #removing item

print(favorite_fruits)
