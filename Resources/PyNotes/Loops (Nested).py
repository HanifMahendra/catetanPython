# nested loops = the "inner loop" will finish all of it's interactions before
#                finishing one iteration of the "outer loop"
#                or
# nested loops = A loop within another loop (outer, inner)
#                outer loop:
#                   inner loop:

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter the symbol to use: ")

for i in range(rows):               # This i loop will loop j a certain times
    for j in range(columns):
        print(symbol, end=" ") # Ada spasi diantara setiap symbol
    print()

for x in range(3):
    for y in range(1, 10):
        print(y, end="")
    print()

for x in range(rows):
    for y in range(columns):
        print(symbol, end="") # Ga ada spasi diantara setiap symbol
    print()

n = 5
for x in range(1,n+1):
    print(" " * (n-x), end="")
    for y in range(columns):
        print(symbol, end=" ")
    print()

