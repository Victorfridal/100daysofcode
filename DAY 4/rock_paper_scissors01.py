import random

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
options = [rock,paper,scissors]

user_options = int(input("what do you choose? Type 0 for Rock, 1 for paper or 2 for scissors.\n"))

if user_options >= 3 or user_options < 0:
    print("You typed an invalid number, you lose!")
else:
    print(options[user_options])
#select the rest of the code at this point and hit tab button
    computer_options = random.randint(0,2)
    print("computer picked")
    print(options[computer_options])

    if user_options == 0 and computer_options == 2:
        print("You win!")
    elif computer_options == 0 and user_options == 2:
        print("You lose!")
    elif computer_options > user_options:
        print("You lose")
    elif user_options > computer_options:
        print("You win!")
    elif computer_options == user_options:
        print("its a draw")