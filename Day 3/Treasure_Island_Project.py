# Treasure Island Project
print("Welcome to Treasure Island!")
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
              ''')
print("Your mission is to find the treasure.")
turn= input("you are at a crossroad, where do you want to go? left or right? ").lower()
if turn=="left":
    action = input("you've come to a lake. There is an island in the middle of the lake.Swim or wait?").lower()
    if action=="wait":
        door = input("Congragulations! you arrve at the island unharmed. There is a house with 3 doors. Which door you open?(RED,BLUE,YELLOW)").lower()
        if door=="red":
            print("It's a room full of pirate zombies!!.....\nGAME OVER!")
        elif door=="blue":
            print("You enter a room of witches!!!.....\nGAME OVER!")
        elif door=="yellow":
            print("Treasure is here!!\nYOU WON!!!!")
            print("""
                  (>,  oo      
            /  8 "} > @ <
            |`.8 .-._/| 
            `-.'`')`_.'
               ) /    
              /  |__,      
              |    ( /   
            .'    , /  
             `._/  '`- 
              \|        
         --  -`' -        --- 
            """)
        else:
            print("GAME OVER!")
    else:
        print("Attacked by trout......\nGAME OVER!")
else:
    print("Fall into a hole......\nGAME OVER!")