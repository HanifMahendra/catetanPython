import turtle
import random

sisi_n = int(input("Masukkan nilai N (sisi): "))

while sisi_n < 3 or sisi_n > 10:
    print("Angka 'N' harus diantara 3-10!")
    sisi_n = int(input("Masukkan nilai N (sisi): "))

warna = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "black", "white"]

# Set up the turtle
kura_kura = turtle.Turtle()
kura_kura.pensize(5)
kura_kura.fillcolor(random.choice(warna))  # Pilih warna secara acak
kura_kura.begin_fill()

for _ in range(sisi_n):  # Loop untuk membuat poligon
    kura_kura.forward(50 + (sisi_n * 10))  # Atur panjang sisi berdasarkan nilai "sisi_n"
    kura_kura.right(360 / sisi_n) 

kura_kura.end_fill()

turtle.done()