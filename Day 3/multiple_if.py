print("Welcome to the rollercoaster!")
height = int(input("What's your height in cm? "))
bill = 0

if height >= 120:
    age = int(input("what is your age? "))
    if age < 12:
        bill = 5
        print("Child ticket prize is $5")
    elif age <= 18:
        bill = 7
        print("Teenage ticket prize is $7")
    else:
        bill = 12
        print("Adult ticket prize is $12")

    photos = input("Do you want a photo taken? Y or N. ")
    if photos == "Y":
        bill += 3    
    print(f"Your final bill is ${bill} ")

else:
    print("Sorry! You have to grow taller before you can ride ")
    