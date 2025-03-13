import pandas

student_dict = {
    "student": ["Hana", "Yana", "Zizi"],
    "score": [56, 76, 98]
}
# Loop through dictionaries:
student_dataframe = pandas.DataFrame(student_dict)
for (index, row) in student_dataframe.iterrows():
    if row.student == "Zizi":
        print(row.score)
