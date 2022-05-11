
from cmath import log
import requests
import json

# amount of auction per page
page_length = 36

# if the api keys is invalid just put a new one
# each api key has a max of 65 requests per minute
# the api keys need to be made by 2 different minecraft accounts
main_api_key = ""
second_api_key = ""
current_key = ""

#api address
hypixel_api = "https://api.hypixel.net/skyblock/auctions"

auctions = []
price_sort = []
end_sort = []

# function that reloads the entire data
def reloadauctions():
    print('reloadauctions function called')
    fetchauctions()
    # print(auctiondata)
    sortauctions()
    copyprocesseddata()

# fetch auction pages from the hypixel api
def fetchauctions():
    print('fetchauctions function called')
    # init variables
    global main_api_key
    global second_api_key
    global auctiondata
    auctiondata = []
    current_key = main_api_key

    # fetch the first page
    jsonresponse = fetchpage(0, current_key)

    # todo: add better error handling
    if jsonresponse["success"] == "false" :
        print("fetching error on page " + str(0))
        return()

    print("fetched page 0")
    auctiondata = auctiondata + jsonresponse["auctions"]
    totalpages = jsonresponse["totalPages"]

    #fetch all the other pages
    for current_page in range(totalpages - 1):
        jsonresponse = fetchpage(current_page + 1, current_key)
        if jsonresponse["success"] == "false" :
            print("fetching error on page " + str(current_page))
            return()
        print("fetched page" + str(current_page))
        auctiondata = auctiondata + jsonresponse["auctions"]
        # switch api key for cooldown
        if current_page == 59 :
            current_key = second_api_key



# todo: move this before fetchauctions
def fetchpage(page, key):
    global hypixel_api
    headers = {"api": key, "page": page}
    response = requests.get(hypixel_api + "?page=" + str(page))
    return json.loads(response.text)

# sort algorithm
def binary_search(arr, val, start, end):
    if start == end:
        if arr[int(start)] > val:
            return start
        else:
            return start+1
  
    if start > end:
        return start
  
    mid = (start+end)/2
    if arr[int(mid)] < val:
        return binary_search(arr, val, mid+1, end)
    elif arr[int(mid)] > val:
        return binary_search(arr, val, start, mid-1)
    else:
        return mid

# sort the auctions by price and end time
def sortauctions():
    print('sortauctions function called')
    # sort the data into two lists, sorted by price and end time

    global auctiondata
    global price_sort
    global end_sort
    global temp_price_sort
    global temp_end_sort
    
    # sort by price
    temp_price_sort = []
    tempsort = []
    i = 0
    for current_auction in auctiondata:
        if current_auction["highest_bid_amount"] != 0:
            sortpos = int(binary_search(tempsort, current_auction["highest_bid_amount"], 0, len(tempsort) - 1))
            tempsort.insert(sortpos, current_auction["highest_bid_amount"])
        else:
            sortpos = int(binary_search(tempsort, current_auction["starting_bid"], 0, len(tempsort) - 1))
            tempsort.insert(sortpos, current_auction["starting_bid"])
        temp_price_sort.insert(sortpos, i)
        i += 1

    # sort by end
    temp_end_sort = []
    tempsort = []
    i = 0
    for current_auction in auctiondata:
        sortpos = int(binary_search(tempsort, current_auction["end"], 0, len(tempsort) - 1))
        tempsort.insert(sortpos, current_auction["end"])
        temp_end_sort.insert(sortpos, i)
        i += 1

# copy the processed data into the active lists
def copyprocesseddata():
    print('copyprocesseddata function called')
    global auctions
    global price_sort
    global end_sort
    global temp_price_sort
    global temp_end_sort

    auctions = auctiondata
    price_sort = temp_price_sort
    end_sort = temp_end_sort

    # save the data to a txt file
    with open('backend/save/auctionssave.txt', 'w') as f:
        f.write(json.dumps(auctions))
    with open('backend/save/pricesortsave.txt', 'w') as f:
        f.write(json.dumps(price_sort))
    with open('backend/save/endsortsave.txt', 'w') as f:
        f.write(json.dumps(end_sort))

def loadsave():
    with open("backend/save/auctionssave.txt", "r") as f:
        auctions = json.loads(f.read())
    with open("backend/save/pricesortsave.txt", "r") as f:
        price_sort = json.loads(f.read())
    with open("backend/save/endsortsave.txt", "r") as f:
        end_sort = json.loads(f.read())




# todo : check for valid inputs
# filter the auctions for a request
def filterauctions(amount, sort, category, search, rarity, binfilter):
    print('filterauctions function called')
    # filter the auctions with the inputted properties
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
        item = auctiondata[i]
        if category != "any" :
            if category != item[category] :
                continue
        if search != "" :
            if search in item[name] :
                continue
        if rarity != "any"
            if rarity != item[tier] :
                continue
        if binfilter == "bin" and item[bin] == "false" :
            continue
        if binfilter == "auctions" and item[bin] == "true" :
            continue
        
        founditems.append(item)
        founditemcount += 1
        if founditemcount == amount :
            break
    return(founditems)







reloadauctions()

print('done')


