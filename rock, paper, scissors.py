#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''Popular game originating from china, usually played between two people, forming one of three shaped with
an outstreched hand. The game has three possible outcomes: a win, a loss or a draw, rock beats scissors, but losses to a paper,
scissors beats paper and paper beats rock.'''


# import nessesary module
import random

# assign variables

user_guess = 0
computer_guess = 0
draw_count = 0

options = ["rock", "paper", "scissors"]

# infinite loop checking certian conditions and incrementing variables until it breaks (when user quits the game)

while True:
    pick = input("Choose Rock/Paper/Scissors or Q to quit ").lower()
    if pick == "q":
        break

    if pick not in options:
        continue
        
    ran_num = random.randint(0, 2)
    comp_pick = options[ran_num]
    
    print("computer picked", comp_pick)

    if pick == "rock" and comp_pick == "scissors":
        print("You won")
        user_guess += 1
    elif pick == "paper" and comp_pick == "rock":
        print("You won")
        user_guess += 1
    elif pick == "scissors" and comp_pick == "paper":
        print("You won")
        user_guess += 1
    elif pick == comp_pick:
        print("It's a draw")
        draw_count += 1
    else:
        print("Computer wins")
        computer_guess += 1
print("Game Over")  
print()

# check for spelling correctness

if user_guess <= 1:
    print("You scored", user_guess, "point")
else:
    print("You scored", user_guess, "points")

if computer_guess <= 1:
    print("Computer scored", computer_guess, "point")
else:
    print("Computer scored", computer_guess, "points")        
    

print("Number of draws", draw_count)
print()

# check who has more points and announce the winner

if user_guess > computer_guess:
    print("You won the game")    
elif user_guess < computer_guess:
    print("Computer won the game")    
else:    
    print("The game ended in a draw")


# In[ ]:




