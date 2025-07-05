# 4. Fix the errors.

try:
    age = int(input("What is your age? "))
except ValueError:
    print("Youv'e typed an invalid number. Please try again with a numeric response such as 15")
    age = int(input("What is your age? "))

if age > 18:
    print(f"Your'e drive at age {age}.")
