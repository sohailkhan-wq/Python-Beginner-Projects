import random

print("______________________________________________________________________")
print('''Game Rules:
01_ Rock wins against Scissors
02_ Paper wins against Rock
03_ Scissors wins against Paper''')

your_score = 0
opponent_score = 0
winner = 0

opponent_names = ["Asfand Yar", "Faizan", "Noman", "Sulaeman", "Ibrar"]
computer_name = random.choice(opponent_names)
opponent_bets = [50, 60, 80, 70, 100, 90]
computer_bet = random.choice(opponent_bets)


user_name = input("\nWhat's your name?  ")
user_bet = int(input("Make A Bet Between $10 - $100 ? $ "))
print("\nYour Opponent is: ", computer_name)
print(f"{computer_name} bet is: $" , computer_bet)
print(f"\n===========  {user_name} VS {computer_name}   ===========")

game_on = True
while game_on:
    your_choice = int(input("\nChoose any number 0 for Rock 1 for Paper 2 for Scissors:  "))
    opponent_choice = random.randint(0, 2)
    print(f"{computer_name} Chooses: {opponent_choice}\n")

    if your_choice == opponent_choice:
        print("The match ended in a draw.")
        
    elif your_choice == 0 and opponent_choice == 1: #!  rock vs paper
        opponent_score += 1
        print(f"Paper covers the Rock. \n{computer_name} scored {opponent_score} points")
        
    elif your_choice == 1 and opponent_choice == 2: #! paper vs scissors 
        opponent_score += 1
        print(f"Scissors cuts the Paper. \n{computer_name} scored {opponent_score} points")
        
    elif your_choice == 2 and opponent_choice == 0: #! scissors vs rock
        opponent_score += 1
        print(f"Rock smashes the Scissors. \n{computer_name} scored {opponent_score} points")
        
    elif your_choice == 1 and opponent_choice == 0: #! paper vs rock
        your_score += 1
        winner += 1
        print(f"Paper covers the Rock. \nYou scored {your_score} points")
        
    elif your_choice == 2 and opponent_choice == 1: #! scissors vs paper
        your_score += 1
        winner += 1
        print(f"Scissors cuts the Paper. \nYou scored {your_score} points")
        
    elif your_choice == 0 and opponent_choice == 2: #! rock vs scissors
        your_score += 1
        winner += 1
        print(f"Rock smashes the Scissors. \nYou scored {your_score} points")
        
    else:
        print("Sorry! Invalid Input")
    
    if winner == 5 and your_score == 5:
        print("\nCongrates! You Win the game🏆🥇")
        game_on = False
    elif opponent_score == 5:
        print("\nOops You Lose the game😥😥")
        game_on = False