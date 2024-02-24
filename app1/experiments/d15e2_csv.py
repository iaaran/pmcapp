import csv


with open("files/weather.csv", 'r') as file:
    data = list(csv.reader(file))

for row in data:
    print(f"|  {row[0]}       |    {row[1]}")
