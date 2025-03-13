import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data)) dataframe - 2 dimensional
# print(type(data["temp"])) series - 1dimensional
# sum = 0
# count = 0
# data_dict = data.to_dict()
# for temp in data_dict["temp"]:
#     sum += data_dict["temp"][count]
#     count += 1
#
# average = round((sum / count), 2)
# print(average)
print("The average of temperatures:", end='')
print(data["temp"].mean())
print(data["temp"].max())

# Get Data in Columns
print("Getting the data in columns: ")
"""print(data["condition"])"""
print(data.condition)

# Get Data in Row
print("Getting the data in rows:  ")
print(data[data.day == "Monday"])
print("\nGetting the row with the highest temperature: ")
highest_temp = data[data.temp == data["temp"].max()]
print(highest_temp)

# A particular thing in a particular row
print("\nGetting actual condition for the particular day 'monday'")
monday = data[data.day == "Monday"]
print(monday.condition)
fahrenheit = (monday.temp[0] * 9/5) + 32
print(f"The temperature in fahrenheit: {fahrenheit}")

