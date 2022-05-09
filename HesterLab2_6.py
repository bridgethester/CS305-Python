# Bridget Hester
# January 20 2022
# Write a program that will calculate a 20% tip and a 6% tax on a meal price.
# The user will enter the meal price and the program will calculate tip, tax,
# and the total. The total is the meal price plus the tip plus the tax. 

# This program uses functions and variables

# the main function
def main(): 
    print('Welcome to the meal calculator program')
    print() # prints a blank line
    
#calls functions
    mealPrice = input_meal()
    tip= calc_tip(mealPrice)
    tax = calc_tax(mealPrice)
    total = calc_total(mealPrice, tip, tax)
    print_info(mealPrice, tip, tax, total) 
    
# this function will input meal price
def input_meal():
   mealPrice = input('Enter the meal price $')
   mealPrice = float (mealPrice)
   return mealPrice

# this function will calculate tip at 20%
def calc_tip(mealPrice): 
    tip = mealPrice * .20 
    return tip
    
# this function will calculate tax at 6%
def calc_tax(mealPrice):
    tax = mealPrice * .06
    return tax
    
# this function will calculate tip, tax, and the total cost
def calc_total(mealPrice, tip, tax): 
    total = mealPrice + tip + tax
    return total
    
# this function will print tip, tax, the mealprice, and the total 
def print_info(mealPrice, tip, tax, total):
    print ('The meal price is $',mealPrice)
    print ('The tip is $', tip)
    print ('The tax is $', tax)
    print ('The total is $',total)
    
#calls main 
main()

 