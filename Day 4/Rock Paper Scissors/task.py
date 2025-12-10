from operator import index
from urllib.parse import uses_relative

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
game_images=[rock,paper,scissors]

user_choice=int(input("Type O for Rock, 1 for paper or 2 for scissors\n"))
print(game_images[user_choice])
if user_choice >=3 or user_choice < 0:
    print("invalid no")
else:
    print(f'You chose:{user_choice}')

computer_choice=random.randint(0,2)
print(game_images[user_choice])
print(f'computer chose:{computer_choice}')

if user_choice==0 and computer_choice==2:
    print("You Win!")
elif user_choice==1 and computer_choice==0:
    print("You Win!")
elif user_choice==2 and computer_choice==1:
    print("You win!")
elif user_choice==computer_choice:
    print("It's Draw!")

else:
    print("You lose!")
