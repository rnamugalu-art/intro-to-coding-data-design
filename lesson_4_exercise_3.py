"""Exercise 3
Write a program that asks the user for their favorite colors (up to 5)
and stores them in a list. Then, create a sentence that says,
"Your favorite colors are: color1, color2, ..." using the .join() function.
"""

favorite_colors = []

for number in range(5):
    color = input("Enter one of your favorite colors: ")
    favorite_colors.append(color)

colors_text = ", ".join(favorite_colors) #join combines all the lists in one sentence

print("Your favorite colors are: " + colors_text)
