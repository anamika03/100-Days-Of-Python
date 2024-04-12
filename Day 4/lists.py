# # Lists 
# # positive index - [0 to n]
# # negatve index - [-1 to n]
# fruits = ["Cheery", "Apple", "Banana"]
# print(fruits)
# fruits.append("Mango")
# print(fruits)
# fruits.extend(["Guava", "Avacado", "Grapes"])
# print(fruits)

# #IndexError : List index out of range

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
# print(dirty_dozen)
# Then print out:

# print(dirty_dozen[0])
# print(dirty_dozen[1])
# # To see what happens at the next stage print out:

print(dirty_dozen[1][2])
# print(dirty_dozen[1][3])