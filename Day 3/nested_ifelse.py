print("Welcome to the rollercoaster!")
height = int(input("What's your height in cm? "))
age = int(input("what is your age? "))

if height >= 120:
    print("You can ride the rollercoaster")
    if age < 12:
        print("And you have to pay $5")
    elif age <= 18:
        print("And you have to pay $8")
    else:
        print("And you have to pay $14")
else:
    print("Sorry! You have to grow taller before you can ride ")
    