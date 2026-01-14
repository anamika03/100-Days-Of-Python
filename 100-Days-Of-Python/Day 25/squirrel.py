import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Data.csv")
data["Primary Fur Color"] == "Gray"
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(gray_squirrels_count)
print(black_squirrels_count)
print(cinnamon_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray_squirrels_count, black_squirrels_count, cinnamon_squirrels_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
