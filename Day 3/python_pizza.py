#Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.
print("Thank you for choosing Python Pizza Deliveries! ")

bill = 0
users = input("Which size of pizza do you want? S, M or L : ")

if users == "S":
    bill = 15
elif users == "M":
    bill = 20
else:
    bill = 25

toppings = input(f"Want to add pepperoni? Y or N : ")
if toppings == "Y":
    if users == "S":
        bill += 2
    else:
        bill += 3

cheese = input("Want to add extra cheese? Y or N : ")
if cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}. ")

