#check if a number is within 100 of 1000 or 2000
# 100 of 1000 means between 900 to 1100 (inclusive)
#100 of 2000 means between 1900 to 2100 (inclusive)

myNum = int(input('Enter a number to check netween 100 of 1000 or 2000: '))
if (myNum>=900 and myNum<=1100) or (myNum>=1900 and myNum<=2100):
    print(True)
else:
    print(False)