import random

# number = [1, 2, 3]
# new_numbers = [x + 1 for x in number]
# print(new_numbers)

# name = "Burak"
# new_name = [x for x in name]
# print(new_name)

# number_list = [x * 2 for x in range(1, 5)]
# print(number_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# short_names = [x for x in names if len(x) < 5]
# print(short_names)

students_scores = {x:random.randint(0, 100) for x in names}
passed_students = {x:y for (x,y) in students_scores.items() if y > 75}
print(students_scores)
print(passed_students)