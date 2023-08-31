import random
from re import I

choices = ['rock', 'paper', 'scissors']
user_score = 0
computer_score = 0
tries = 6


def Game(user, computer):
    global user_score
    global computer_score
    global tries
    print(f"You chose {user}, computer chose {computer}")
    if user == computer:
        print(f"Both players selected {user}. It is a tie!\n")
        tries -=1 
    elif user == 'rock':
        if computer == 'scissors':
            user_score += 1
            tries -=1 
            print("Rock smashes scissors!")
        else:
            computer_score += 1
            tries -=1 
            print("Paper covers rock!")
    elif user == 'paper':
        if computer == 'rock':
            user_score += 1
            tries -=1 
            print("Paper covers rock!")
        else:
            computer_score += 1
            tries -=1 
            print("Scissors cuts paper!")
    elif user == 'scissors':
        if computer == 'paper':
            user_score += 1
            tries -=1 
            print("Scissors cuts paper!")
        else:
            computer_score += 1
            tries -=1 
            print("Rock smashes scissors!")



while tries != 0:
    
    user_choice = input("Enter a choice (rock, paper, scissors): ").lower()
    computer_choice = random.choice(choices)

    if  user_choice in choices:
        Game(user_choice, computer_choice)
    else:
        print("You chose a wrong choice, please try again :(")

if user_score > computer_score:
        print("Your score longer than computer score. You WIN :) \n")
        exit()
elif computer_score > user_score :
         print("Computer score longer than your score. You LOSE :( \n")
         exit()
elif computer_score == user_score:
        print("Tie")
    
   
    
    
