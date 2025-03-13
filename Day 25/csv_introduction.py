# with open("weather_data.csv") as datafile:
#     data = datafile.readlines()
#     print(data)

import csv
with open("weather_data.csv") as datafile:
    data = csv.reader(datafile)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)