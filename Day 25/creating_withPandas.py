import pandas
# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "Scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

