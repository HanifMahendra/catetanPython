import random

x = random.randint(1,6)                         # Randomize the following numbers (for ints)
y = random.random()                             # Randomize number between 0-1

print(x)
print(y)

myList = ["rock", "paper", "scissors"]
z = random.choice(myList)                       # Randomize the following choice (for strings)

print(z)

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]

random.shuffle(cards)                           # Shuffle the follwing list

print(cards)