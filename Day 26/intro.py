name = "Angela"
new_list = [letter for letter in name]
print(new_list)

new_list = [2*n for n in range(1, 5)]
print(new_list)


import random
names = ["Hana", "Yana", "Gholi", "Asghar", "Jafar"]
new_names = [name.upper() for name in names if len(name) <= 4]
print(new_names)

students_random = {student: random.randint(1, 100) for student in names}
print(students_random)

passed_student = {student: score for (student, score) in students_random.items() if score>50}
print(passed_student)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
for (key, value) in student_dict.items():
    print(value)

