#accept the radius of a circle from user and return the area of a circle
radius = input("Enter the radius of the circle ")
area = 3.14 * (int(radius)**2)
print(f"area of the circle is: {area}")
# printing it using another format
print("area of the circle {}".format(area))