# List comprehension = A concise way to create lists in Python
#                                        Compact and easier to read than traditional loops
#                                        [expression for value in iterable if condition]
#                                        Expression: What to do with each value.

#                                        Value: The current element from the iterable.
#                                        Iterable: Any sequence like a list, range, or string.
#                                        Condition (optional): A filter to include only certain elements.
doubles = [x * 2 for x in range(1, 11)]
triples = [y * 3 for y in range(1, 11)]
squares = [z * z for z in range(1, 11)]

fruits = ["apple", "orange", "banana", "coconut"]
uppercase_words = [fruit.upper() for fruit in fruits]
fruit_chars = [fruit[0] for fruit in fruits]

numbers = [1, -2, 3, -4, 5, -6, 8, -7]
positive_numbers = [x for x in numbers if x >= 0]
negative_numbers = [x for x in numbers if x < 0]
even_numbers = [x for x in numbers if x % 2 == 0]
odd_numbers = [x for x in numbers if x % 2 == 1]

grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]

class Comprehension:
    def doubles(self):
        """Returns a list of numbers doubled (2x)."""
        return [x * 2 for x in range(1, 11)]

    def triples(self):
        """Returns a list of numbers tripled (3x)."""
        return [y * 3 for y in range(1, 11)]

    def squares(self):
        """Returns a list of squared numbers."""
        return [z * z for z in range(1, 11)]

    def uppercase_fruits(self, fruits):
        """Converts a list of fruits to uppercase."""
        return [fruit.upper() for fruit in fruits]

    def first_chars(self, fruits):
        """Returns the first character of each fruit."""
        return [fruit[0] for fruit in fruits]

    def filter_numbers(self, numbers):
        """Filters positive, negative, even, and odd numbers."""
        positive = [x for x in numbers if x >= 0]
        negative = [x for x in numbers if x < 0]
        even = [x for x in numbers if x % 2 == 0]
        odd = [x for x in numbers if x % 2 == 1]
        return {"positive": positive, "negative": negative, "even": even, "odd": odd}

    def passing_grades(self, grades):
        """Returns grades that are >= 60."""
        return [grade for grade in grades if grade >= 60]


# Create an object of the Comprehension class
comp = Comprehension()

# Call the methods
print("Doubles:", comp.doubles())
print("Triples:", comp.triples())
print("Squares:", comp.squares())

fruits = ["apple", "orange", "banana", "coconut"]
print("Uppercase Fruits:", comp.uppercase_fruits(fruits))
print("First Chars of Fruits:", comp.first_chars(fruits))

numbers = [1, -2, 3, -4, 5, -6, 8, -7]
filtered = comp.filter_numbers(numbers)
print("Positive Numbers:", filtered["positive"])
print("Negative Numbers:", filtered["negative"])
print("Even Numbers:", filtered["even"])
print("Odd Numbers:", filtered["odd"])

grades = [85, 42, 79, 90, 56, 61, 30]
print("Passing Grades:", comp.passing_grades(grades))

