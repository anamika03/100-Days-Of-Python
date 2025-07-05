# Treasure Map
line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]
map = [line1, line2, line3]

# Valid input positions
valid_spots = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]

# Keep asking until input is valid
while True:
    spot = input("Where do you want to put the treasure? (e.g., a1, b2, c3): ").lower()
    if spot in valid_spots:
        break
    print("❌ Invalid input. Please enter one of: a1, a2, a3, b1, b2, b3, c1, c2, c3")

print("Hiding your treasure! X marks the spot.")

number = spot[1]
if number == "1":
    letter = spot[0].lower()
    if letter == "a":
        line1[0] = "X"
    elif letter == "b":
        line1[1] = "X"
    elif letter == "c":
        line1[2] = "X"
    else:
        exit
elif number == "2":
    letter = spot[0].lower()
    if letter == "a":
        line2[0] = "X"
    elif letter == "b":
        line2[1] = "X"
    elif letter == "c":
        line2[2] = "X"
    else:
        exit
elif number == "3":
    letter = spot[0].lower()
    if letter == "a":
        line3[0] = "X"
    elif letter == "b":
        line3[1] = "X"
    elif letter == "c":
        line3[2] = "X"
    else:
        exit
else:
    exit
print(f"{line1}\n{line2}\n{line3}")
