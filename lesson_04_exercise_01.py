"""Exercise 1
Create a list of strings containing words. Using a loop, print out the length
of each word in the list.
words = ["house", "car", "bicycle", "umbrella", "computer"]
"""

Words = ["house", "car", "bicycle", "umbrella", "computer"]
for index in range(len(Words)):
    print(len(Words[index]))

"""
Another alternative i prefer can be:

for word in words:
    print(len(word))
    
"""
