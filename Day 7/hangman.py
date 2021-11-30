import random
import hangman_art
import hangman_words

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
lives = 6

print(f"Psst,the solution is {chosen_word}.")

display = []

for letter in chosen_word:
    display.append("_")

print(display)

while "_" in display:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for index in range(len(chosen_word)):
        letter = chosen_word[index]
        if letter == guess:
            display[index] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        print(f"{lives} lives left!")
        if lives == 0:
            print(hangman_art.stages[lives])
            print("You lose.")
            break

    print(f"{' '.join(display)}")

    if "_" not in display:
        print("You win.")
        break

    print(hangman_art.stages[lives])