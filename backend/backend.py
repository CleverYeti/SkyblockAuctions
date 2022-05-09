
import requests
import json

# amount of auction per page
page_length = 36

# if the api keys is invalid just put a new one
# each api key has a max of 65 requests per minute
# the api keys need to be made by 2 different minecraft accounts
main_api_key = ''
second_api_key = ''

#api address
hypixel_api = "https://api.hypixel.net/skyblock/auctions"

auctions = []
price_sort = []
end_sort = []

# function that reloads the entire data
def reloadauctions():
    print('reloadauctions function called')
    fetchauctions()
    sortauctions()
    copyprocesseddata()

# fetch auction pages from the hypixel api
def fetchauctions():
    print('fetchauctions function called')
    # init variables
    global auctiondata
    auctiondata = {}
    current_key = main_api_key

    # fetch the first page
    jsonresponse = fetchpage(0)

    # todo: add better error handling
    if jsonresponse["success"] = false :
        print("fetching error on page " + 0)
        return()

    auctiondata.update(jsonresponse["auctions"])
    totalpages = jsonresponse["auctions"]

    #fetch all the other pages
    for current_page in range(totalpages - 1):
        jsonresponse = fetchpage(current_page + 1)
        if jsonresponse["success"] = false :
            print("fetching error on page " + 0)
            return()
        auctiondata.update(jsonresponse["auctions"])
        # switch api key for cooldown
        if current_page = 59 :
            current_key = second_api_key



# todo: move this before fetchauctions
def fetchpage(page):
    headers = {"api": currentkey, "page": page}
    response = requests.get(hypixel_api, headers=headers)
    return json.loads(response.txt)

# sort algorithm
def binary_search(arr, val, start, end):
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start+1
  
    if start > end:
        return start
  
    mid = (start+end)/2
    if arr[mid] < val:
        return binary_search(arr, val, mid+1, end)
    elif arr[mid] > val:
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
    
    # sort by end
    tempsort = []
    tempsorteditems = []
    for i in auctiondata:
        if auctiondata[i][highest_bid_amount]:
            sortpos = binary_search(tempsort, auctiondata[i][highest_bid_amount], 0, len(tempsort) - 1)
            tempsort.insert(sortpos, auctiondata[i][highest_bid_amount])
        else:
            sortpos = binary_search(tempsort, auctiondata[i][starting_bid], 0, len(tempsort) - 1)
            tempsort.insert(sortpos, auctiondata[i][highest_bid_amount])
        tempsorteditems.insert(sortpos)
 



# copy the processed data into the active lists
def copyprocesseddata():
    print('copyprocesseddata function called')
    # copy the newly processed data into the active lists


# filter the auctions for a request
def filterauctions(amount, sort, category, search, rarity, binfilter):
    print('filterauctions function called')
    # filter the auctions with the inputted properties


reloadauctions()

print('done')


