fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    fruit = fruits[index]
    print(fruit + " pie")


answer = int(input("Index ?: "))
try:
    make_pie(answer)
except:
    print("Fruit pie")