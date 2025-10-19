# while loop = a statement that will execute it's block of code,
#              as long as it's condition remains true (execute some code WHILE some condition remains true)

#cara 1
name = ""

while len(name) == 0:
    name = input("Enter your name: ")
    
print("Hello "+name)

#cara 2
name = None

while not name:
    name = input("Enter your name: ")
    
print("Hello "+name)