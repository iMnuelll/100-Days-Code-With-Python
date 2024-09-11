import os
from art import logo

print(logo)
biddersData = []
loops = False

def checkBidders() :
    bidderBid = 0
    bidIndex = 0
    bidderWinner = {}
    for bidder in biddersData :
        if bidder['bidPrice'] > bidderBid :
            bidderWinner = bidder
        bidderBid = bidder['bidPrice']
        bidIndex += 1
    print(f"The winner is {bidderWinner['name']} with a bid of ${bidderWinner['bidPrice']}")    

while loops is not True :
    askName = input("What's your name? ")
    askBidPrice = int(input("What's your bid price : $"))
    biddersData.append({'name' : askName, 'bidPrice' : askBidPrice})
    anyBidders = input("Are there any bidders? Type 'yes' or 'no'\n")
    if anyBidders == "yes" :
        loops = False
        os.system('cls||clear')
    else :
        loops = True

os.system('cls||clear')

checkBidders()