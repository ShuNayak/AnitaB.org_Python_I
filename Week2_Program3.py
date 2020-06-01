s= "hello python three"
myList = []
for item in s.split(' '):
    if item=="three":
        myList.append(3)
    else:
        myList.append(item.upper())

print(myList)