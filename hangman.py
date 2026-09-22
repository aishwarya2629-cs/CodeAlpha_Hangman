import random

words = ["python", "computer", "program", "coding", "developer"]

word = random.choice(words)
guessed_word = ["_"] * len(word)

incorrect_guesses = 0
guessed_letters = []

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.")

while incorrect_guesses < 6 and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Guessed letters:", guessed_letters)
    print("Incorrect guesses:", incorrect_guesses, "/ 6")

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess

    else:
        incorrect_guesses += 1
        print("Wrong guess!")

if "_" not in guessed_word:
    print("\nCongratulations!")
    print("You guessed the word:", word)
else:
    print("\nGame Over!")
    print("The word was:", word)
    