myList = [2,3,4,5,8,4,3,5,2,1,8,8,6,3,4,5,7,9]
myList = list(set(myList))
print([x for x in myList if x%2 != 0])