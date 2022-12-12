import os

bids = {}
keep_adding = True

def theWinner():
    highest_bid = 0
    winner = ""

    for bidders in bids:
        amount = bids[bidders]
        if amount > highest_bid:
            highest_bid = amount
            winner = bidders
    print(f"The winner is {winner} with a bid amount of $ {highest_bid}.")

while keep_adding:
    name = input("Enter you name:  ")
    bid_amount = int(input("Enter your bid amount:  "))
    bids[name] = bid_amount

    other_bidders = input("Type 'Yes' if there are other bidders and 'No' if not:  ").lower()

    if other_bidders == 'no':
        theWinner()
        keep_adding = False
    elif other_bidders == 'yes':
        os.system('cls')
        keep_adding = True
    else:
        print("Invalid Input")
        keep_adding = False