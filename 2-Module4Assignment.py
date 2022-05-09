# Bridget Hester
# March 12 2022
# This program will take in a series of numbers and display data.

def main():
    inputNum = []
    totalNum = 0
    newNum = input("Enter one number at a time or exit:")
    while newNum != "exit":
        inputNum.append(float(newNum))
        if float(newNum) > 0:    
            totalNum += float(newNum) 
        else:
            totalNum += abs(float(newNum))
        newNum = input("Enter one number at a time or exit:")
        
    #variables
    mode = inputNum[0]
    #inputNum = [0]
    totalNum = 0
    averageNum = 0
    unsortedInputNum = inputNum
    specNum = float(input("Enter a specific number: "))
    #function call for getSpec
    specNumIndex = getSpec(unsortedInputNum,specNum)
    inputNum = sortNums(inputNum)
    
    #function call for getMode
    mode = getMode(inputNum,mode) 
    
    #function call for getTotal
    totalNum = getTotal(inputNum,totalNum)
    #function call for getAverage
    averageNum = getAverage(inputNum,totalNum) 
    #call for displayInfo
    displayInfo(averageNum, mode,  specNumIndex, inputNum)
    
def sortNums(inputNum):
        inputNum.sort(reverse=True)
        return inputNum
    
def getSpec(inputNum, specNum):
        counter = 0
        while counter < len(inputNum) :
            if inputNum[counter] == specNum:
                return counter
            counter = counter + 1
        return 0
    
def getMode(inputNum, mode):
        highNum = inputNum[0]
        highCount = 1
        currentNum = inputNum[0]
        currRun = 1
        counter = 1
        while counter < len(inputNum):
            if inputNum[counter] == currentNum:
                currRun = currRun + 1
                if currRun > highCount:
                    highNum = currentNum
                    highCount = currRun
            else:
                currentNum = inputNum[counter]
                currRun = 1
                
            counter = counter + 1
        return highNum
       
def getTotal(inputNum, totalNum):
        counter = 0 
        while counter < len(inputNum):
            totalNum= totalNum + inputNum[counter]
            counter = counter + 1
        return totalNum

def getAverage(inputNum,totalNum):
        averageNum = totalNum/len(inputNum)
        return averageNum
            
def displayInfo(averageNum, mode,  specNumIndex, inputNum):
        print(" ")
        
        print("The average number is ", averageNum)
        print("The sorted array is ", inputNum)
        print("The mode is ", mode)
        print("The specific Number Index is ", specNumIndex)
    
main()

