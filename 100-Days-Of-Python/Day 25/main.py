# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
print(data["temp"])

# The two primary data structures in pandas are Series(1-dimensional) and DataFrame(2-dimensional)
print(type(data)) #data type is dataframe
print(type(data["temp"]))  #data type is series

data_dict = data.to_dict()
print(data_dict)
temp_list = data["temp"].to_list()
print(temp_list)
print(len(temp_list))
# average_temp = sum(temp_list) / len(temp_list)
# print(average_temp)

print(data["temp"].mean())  #average using pandas
print(data["temp"].max())   #max using pandas
print(data.temp)  # another way to access a column

# Get data in columns 
print(data[data.day == "Monday"])  # to get row where day is Monday
print(data[data.temp == data.temp.max()])  # to get row where temp is max

monday = data[data.day == "Monday"]
print(monday.temp)
monday_temp_F = (monday.temp * 9/5) + 32
print(monday_temp_F)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela", "John"],
    "scores": [76, 56, 65, 89],
    "rank": [2, 4, 3, 1]
}                   
data = pandas.DataFrame(data_dict)
# print(data)
data.to_csv("new_data.csv")  # to save dataframe to a csv file
