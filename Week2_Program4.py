myList = [2,3,4,5,8,4,3,5,2,1,8,8,6,3,4,5,7,9]
myList = list(set(myList))
print(myList) # this is a list it is ordered.
# in a list I can update the values, for example changing the value at position 0
myList[0] = 100
print(myList)

# a tuple is immutable and ordered , so we can access the elements in a tuple but we cannot alter it
myTuple = tuple(myList)
print(myTuple)
#fetching the element at location 0
print(myTuple[0])
# but modifications in a tuple are not allowed
# so this shud raise you an error
myTuple[0] =101
