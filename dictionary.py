allGuests = {'Alice':{'apples': 5,'pretzels': 12},'Bob':{'sandwiches': 3,'apples': 2},'Carol':{'cups': 3 ,'apple pie': 2}}
def totalBrought(guests,item):
    numBrought = 0
    for k,v in guests.items():
        numBrought = numBrought + v.get(item,0)
    return numBrought
print('Number of Items being brought')
print( ' 1.Apples      ' + str(totalBrought(allGuests,'apples')))
print( '2.Cup          ' + str(totalBrought(allGuests,'cups')))

