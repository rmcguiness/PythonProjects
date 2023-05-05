#Using just file methods
with open("./weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)


#Using csv library
import csv

with open("./Weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)


# Using the pandas library
import pandas

data = pandas.read_csv("./weather_data.csv")
print(type(data))
print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))

print(data["temp"].mean())
print(data["temp"].max())