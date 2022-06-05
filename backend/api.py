# api requests

from fastapi import FastAPI
import json

app = FastAPI()

auctions = []
price_sort = []
end_sort = []

# TODO : make the loading and refreshing (backend.py) periodically happen
@app.on_event("startup")
async def startup_event():
    loadsave()

# load the saved data from files
def loadsave():
    # load the data from the json files
    global auctions
    global price_sort
    global end_sort
    with open("save/auctionssave.json", "r", encoding="utf-8-sig") as f:
        auctions = json.load(f)
    with open("save/pricesortsave.json", "r", encoding="utf-8-sig") as f:
        price_sort = json.load(f)
    with open("save/endsortsave.json", "r", encoding="utf-8-sig") as f:
        end_sort = json.load(f)


# auction house api
@app.get("/auctionhouse")
def auctions(amount: int = 36, sort: str = "low", category: str = "any", search: str = "", rarity: str = "any", binfilter: str = "any"):
    print("recieved request for: amount: " + str(amount) + ", sort: " + sort + ", category: " + category + ", search: " + search.replace("_", " ") + ", rarity: " + rarity + ", bin: " + binfilter)
    return{"data":filterauctions(amount, sort, category, search.replace("_", " "), rarity, binfilter)}

#filter the autions with the requested parameters
def filterauctions(amount, sort, category, search, rarity, binfilter):
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
        
        founditems.append(item)
        founditemcount += 1
        if founditemcount == amount :
            break
    return(founditems)