import tkinter as tk
from math import sin, cos, tan, log, sqrt, radians, degrees

# Fungsi untuk evaluasi ekspresi matematika
def evaluate_expression():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Fungsi untuk menambahkan teks ke entry
def add_to_expression(value):
    entry.insert(tk.END, value)

# Fungsi untuk menghapus entry
def clear_entry():
    entry.delete(0, tk.END)

# Membuat jendela utama
window = tk.Tk()
window.title("Scientific Calculator")

# Entry untuk memasukkan ekspresi
entry = tk.Entry(window, font=("Arial", 18), justify="right", bd=10, width=30)
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Tombol angka dan operator
buttons = [
    '7', '8', '9', '/', 'sin',
    '4', '5', '6', '*', 'cos',
    '1', '2', '3', '-', 'tan',
    '0', '.', '=', '+', 'sqrt',
    '(', ')', 'log', 'C', '**'
]

# Menambahkan tombol ke GUI
row_val = 1
col_val = 0

for button in buttons:
    if button == "=":
        tk.Button(window, text=button, width=5, height=2, command=evaluate_expression).grid(row=row_val, column=col_val)
    elif button == "C":
        tk.Button(window, text=button, width=5, height=2, command=clear_entry).grid(row=row_val, column=col_val)
    elif button in ["sin", "cos", "tan", "sqrt", "log"]:
        tk.Button(window, text=button, width=5, height=2, command=lambda b=button: add_to_expression(f"{b}(")).grid(row=row_val, column=col_val)
    else:
        tk.Button(window, text=button, width=5, height=2, command=lambda b=button: add_to_expression(b)).grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val > 4:
        col_val = 0
        row_val += 1

# Menjalankan aplikasi
window.mainloop()
