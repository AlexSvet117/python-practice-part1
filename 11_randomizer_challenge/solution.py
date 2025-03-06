import random

## Instructions  
# 1. Print a random float between 0 and 1.  
# 2. Print a random integer between 1 and 50.  
# 3. Print a random choice from the list `["red", "blue", "green", "black", "yellow"]`.  
# 4. Shuffle the list `["apple", "banana", "plum", "orange"]` and print it.

colors = ["red", "blue", "green", "black", "yellow"]
fruits = ["apple", "banana", "plum", "orange"]

print(random.random())
print(random.randint(0,50))
print(random.choice(colors))
random.shuffle(fruits)
print(fruits)



