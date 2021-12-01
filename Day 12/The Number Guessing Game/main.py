import random
import art

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1,100)
easy_hard = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
lives = 10

if easy_hard == "hard":
    lives = 5
    print("You have 5 attempts remaining to guess the number.")
else:
    print("You have 10 attempts remaining to guess the number.")

while True:
    if lives == 0:
        print("You've run out of guesses, you lose.")
        break
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You got it! The answer was {number}")
        break
    elif guess < number:
        print("Too low")
        print("Guess again")
        lives -= 1
        print(f"You have {lives} attempts remaining to guess the number.")
    elif guess > number:
        print("Too high")
        print("Guess again")
        lives -= 1
        print(f"You have {lives} attempts remaining to guess the number.")

