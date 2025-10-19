
text = "Have a nice day!" + " This is an example text\nThis is to make a new line"

with open("Text.txt","w") as file:
    file.write(text)

# "w" to write
# "r" to read
# "a" to add something to the file