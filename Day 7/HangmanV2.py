import random
print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/      
""")
# 7 stages of hangman: 
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

lives = 6
word_list = ["ali", "hannah", "asghar","akbar","zoleikha"]
chosen_word = random.choice(word_list)

display =[]
for blank in chosen_word:
    display.append("_")
print(display)

flag = True
while flag:
    guess = input("Guess a letter: \n").lower()
    index=0
    for letter in chosen_word:
        if letter==guess:
            display[index]=letter
        index+=1

    if guess not in chosen_word:
        lives-=1   
        print(HANGMANPICS[6-lives])
        if lives==0:
            print("You lost!")
            print(f"The word was {chosen_word}")
            break


    print(f"{''.join(display)}") 

    if "_" not in display:
        flag = False
        print("You won!")
        break


