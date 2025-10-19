# SORTING IN PYTHON .sort() or sorted()
# Lists[], Tuples(), Dictionaries{"":""}, Objects

# ---------- LISTS ----------
print("---------- LISTS ----------")
fruits = ["banana", "orange", "apple", "coconut"]

fruits.sort()
print(fruits)
# Output : ['apple', 'banana', 'coconut', 'orange']
fruits.sort(reverse=True)
# Output : ['orange', 'coconut', 'banana', 'apple']
print(f"{fruits} Reversed")

# ---------- TUPLES ----------
print()
print("---------- TUPLES ----------")
fruits2 = ("banana", "orange", "apple", "coconut")

fruits2 = tuple(sorted(fruits2))
print(fruits2)
# Output : ('apple', 'banana', 'coconut', 'orange')
fruits2 = tuple(sorted(fruits2, reverse=True))
print(f"{fruits2} Reversed")
# Output : ('orange', 'coconut', 'banana', 'apple')

# ---------- DICTIONARIES ----------
print()
print("---------- DICTIONARIES ----------")

fruits3 = {
   "banana": 105,
   "apple": 72,
   "orange": 73,
   "coconut": 354
}

fruits3 = dict(sorted(fruits3.items()))
print(fruits3)

fruits3 = dict(sorted(fruits3.items(), key=lambda item: item[0], reverse=True))
print(f"{fruits3} Reversed")

print()

fruits3 = dict(sorted(fruits3.items(), key=lambda item: item[1]))
print(fruits3)

fruits3 = dict(sorted(fruits3.items(), key=lambda item: item[1], reverse=True))
print(f"{fruits3} Reversed")

# ---------- OBJECTS ----------
print()
print("---------- OBJECTS ----------")
class Fruit:
   def __init__(self, name, calories):
       self.name = name
       self.calories = calories

   def __repr__(self):
       return f"{self.name}: {self.calories}"

fruits = [Fruit("banana", 105),
              Fruit("apple", 72),
              Fruit("orange", 73),
              Fruit("coconut", 354)]

fruits = sorted(fruits, key=lambda fruit: fruit.name)
print(fruits)

fruits = sorted(fruits, key=lambda fruit: fruit.name, reverse=True)
print(f"{fruits} Reversed")

print()

fruits = sorted(fruits, key=lambda fruit: fruit.calories)
print(fruits)

fruits = sorted(fruits, key=lambda fruit: fruit.calories, reverse=True)
print(f"{fruits} Reversed")
print()
