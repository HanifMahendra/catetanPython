import os

source = "C:\\Users\\Mahendra's\\OneDrive\\Documents\\Ngopi slur\\Python\\hayo.txt"
destination = "C:\\Users\\Mahendra's\\OneDrive\\Desktop\\hayo.txt"

try:
    os.replace(source,destination)
    print(source, " was moved!")
except FileNotFoundError:
    print(source, " was not found!")