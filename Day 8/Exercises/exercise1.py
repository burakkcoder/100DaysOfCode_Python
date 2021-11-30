import math
#Write your code below this line 👇
def paint_calc(height,width,cover):
    cans = int(math.ceil((height * width) / cover))
    print(f"You'll need {cans} cans of paint.")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = float(input("Height of wall: "))
test_w = float(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)