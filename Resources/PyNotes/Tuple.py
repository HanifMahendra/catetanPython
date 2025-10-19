# tuple = collection which is ordered and unchangeable
#         used to group together related data

student = ("Bro", 21, "male")

print(student.count("Bro")) #untuk menghitung ada berapa "Bro" di (student)
print(student.index("male")) #untuk menghitung ada di angka ke "berapa" sih "male" itu

for x in student:
    print(x)
    
if "Bro" in student:
    print("Bro is here!")