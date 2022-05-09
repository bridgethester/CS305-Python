#Bridget Hester 
# Lab 8-4 (updated)
# Lab 6-4 Test Score Averages

# the main function
def main():
    endProgram = 'no'
    while not (endProgram == 'yes' or endProgram == 'no'):
        print ('Please enter a yes or no')
        endProgram = input('Do you want to end program? (Enter no or yes): ')

    while endProgram == 'no':
        totalScores = 0
        averageScores = 0
        number = 0
        number = getNumber(number)
        totalScores = getScores(totalScores, number)
        averageScores = getAverage(totalScores, averageScores, number)
        printAverage(averageScores)
        endProgram = input('Do you want to end program? (yes/no): ')
        while not (endProgram == 'yes' or endProgram == 'no'):
            print ('Please enter a yes or no')
            endProgram = input('Do you want to end program? (Enter no or yes): ')

                
# this function will determine how many students took the test
def getNumber(number):
    number = int(input('How many students took the test: '))
    while not (number >=2 and  number <=30):      
        print ('Please enter a number between 2 and 30')
        number = int(input('How many students took the test: '))


    return number

# this function will get the total scores
def getScores(totalScores, number):
    for counter in range(0, number):
        score = int(input('Enter their score: '))
        while not (score >=0 and  score <=100):      
            print ('Please enter a number between 0 and 100')
            score = int(input('Enter their score: '))
        totalScores = totalScores + score
    return totalScores

# this function will calculate the average
def getAverage(totalScores, averageScores, number):
    averageScores = totalScores / number
    return averageScores

# this function will display the average
def printAverage(averageScores):
    print('The average test score is', averageScores)
    
# calls main
main()
