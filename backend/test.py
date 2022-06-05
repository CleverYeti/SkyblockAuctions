# item search testing

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

def filterauctions(amount, sort, category, search, rarity, binfilter):
    print('filterauctions function called')
    # filter the auctions with the inputted properties
    global auctions
    global price_sort
    global end_sort
    founditems = []
    founditemcount = 0

    # copy the right sort into a list
    if sort == "low" :
        activesort = price_sort
    elif sort == "high":
        activesort = reversed(price_sort)
    else :
        activesort = end_sort
    
    # check all the items until enough are found
    for i in activesort :
        item = auctions[i]
        if category != "any" :
            if category != item["category"] :
                continue
        if search != "" :
            if not search.lower() in item["item_name"].lower() :
                continue
        if rarity != "any" :
            if rarity != item["tier"] :
                continue
        if binfilter == "bin" and item["bin"] == "false" :
            continue
        if binfilter == "auctions" and item["bin"] == "true" :
            continue
        
        founditems.append(i)
        founditemcount += 1
        if founditemcount == amount :
            break
    return(founditems)

loadsave()
print(filterauctions(10, "low", "any", "shadow assassin", "any", "any"))
print("test")