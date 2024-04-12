# Treasure Map
line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]
map = [line1, line2, line3]
spot = input()

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
        line1[2] = "X"
    else:
        exit
elif number == "3":
    letter = spot[0].lower()
    if letter == "a":
        line3[0] = "X"
    elif letter == "b":
        line3[1] = "X"
    elif letter == "c":
        line1[2] = "X"
    else:
        exit
else:
    exit
print(f"{line1}\n{line2}\n{line3}")
