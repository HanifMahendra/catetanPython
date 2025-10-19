# set = collection which is unordered, unindexed. No duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

utensils.add("napkin") #nambahin "napkin" di (utensils)
utensils.remove("fork") #hapus "fork" di (utensils)
utensils.update(dishes)  #menggabungkan (utensils) dan (dishes)  menjadi satu
utensils.clear()  #menghapus semua isi (utensils)
dinner_table = utensils.union(dishes) #bisa dibalik

print(dishes.difference(utensils)) #print  semua elemen yang ada di (dishes) tapi tidak ada di (utensils)
print(utensils.intersection(dishes))  #print semua elemen yang ada di (utensils) dan (dishes)

 
for x in utensils:
    print(x)