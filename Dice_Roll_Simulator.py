import random

user_choice = random.randint(1, 6)
computer_choice = random.randint(1, 6)

print("\nRolling The Dice...")
print("\nThe Values are: ")
print(f"\nYour Number: {user_choice} || Computer Number: {computer_choice}")

if user_choice > computer_choice:
    print("\nCongratulations You Win!")
elif user_choice < computer_choice:
    print("\nOops You Lose!")
else:
    print("\nTie!")