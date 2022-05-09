# Bridget Hester
# CS 305 Module 3 Assignment#2

# This program, when given 𝑎, 𝑏, and 𝑐 as inputs, will give you the roots
# of the quadratic equation.
import math

def main():
    a = float(input("Enter value for a: "))
    b = float(input("Enter value for b: "))
    c = float(input("Enter value for c: "))
    
    while not ((b*b)-4*a*c)>0:
        print ("Make sure equation can't go negative.")    
        a = float(input("Enter value for a: "))
        b = float(input("Enter value for b: "))
        c = float(input("Enter value for c: "))
    quadratic(a,b,c)

  
def quadratic(a,b,c):
    root1=(-b+math.sqrt((b*b)-4*a*c))/(2*a)
    root2=(-b-math.sqrt((b*b)-4*a*c))/(2*a)
    print("The roots are:",root1,root2)
    

main()
