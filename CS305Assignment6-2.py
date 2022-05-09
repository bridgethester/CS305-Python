# Bridget Hester
# April 14 2022
# CS305 Assignment 6 #2

# This program will display an open seating chart, then ask the user the location of their
# seats. Then it will ultimately display the seats that are no longer avaiable. 

arrangement = [['*']*8 for i in range(10)]

print('========================')
print('Initial Seating Chart')
print('========================')
for row in range(10):
    for seat in range(8):
        print(arrangement[row][seat],end= " ")
    print()

tickets = int(input("Enter number of tickets: "))

for i in range(tickets):
    row_inp = int(input("Which Row: "))
    seat_inp = int(input("What Seat: "))
    arrangement[row_inp-1][seat_inp-1] = "#"

    for row in range(10):
        for seat in range(8):
            try:
                if arrangement[row][seat] == "#":
                    if arrangement[row+1][seat] == '*':
                        arrangement[row+1][seat] = 'X'
                        if row-1 != -1:
                            if arrangement[row-1][seat] == '*':
                                arrangement[row-1][seat] = 'X'
            except IndexError:
                if row-1 != -1:
                    if arrangement[row-1][seat] == '*':
                        arrangement[row-1][seat] = 'X'

    for row in range(10):
        for seat in range(8):
            try:
                if arrangement[row][seat] == "#":
                    if arrangement[row][seat-1] == '*':
                        if seat-1 != -1:
                            arrangement[row][seat-1] = 'X'
                    if arrangement[row][seat+1] == '*':
                            arrangement[row][seat+1] = 'X'
            except IndexError:
                pass

print('========================')
print('New Seating Chart')
print('========================')
for row in range(10):
    for seat in range(8):
        print(arrangement[row][seat],end= " ")
    print()
print("enjoy the movie! :)")

    
