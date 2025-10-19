# Exception = events detected during execution that interrupt the flow of a program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero!")
except ValueError as e:
    print(e)
    print("Numbers only")
except Exception as e:
    print(e)
    print("Something went wrong :(")
else:
    print(f"The result is {result}")
finally:
    print("Yey") # This usually used in file coding