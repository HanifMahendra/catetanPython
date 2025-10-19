def f(x,y):
    counter = 0
    for a in y:
        if set(x).issubset(set(a)):
            counter += 1
    return counter

def f(x,y):
    counter = 0
    for a in y:
        if set(x) <= set(a):
            counter += 1
    return counter

x = [1, 2]
y = [[1, 2, 3], [4, 5], [1, 2], [2, 3, 1]]

result = f(x, y)
print(result)