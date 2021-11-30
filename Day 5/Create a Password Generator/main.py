import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Easy
easyPassword = ""

for x in range(0,nr_letters):
    letter = random.randint(0,len(letters) - 1)
    easyPassword += letters[letter]
for x in range(0,nr_numbers):
    number = random.randint(0,len(numbers) - 1)
    easyPassword += numbers[number]
for x in range(0,nr_symbols):
    symbol = random.randint(0,len(symbols) - 1)
    easyPassword += symbols[symbol]

print(f"Here is your easy password: {easyPassword}")

#Hard
hardPassword = ""
listEasyPassword = []
for x in easyPassword:
    listEasyPassword.append(x)

for x in range(0,len(listEasyPassword)):
    y = random.randint(0,len(listEasyPassword) - 1)
    hardPassword += listEasyPassword[y]
    listEasyPassword.remove(listEasyPassword[y])

print(f"Here is your hard password: {hardPassword}")