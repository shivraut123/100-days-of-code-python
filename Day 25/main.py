#
#
# with open("weather_data.csv") as csvfile:
#     data = csvfile.readlines()
#     print(data)
#
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
# temp_list = data["temp"].to_list()
# print(temp_list)
# avg_temp = sum(temp_list) / len(temp_list)
# print(avg_temp)
# mean() - use to find avg
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["condition"])
# print(data.condition)

# Get Data in row
# print(data[data.day == "Monday"])
# print(data[data.condition == "Sunny"])
# print(data[data.temp == max(data.temp)])
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# print(monday.condition)

# monday_temp = data.temp[0]
# print(monday_temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# Create a Dataframe from Scratch
# data_dict = {
#     "students": ["Shiv","Shambhu","Tapan"],
#     "scores": [80,78,60]
# }
# data = pandas.DataFrame(data_dict)
# # print(data)
# data.to_csv("new_data.csv")

data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260819.csv")
fur_color = data["Primary Fur Color"].value_counts()

df=pandas.DataFrame(fur_color)
df.to_csv("./Squirrels_count.csv")


black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
# print(black_squirrels)
