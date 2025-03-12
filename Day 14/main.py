#To Do 
#Create a loop which breaks when the answer is wrong
#Inside the loop, Show the logo each time 
#first compare two game data (random)
#second get an input of A or B
#third check the answer if it was right compare the answer to the next game data 
#score counter
import random
from game_data import data
from logo import logo,vs
import time

def answer_checker(answer,a,b):
    if a > b:
        result = "a"
        print("a:",a)
    else:
        result = "b"
        print("b ",b)
    if answer==result:
        win = True
    else:
        win = False
    return win


print(logo)
game=True
score = 0

while game==True:
    A = random.choice(data)
    print(f'Compare A: {A["name"]}, {A["description"]} ,{A["country"]} ')
    print(vs)
    B = random.choice(data)
    print(f'Compare B: {B["name"]}, {B["description"]} ,{B["country"]} ')
    while A==B:
        B = random.choice(data)
    answer = input("Who has more followers? Type A or B: ").lower()
    A_followers= A['follower_count']
    B_followers= B['follower_count']
    game = answer_checker(answer,A_followers,B_followers)
    if game==False:
        print(f"Sorry that's wrong! Final score: {score}")
        break
    score +=1
    print("That's correct! good job :))")
    time.sleep(2)
    print("\n\n")

