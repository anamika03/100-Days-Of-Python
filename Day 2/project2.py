# Tip Calculator

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, 15 or 20? "))
split = int(input("How many ople to split the bill? "))

tip_in_percent = (tip * bill ) / 100

pay = (bill + tip_in_percent) / split
print(f"Each person should pay: ${round(pay,2)}")

