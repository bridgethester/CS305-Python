# Bridget Hester
# April 14 2022
# CS305 Assignment 6 #1

# This program will take in a particular shape and output the area and perimeter 
# of either a triangle, circle, or square. 

import math 

shape = input("Enter shape to find its area and perimeter: ")

if shape == "triangle":
    sideOne = float(input("Enter side one: "))
    sideTwo = float(input("Enter side two: "))
    sideThree = float(input("Enter side three: "))
    
    perimeter = sideOne + sideTwo + sideThree
    area = math.sqrt(perimeter/2*(perimeter/2-sideOne)*(perimeter/2-sideTwo)*(perimeter/2-sideThree))
    print("")
    print("The perimeter of the triangle is: ",perimeter) 
    print('The area of the triangle is: ',area)
        
elif shape == "circle":
    radius = float(input("Enter radius of circle: "))
    
    perimeter = 2*math.pi*radius
    area = math.pi*radius*radius
    print("")
    print("The perimeter of the circle is: ",perimeter) 
    print('The area of the circle is: ',area)

elif shape == "square":
    side = float(input("Enter side of square: "))
    
    perimeter = 4*side
    area = side * side
    print("")
    print("The perimeter of the square is: ",perimeter) 
    print('The area of the square is: ',area)
    
print("")
print ("goodbye!:)")
    



