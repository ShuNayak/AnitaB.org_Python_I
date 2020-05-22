#writing python program to display current date and time
import datetime

rightNow = datetime.datetime.now()
print("the current date and time is",end=" ")
print(rightNow.strftime("%Y-%m-%d %A %I-%M-%S %p"))