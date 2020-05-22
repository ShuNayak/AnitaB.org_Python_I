#check if a particular number is within a given set of numbers
myList = [1,2,34,56,78,90,100,345,678]
myNum = int(input("enter a specific number to check: "))
if myNum in myList:
    print(True)
else:
    print(False)
