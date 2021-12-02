import art
import game_data
import random

score = 0

while True:
    print(art.logo)

    comperaA = random.choice(game_data.data)
    againstB = random.choice(game_data.data)
    if comperaA == againstB:
        againstB = random.choice(game_data.data)

    print(f"Compare A: {comperaA['name']}, {comperaA['description']}, from {comperaA['country']}")
    print(art.vs)
    print(f"Against B: {againstB['name']}, {againstB['description']}, from {againstB['country']}")

    question = input("Who has more followers? Type 'A' or 'B': ")

    if question == "A" and comperaA["follower_count"] > againstB["follower_count"]:
        score += 1
    elif question == "B" and comperaA["follower_count"] < againstB["follower_count"]:
        score += 1
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        break

    print(f"You're right! Current score: {score}")