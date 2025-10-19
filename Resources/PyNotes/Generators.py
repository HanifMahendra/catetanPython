# Generators = a special type of function that yield values one at a time instead of returning all the results at once. 
#              This saves memory and improves performance for large datasets.

def countdown(n): # Generator memungkinkan fungsi untuk menghasilkan nilai satu per satu 
    while n > 0:  # daripada mengembalikan semua nilai sekaligus seperti pada fungsi biasa.
        yield n
        n -= 1

gen = countdown(5)

for i in gen:
    print(i)
print()
# Saat yield dipanggil dalam sebuah fungsi, fungsi tersebut akan pause (berhenti sementara) 
# dan mengembalikan nilai yang disebutkan setelah yield.

# Saat fungsi dilanjutkan (dengan next() atau for loop), 
# eksekusi akan melanjutkan dari titik terakhir (tempat yield berhenti).

def fibo_generator():
    first, second = 2,3
    while True:
        yield first # Kalo ada next() "yield" ga diitung lagi
        first,second = second, first + second # first -> second & second -> first + second
fiboGen = fibo_generator()
for count in range (10):
    print(next(fiboGen), end=', ')
