# Bridget Hester
# April 1 2022
# This program will get the number of pints in a drive, open files,
# and display information.

#Lab 10-3 Blood Drive

#the main function
def main():
  endProgram = 'no'
  print
  while endProgram == 'no':
    option = 0
    print
    print ('Enter 1 to enter in new data and store to file')
    print ('Enter 2 to display data from the file')
    option = input('Enter now ->')
    print
    
    # declare variables
    pints = [0] * 7
    totalPints = 0
    averagePints = 0
    
    if option == 1:
      # function calls
      pints = getPints(pints)
      totalPints = getTotal(pints, totalPints)
      averagePints = getAverage(totalPints, averagePints)
      writeToFile(averagePints, pints)
      
    else:
        readFromFile(averagePints, pints)
        counter=0
        for counter in range(6):
            outFile = 0
            outFile.write(str(pints[counter]) + '\n')
            outFile.write('Average Pints')
            outFile.write(str(averagePints) + '\n\n')
            outFile.close
    raw_input = 0      
    endProgram = raw_input('Do you want to end program? (Enter no or yes): ')
    while not (endProgram == 'yes' or endProgram == 'no'):
      print ('Please enter a yes or no')
      endProgram = raw_input('Do you want to end program? (Enter no or yes): ')

#the getPints function
def getPints(pints):
  counter = 0
  while counter < 7:
      pints[counter] = input('Enter pints collected: ')
      counter = counter + 1
  return pints
  
#the getTotal function
def getTotal(pints, totalPints):
  counter = 0
  while counter < 7:
    totalPints = totalPints + pints[counter]
    counter = counter + 1
  return totalPints

#the getAverage function
def getAverage(totalPints, averagePints):
  averagePints = float(totalPints) / 7
  return averagePints

#the writeToFile function
def writeToFile(averagePints, pints):
    outFile = open('Blood.txt', 'a')
    print ('Pints Each Hour', outFile)

    for counter in range(6):
      outFile.write(str(pints[counter]) + '\n')
    outFile.write('Average Pints'+ '\n')
    outFile.write(str(averagePints) + '\n\n')
    outFile.close
    
    

#the readFromFile function
def readFromFile(averagePints, pints):
  inFile= open('Blood.txt', 'r')
  str1 = inFile.read()
  print (str1)
  for counter in range(6):
    pints[counter]= inFile.read()
  str2 = inFile.read()
  print (str2)
  averagePints = inFile.read()
  print (averagePints)
    
  
main()

