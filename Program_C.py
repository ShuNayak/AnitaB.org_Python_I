#accepst a comma separated numbers from user and putputs a list and tuple
myList =[x for x in input("Enter a comma separated sequence of numbers : ").split(",")]
myTuple = tuple(myList)
print("List: {}".format(myList))
print("Tuple: {}".format(myTuple))