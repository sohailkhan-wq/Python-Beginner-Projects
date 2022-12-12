import random
from HangMan_art import stages

words_list = ["code", "python", "developer", "development", "feelings", "website"]
choosen_word = random.choice(words_list)
print(choosen_word)

correct_word = []

for letters in choosen_word:
    correct_word.append("_")

game_on = True
lives = 6

while game_on:

    guess = input("\nGuess A Letter: ").lower()

    for index in range(len(choosen_word)):
        letter = choosen_word[index]

        if letter == guess:
            correct_word[index] = letter
    print("You guessed a correct letter. But don't repeat it")
    print(' '.join(correct_word))


    if "_" not in correct_word:
        print("\nCongratulations! You Win!")
        game_on = False

    if guess not in correct_word:
        lives -= 1
        print(f"\nIncorrect Guess. You Lose A Life. Now You have {lives} lives remaining")

    if lives == 0:
        print("\nOops! You Lose.")
        game_on = False

    print(stages[lives])