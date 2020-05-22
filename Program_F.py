#return difference between given number and 17 , if the number is greater than 17 return double the difference
myNum = int(input('enter a specific number: '))
if myNum>17:
    print("The number is greater than 17, hence: {}".format(2*(myNum-17)))
else:
    print("The number is less than 17, hence: {}".format(17-myNum))