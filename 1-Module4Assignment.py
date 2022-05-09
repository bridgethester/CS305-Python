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
    lowNum = inputNum[0]
    #inputNum = [0]
    highNum = inputNum[0]
    totalNum = 0
    averageNum = 0
    
    #function call for getLow
    lowNum = getLow(inputNum,lowNum) 
    #function call for getHigh
    highNum = getHigh(inputNum,highNum)
    #function call for getTotal
    totalNum = getTotal(inputNum,totalNum)
    #function call for getAverage
    averageNum = getAverage(inputNum,totalNum) 
    #call for displayInfo
    displayInfo(averageNum, lowNum, highNum, totalNum)
    
def getLow(inputNum,lowNum):
        counter = 1
        lowNum = inputNum[counter] 
        while counter < len(inputNum) :
            if inputNum[counter] < lowNum:
                lowNum = inputNum[counter]
            counter = counter + 1
        return lowNum
    
def getHigh(inputNum, highNum):
        counter = 1
        while counter < len(inputNum) :
            if inputNum[counter] > highNum:
                highNum = inputNum[counter]
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
            
def displayInfo(averageNum, lowNum, highNum, totalNum):
        print(" ")
        print("The average number is ", averageNum)
        print('The total is ' ,totalNum)
        print("The highest number is ",highNum)
        print("The lowest number is ", lowNum)
    
main()

