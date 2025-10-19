# Nested Function Calls = function calls inside other function calls
#                         innermost function calls are resolved first
#                         returned value is used as argument for the next outer function

num = input("Enter a whole positive number: ")                       # Ini versi normal/basicnya saja
num = float(num)
num = abs(num)
num = round(num)
print(num)

#---------------------------------------------#

print(round(abs(float(input("Enter a whole positive number: ")))))   # Ini versi lebih singkat saja (1 line code)