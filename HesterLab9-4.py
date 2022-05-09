# Bridget Hester
# March 12 2022
# This program will get the number of pints in a drive and display information.

# the main function
def main():
    endprogram = 'no' 
    print()
    while endprogram == 'no':
        print() 
    
        # declare variables
        pints = [0]*7
        totalPints = 0
        averagePints = 0 
        highPints = 0
        lowPints = 0
        
        # function calls
        endProgram = input("Do you want to end the program?(Enter no or yes): ")
        while not (endProgram == "yes" or endProgram == "no"):
            print("Please enter a yes or no")
            endProgram = input ("Do you want to end the program? (Enter no or yes): ")
        
    # getPints function
        pints = getPints(pints)
    # getTotal function
        totalPints = getTotal(pints,totalPints) 
    # getAverage function
        averagePints = getAverage(totalPints, averagePints)
    # getHigh function
        highPints = getHigh(pints, highPints)
    # getLow function
        lowPints = getLow(pints,lowPints)    
    # getInfo function
        displayInfo(averagePints, lowPints, highPints) 
    
    
    
    
    
def getPints(pints):
    counter = 0
    while counter < 7 :
        pints[counter] = int(input("Enter pints: "))
        counter = counter + 1
    return pints 

def getTotal(pints,totalPints):
    counter = 0 
    while counter < 7:
        totalPints= totalPints + pints[counter]
        counter = counter + 1
    return totalPints

def getAverage(totalPints,averagePints):
    averagePints = totalPints/7
    return averagePints 

def getHigh(pints, highPints):
    highPints = 0
    counter = 1
    while counter < 7 :
        if pints[counter] > highPints:
            highPints = pints[counter]
        counter = counter + 1
    return highPints

def getLow(pints,lowPints):
    counter = 1
    lowPints = pints[counter] 
    while counter < 7 :
        if pints[counter] < lowPints:
            lowPints = pints[counter]
        counter = counter + 1
    return lowPints

def displayInfo(averagePints, lowPints, highPints):
    print("The average number of pints is", averagePints)
    print("The highest number of pints donated is",highPints)
    print("The lowest number of pints donated is", lowPints)



# calls main
main()



