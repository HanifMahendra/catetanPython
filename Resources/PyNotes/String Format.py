# str.format() = optional method that gives users
#                more control when displaying output

animal = "cow"
item = "moon"

print("The " + animal+" jumped over the "+item)
print("The {} jumped over the {}".format(animal,item))
print("The {0} jumped over the {1}".format(animal,item)) # Positional arguments
print("The {animal} jumped over the {item}".format(animal="cow", item="moon")) # Keyword arguments

text = "The {} jumped over the {}"
print(text.format(animal,item))

# ================================================================================================================================================

name = "Hanif"

print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name))
print("Hello, my name is {:<10}. Nice to meet you".format(name))
print("Hello, my name is {:>10}. Nice to meet you".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name))
print("Hello, my name is {:^10}. Nice to meet you".format(name))

# ================================================================================================================================================

pi = 3.14159

print("The number pi is {:.2f}".format(pi)) # You can change it to .3f or else.

number = 1000

print("The number is {:,}".format(number))
print("The number is {:b}".format(number))
print("The number is {:o}".format(number))
print("The number is {:X}".format(number))
print("The number is {:E}".format(number))
