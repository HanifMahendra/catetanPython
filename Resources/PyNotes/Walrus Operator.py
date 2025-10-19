# walrus operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# foods = list()
# while True:
#   food = input("What food do you like?: ")
#       if food == "quit":
#           break
#   foods.append(food)

foods = list()
if food := input("What food do you like?: ") != "quit":
    foods.append(food)

food = []

quantity = input("How many items you want to buy? ")
for i in range (int(quantity)):
    food.append(input("What your list of shopping?: "))
if (value := len(food)) > 0:
    print(f"Your shopping list has {value} elements")
    print("Here is your list:")
    for items in food:
        print(f"- {items}")
else:
    print("Your shopping list is empty")