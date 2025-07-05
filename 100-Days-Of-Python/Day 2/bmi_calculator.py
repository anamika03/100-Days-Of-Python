# BMI = weight (kg) / height^2 (m^2)

height = input("what's your height in meters? \n")
weight = input("What's your weight in KG's? \n")

BMI = int(weight) / ( float(height) ** 2 )
print(round(BMI,2)) # 2 represents the number pricise after decimal
