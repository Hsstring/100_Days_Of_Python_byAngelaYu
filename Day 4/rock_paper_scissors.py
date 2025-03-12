rock = """
 _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissors = """
_______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
import random
play = [rock, paper, scissors]

print("Rock, Paper, Scissors!")
player = int(input("Rock ->1 & Paper ->2 & scissors ->3 \n which one you choose? "))
if player>3:
    print("you've entered an invalid number, thus you loose!")
player = play[player-1]
computer = random.choice(play)
print(f"you:\n{player}")
print(f"computer:\n{computer}")
if player==rock :
    if computer==rock:
        print("Equal!") 
    elif computer==paper:
        print("You lost!")
    else:
        print("You Won!")
elif player ==paper:
    if computer==rock:
        print("You Won!") 
    elif computer==paper:
        print("Equal!")
    else:
        print("You Lost!")
else:
    if computer==rock:
        print("You Lost!") 
    elif computer==paper:
        print("You Won!")
    else:
        print("Equal!")
