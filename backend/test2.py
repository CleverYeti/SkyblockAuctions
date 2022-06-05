# testing for random stuff

import requests
import json

auctions = []
price_sort = []
end_sort = []

def loadsave():
    # load the data from the json files
    global auctions
    global price_sort
    global end_sort
    with open("backend/save/auctionssave.json", "r") as f:
        auctions = json.load(f)
    with open("backend/save/pricesortsave.json", "r") as f:
        price_sort = json.load(f)
    with open("backend/save/endsortsave.json", "r") as f:
        end_sort = json.load(f)

loadsave()
print(auctions[0]["bids"])