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
options = ["rock","paper","scissors"]

#Write your code below this line 👇

call = input("what do you choose? Type 0 for Rock, 1 for paper or 2 for scissors.")

if call == "0":
  print(rock)
elif call == "1":
  print(paper)
else:
  print(scissors)

computer_random = random.randint(0,2)

if computer_random == 0:
  print(rock)
elif computer_random == 1:
  print(paper)
else:
  print(scissors)

if call == "0" and computer_random == 2:
  print("You win, congratulations!")
elif call == "2" and computer_random == 1:
   print("You win, congratulations!")
elif call == "1" and computer_random == 0:
   print("You win, congratulations!")
elif call == "2" and computer_random == 0:
  print("You lose, try again!")
elif call == "0" and computer_random == 1:
  print("You lose, try again!")
elif call == "1" and computer_random == 2:
  print("You lose, try again!")
  
else:
    print("its a draw!")


