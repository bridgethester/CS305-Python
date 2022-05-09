# Bridget Hester
# CS 305 Module 3 Assignment#1

# This program will take the radius of a circle and return the area of the circle.

def main():
    radius = float(input("Enter radius of circle: "))
    while not radius >0:
        print ("Enter a radius greater than 0.")    
        radius = float(input("Enter radius of circle: "))       
    print ("The area is", area(radius))
    
  
def area(radius):
    area = 3.14*radius*radius
    return area

    
    
main()
