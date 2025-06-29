
import random

def hangman():
    words = ["apple", "banana", "orange", "grape", "mango"]
    word = random.choice(words)
    guessed = "_" * len(word)
    guessed = list(guessed)
    attempts = 6
    guessed_letters = []

    print("Welcome to Hangman!")
    print("Word:", " ".join(guessed))

    while attempts > 0 and "_" in guessed:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
            print("Correct! Word:", " ".join(guessed))
        else:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")

    if "_" not in guessed:
        print("🎉 You won!")
    else:
        print(f"😞 You lost. The word was: {word}")

hangman()
