import ASCII_art as sap_art
import os

def secret_auction_program():
    
    # Printing the ASCII art of gavel
    print(sap_art.secret_auction_art)

    print("Welcome to the Secret Auction Program.\n")

    # Initializing empty ledger
    secret_ledger = []

    other_bidders = 'yes'    
    while other_bidders == 'yes':
        # Asking for the details of biddings: 
        name = input("What is your name?: ")
        bid = int(input("What's your bid?: $"))

        # Calling ledger update function:
        sl_update(name, bid, secret_ledger)

        other_bidders = input("Are there any other bidders? Type \'yes\' or \'no\'.\n")

        if other_bidders == 'yes':
            os.system('cls')
    
    max_bid = 0
    win_name = ""
    for i in secret_ledger:
        if i['amount'] > max_bid:
            max_bid = i['amount']
            win_name = i['name']
    
    # Printing the final Winner with Amount after clearing the screen:
    os.system('cls')
    print(f'The winner is {win_name} with a bid of ${max_bid}.')

def sl_update(bidder_name, bid_amt, secret_ledger):
    ledger_update = {}
    ledger_update['name'] = bidder_name
    ledger_update['amount'] = bid_amt
    secret_ledger.append(ledger_update)

# Driver Code:
secret_auction_program()