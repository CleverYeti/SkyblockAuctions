
# amount of auction per page
page_length = 36

# if the api keys is invalid just put a new one
# each api key has a max of 65 requests per minute
# the api keys need to be made by 2 different minecraft accounts
main_api_key = ''
second_api_key = ''

# function that reloads the entire data
def reloadauctions():
    print('reloadauctions function called')
    fetchauctions()
    sortauctions()
    copyprocesseddata()

# fetch auction pages from the hypixel api
def fetchauctions():
    print('fetchauctions function called')
    # fetch all auction pages from the hypixel api

# sort the auctions by price and end time
def sortauctions():
    print('sortauctions function called')
    # sort the data into two lists, sorted by price and end time

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


