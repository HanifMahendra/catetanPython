# scope = The region that a variable is recognized
#         A variable is only  available from inside the region it is created.
#         A global and locally scoped versions of a variable can be created

name = "Hanif"         # global scope (available inside & outside functions)

def display_name():
    name = "Yutori"    # local scope (available only inside this function)
    print(name)

display_name()
print(name)  # yang ini hanya akan menghasilkan output, jika ada variable "name" diluar function seperti pada line 5

# NOTE: local scope > global scope (local scope didahului)