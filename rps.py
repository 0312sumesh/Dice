import random
from time import sleep

i = 1
print('Game starts in')
for i in range(1,4):
   print(i)
   i = i+1
   sleep(1)

possible_action = ['r', 'p', 's']
user_action = input('enter a choice (paper => p, rock => r, scissors => s):')
computer_action = random.choice(possible_action)

print(f'oppoents choice:::::{computer_action}')

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "r":
    if computer_action == "s":
        print("rock smashes scissors! You win!")
    else:
        print("paper covers rock! You lose.")
elif user_action == "p":
    if computer_action == "r":
        print("paper covers rock! You win!")
    else:
        print("scissors cuts paper! You lose.")
elif user_action == "s":
    if computer_action == "p":
        print("scissors cuts p! You win!")
    else:
        print("rock smashes scissors! You lose.")
            


