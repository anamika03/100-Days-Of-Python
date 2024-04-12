import random

names = input("Names of your friend: ").split(", ")
num_item = len(names)
random_names = random.randint(0, num_item-1)
print(f"{names[random_names]} is going to pay the bill.")

