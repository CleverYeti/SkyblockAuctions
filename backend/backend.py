
# function that reloads the entire data
def reload():
    print('reload function called')
    fetchauctions()
    sortauctions()
    copyprocesseddata()

#fetch auction pages from the hypixel api
def fetchauctions():
    print('fetchauctions function called')
    #fetch all auction pages from the hypixel api

#sort the auctions by price and end time
def sortauctions():
    print('sortauctions function called')
    #sort the data into two lists, sorted by price and end time

#copy the processed data into the active lists
def copyprocesseddata():
    print('copyprocesseddata function called')
    #copy the newly processed data into the active lists


#filter the auctions for a request
def filterauctions(page, sort, category, search, rarity, binfilter):
    print('filterauctions function called')
    #filter the 


reload()

print('done')


