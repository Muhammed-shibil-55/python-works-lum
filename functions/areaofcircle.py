rad=int(input("enter the radius of the circle : "))

def area(r):
    area=3.14*r*r
    return area  # used to return the value to main program

print("area of the circle = ",area(rad))

def areasq(n):
    area=n**2
    return area
side=int(input("enter the side of the square : "))
print("area of the square = ",areasq(side))