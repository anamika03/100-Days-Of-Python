# BMI Calculator
# BMI = weight (kg) / height^2 (m^2)

height = input("what's your height in meters? \n")
weight = input("What's your weight in KG's? \n")

BMI = float(weight) / ( float(height) ** 2 )


if BMI <= 18.5 :
    print(f"Your BMI is {round(BMI, 2)}, you are underweight.")
elif BMI <= 25:
    print(f"Your BMI is {round(BMI, 2)}, you have a normal weight.")
elif BMI <= 30:
    print(f"Your BMI is {round(BMI, 2)}, you are slightly overweight.")
elif BMI <= 35:
    print(f"Your BMI is {round(BMI, 2)}, you are obese.")
else:
    print(f"Your BMI is {round(BMI, 2)}, you are clinically obese.")

# print(round(BMI,2)) # 2 represents the number pricise after decimal
