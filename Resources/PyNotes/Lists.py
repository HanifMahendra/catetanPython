#list = used to store multiple items in a single variable

food = ["pizza", "hamburger",  "hotdog", "spaghetti", "pudding"]

food[0] = "sushi"

food.append("ice cream") #add a new item to the end of the list
food.remove("hotdog") #remove  the first occurrence of the item
food.pop()  #remove the last item from the list
food.insert(0, "cake")  #insert the item at the specified position
food.sort() #sort the list in ascending order
food.reverse() #reverse the list
food.clear()  #remove all items from the list

for x in food:
    print(x)