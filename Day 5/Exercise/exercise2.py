# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
bigger = 0
for n in range(0, len(student_scores)):
  if bigger < int(student_scores[n]):
    bigger = int(student_scores[n])

print(f"The highest score in the class is: {bigger}")