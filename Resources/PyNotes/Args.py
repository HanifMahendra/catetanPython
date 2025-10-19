# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments


# ----- *ARGS Example 1 -----

def add2(*args):
    sum2 = 0
    args = list(args)
    args[1] = 0
    for i in args:          # Ini kalo mau diubah jadi list + mau ganti salah satu value
        sum2 += i
    return sum2

print(add2(1,2,3,4,5,6,7,8,9))

def add1(*stuff):
    sum1 = 0
    for i in stuff:         # Ini base
        sum1 += i
    return sum1

print(add1(1,2,3,4,5,6))

# ----- *ARGS Example 2 -----

def add(*nums):
   total = 0
   for num in nums:
       total += num
   return total

print(add(1, 2, 3, 4))

# ----- *ARGS Example 3 -----

def display_name(*args):
   print(f"Hello", end=" ")
   for arg in args:
       print(arg, end=" ")

display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")