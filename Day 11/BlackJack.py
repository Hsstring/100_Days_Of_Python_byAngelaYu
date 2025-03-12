import logo
import random 



def blackjack():
    print(logo.logo)
    user_cards, computer_cards = [],[]

    user_cards = get_card(user_cards,2)
    computer_cards = get_card(computer_cards,2)

    user_score = score_calculator(user_cards)
    computer_score = score_calculator(computer_cards)

    print(f"your cards: {user_cards}, current score : {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    if user_score<17:
        user_cards, user_score=another(user_cards, user_score)
        print("Your score is under 17 so You have to pick another card!\n")
        print(f"Your new hand: {user_cards}, current score: {user_score}")
    elif computer_score < 17:
        computer_cards, computer_score =another(computer_cards,computer_score)
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if another_card=='y':
        user_cards, user_score=another(user_cards, user_score)
    
    print(f"Your final hand: {user_cards}, final score {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score {computer_score}")

    winner_decision(user_score, computer_score)


def get_card(client,times):
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    for i in range(times):
        client.append(random.choice(cards))
    return client

def score_calculator(card_list):
    score = 0
    for card in card_list:
        score += card
    return score

def winner_decision(score1,score2):
    if score1> score2 and score1<=21:
        print("You Won!")
    if score1 == score2:
        print("Draw!")
    if score2>score1 or score1 > 21:
        print("You lost, Sorry!")

def another(card, score):
    card = get_card(card,1)
    score = score_calculator(card)
    return card, score

stop = False
while not stop:
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': " )
    if play=='y':
        blackjack()
    else:
        stop = True

# main body works
# few modifications needed :
# first revealing winner mistakes
# second add the condition that score<17
# third add the winner condition reaching 21

