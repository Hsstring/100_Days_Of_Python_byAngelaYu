import os
import logo 
print(logo.logo)
bidders = []

def add_bidder(given_name, given_money):
    bidder = {
        "name":given_name,
        "bid" :given_money
    }
    bidders.append(bidder)


# main 
continue_bid = "yes"
winner_price =0 
while continue_bid=="yes":
    print("Welcome to the auction program.")
    name = input("What is your name? ")
    bid = int(input("What's your bid? $"))
    add_bidder(name,bid)
    if bid>winner_price:
        winner_price = bid
        winner = name
    continue_bid = input("Are there any bidders? (yes/no) ")
    os.system('cls||clear')

print(f"The winner is {winner} with a bid of ${winner_price}")
