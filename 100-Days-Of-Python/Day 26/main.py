# List Comprehensions
# list = [new_item for item in list]

list = [1, 2, 3, 4, 5]
squared_list = [n**2 for n in list]
print(squared_list)
new_list = [n+1 for n in list]
print(new_list)

name = "Anamika"
letters_list = [letter for letter in name]
print(letters_list)

number_list = [n*2 for n in range(1, 5)]
print(number_list)

# Conditional List Comprehensions
# list = [new_item for item in list if test]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)

# Dictionary Comprehensions
# new_dict = {new_key: new_value for item in list}

import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {name: random.randint(1, 100) for name in names}
print(students_scores)
# passed_students = {name:score for (name,score) in students_scores.items() if score >= 60}
# print(passed_students)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word: len(word) for word in sentence.split()}
# print(result)

# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# weather_f = {day:temp_c * 9/5 + 32 for (day,temp_c) in weather_c.items()}
# print(weather_f)

# # Looping through a Dictionary
# for (key, value) in weather_c.items():
#     print(f"{key}: {value}°C")

import pandas
student_data_frame = pandas.DataFrame(students_scores.items(), columns=["student", "score"])
print(student_data_frame)

# Loop through rows of a DataFrame
# for (key, value) in student_data_frame.items():
#     print(f"{key}: {value}") or print(value)

for (index, row) in student_data_frame.iterrows():
    print(f"{row.student}: {row.score}")