# recursion = a function that calls itself from within
#                      helps to visualize a complex problem into basic steps
#                      problems can be solved more easily iteratively or recursively
#                      iterative = faster, complex
#                      recursive = slower, simpler

# ----- EXAMPLE 1 -----

# ITERATIVE
def walk(steps):                            # Untuk "step" di range 1 - 100, print 'step'
    for step in range(1, steps+1):
        print(f"You take step #{step}")

# RECURSIVE                                 # Jika 'step' nya = 0, maka berhenti. Kalo ga ada "return" bakalan inf loop/ error
def walk(steps):
    if steps == 0:
        return
    walk(steps - 1)
    print(f"You take step #{steps}")

walk(100)

# ----- EXAMPLE 2 -----

# ITERATIVE
def factorial(x):                           # Diketahui result = 1 dan selama x > 0, akan ada pengulangan selama angka masih di range 1-10+1 (1-10)
    result = 1                              # Jika x > 0, selama si y masih di range 1 - 10, maka result = y dikali result, lalu hasilnya akan di return
    if x > 0:                               # Hasil dari return resultnya = 3628800 karena 1 x 2 x 3 x 4 x 5 x ... x 10
        for y in range(1, x + 1):
            result *= y                     # result = result * y
        return result

# RECURSIVE
def factorial(angka):                           # Jika angka == 1, stop di angka 1.
    if angka == 1:                              # Jika angka != 1, stop di angka dikali hasil dari factorial(angka - 1)
        return 1
    else:
        return angka * factorial(angka - 1)     #                          10 x 9!

print(factorial(10))                            # Recursive itu tidak bisa dijalankan secara langsung seperti "factorial(angka - 1)"
                                                # Karena akan menyebabkan error