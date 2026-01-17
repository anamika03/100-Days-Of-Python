# List Comprehensions
# list = [new_item for item in list]

list = [1, 2, 3, 4, 5]
squared_list = [n**2 for n in list]
print(squared_list)
new_list = [n+1 for n in list]
print(new_list)

name = "Anamika"
letters_list = [letter for letter in name]
print(letters_list)

number_list = [n*2 for n in range(1, 5)]
print(number_list)

# Conditional List Comprehensions
# list = [new_item for item in list if test]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)

