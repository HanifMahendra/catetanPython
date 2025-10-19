# return statement = Function send Python values/objects back to the caller.
#                    These values/objects are known as the function's return value.


def multiply2(number1, number2):     # Jika seperti ini, output tidak akan muncul karena returnnya hanya menyimpan sebuah "nilai"
    return number1 * number2

multiply2(6,8)

#--------------------------------------------#

def multiply(number1, number2):      # Jika seperti ini, output akan muncul karena fungsi "return"nya menyimpan sebuah "nilai" dan "nilai" tersebut di "print" oleh fungsi print
    return number1 * number2

x = multiply(6,8)

print(x)