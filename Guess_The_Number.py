import random

print("--------------------- WELL COME TO GUESS THE NUMBER GAME! --------------------------")
print("""\nGame Rules:
1_ In an easy level you have to guess the actual number only in 10 attempts otherwise You Lose.
2_ In a hard level you have to guess the actual number only in 5 attempts otherwise You Lose.            
3_Don't repeat a number.
4_Type your iuput in lowercase.
Note: Keep an eye on the rules while playing the game.
                    ===== Good Luck! =====""")

level_choice = input("""\nWhich Level would you like to play.
Type 'easy' for the EASY LEVEL. || OR || Type 'hard' for HARD LEVEL. """)

computer_choice  = random.randint(1, 100)
  
def easy():   
    attempts = 0
    end_game = True  
    
    while end_game:  
        user_choice = int(input("\nEnter your guess:  "))
        attempts += 1
    
        if attempts == 10:
            end_game = False     
            print("You exceeds the attempt limit. You Lose!")  
            break;
             
        if user_choice > computer_choice:
            print ("\nYour guess is higher than the actual number. Try a lower guess.")
        
        elif user_choice < computer_choice:
            print ("Your guess is lower than the actual number. Try a higher guess.")

        elif user_choice == computer_choice:
            print(f"You guessed it in {attempts} attempts. Congrates You Win!")
            break;
            
computer_choice  = random.randint(1, 100)

def hard():   
    attempts = 0
    end_game = True  
  
    while end_game:      
        user_choice = int(input("\nEnter your guess:  "))
        attempts += 1
        
        if attempts == 5:
            end_game = False     
            print("You exceeds the attempt limit. You Lose!")  
            break;
                        
        if user_choice > computer_choice:
            print ("\nYour guess is higher than the actual number. Try a lower guess.")
        
        elif user_choice < computer_choice:
            print ("Your guess is lower than the actual number. Try a higher guess.")

        elif user_choice == computer_choice:
            print(f"You guessed it in {attempts} attempts. Congrates You Win!")
            break;
    

if level_choice == 'easy':
    easy()
elif level_choice == "hard":
    hard()
else:
    print("Invalid!")