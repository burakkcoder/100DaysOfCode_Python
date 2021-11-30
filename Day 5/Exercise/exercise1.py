# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
total = 0
for n in range(0, len(student_heights)):
  total += int(student_heights[n])

print(round(total / len(student_heights)))

