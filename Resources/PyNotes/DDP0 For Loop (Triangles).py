n = 6

# Print ascending triangle
for i in range(1, n+1):
    print(" " * (n - i), end="")
    for j in range(1, i+1):
        print("*", end=" ") 
    print()
    
print("==========================================================================================")

# Print descending triangle
n = 6
for i in range(n, 0,-1):
    print(" " * (n - i), end="") 
    for j in range(1, i+1):
        print("*", end=" ") 
    print()

# Print descending triangle (alternative)
n = 6
for i in range(n, 0,-1):
    print(" " * (n-i), end ="")
    for j in range(1, i+1):
        print("*", end ="")
    print()

# Print ascending triangle (alternative)
n = 6
for i in range (1, n+1):
    for j in range (1, i+1):
        print ("*", end = " ")
    print()

# Print descending triangle (alternative)
n = 6
for i in range(n, 0, -1):
    print("* "* i)

# Print ascending triangle (alternative)
n = 6
for i in range(1,n+1):
    print(" " * (n-i), end ="")
    for j in range(1, i+1):
        print("*", end ="")
    print()

# Print numbered triangle
n = 5
count = 1
for i in range (1, n+1):
    for j in range (1, i+1):
        print (count, end= " ")
        count += 1
        if count >6:
            count = 1
    print()

# Print numbered triangle (alternative)
n = 6
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()

# Print numbered triangle (alternative)
n = 6
i = n
while i > 0:
    j = i
    while j > 0:
        print(j, end=' ')
        j -= 1
    print()
    i -= 1