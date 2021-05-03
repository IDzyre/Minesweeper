from random import shuffle
import os
import getpass
import sys
masterlist = []
list1 = [0,0,0,0,0,0,9,0,0]
go = False
Coord1 = int
Coord2 = int
save = False
play = True
name = getpass.getuser()
print("Welcome," , name)
restart = False
try:
    f = open("savegame.txt", "r")
    list1.clear
    for j in range(9):
        list1 = (f.readline().split())
        list1 = list(map(int, list1))
        masterlist.append(list1)
    f.close()
    save = True
except:
    print("No Saved Game, Creating New Game")


try:
    masterlist[5][5]
except:
    save = False
if save != True:
    masterlist.clear()
    for i in range (9):
        
        list1 = [0,0,0,0,0,0,9,0,0]
        shuffle(list1)
        masterlist.append(list1[:])
    for i in range(9):
        for j in range(9):
            if masterlist[i][j] == 9:
                if i !=0 and j != 0 and masterlist[i-1][j-1] != 9:
                    masterlist[i-1][j-1] = masterlist[i-1][j-1]+1
                if  j != 0 and masterlist[i][j-1] != 9:
                    masterlist[i][j-1] = masterlist[i][j-1]+1
                if i != 0 and masterlist[i-1][j] != 9:
                    masterlist[i-1][j] = masterlist[i-1][j]+1
                if i != 0 and j != 8 and masterlist[i-1][j+1] != 9:
                    masterlist[i-1][j+1] = masterlist[i-1][j+1]+1
                if j != 8 and masterlist[i][j+1] != 9:
                    masterlist[i][j+1] = masterlist[i][j+1]+1
                if i == 8:
                     break
                if masterlist[i+1][j] != 9:
                   masterlist[i+1][j] = masterlist[i+1][j]+1
                if j != 0 and masterlist[i+1][j-1] != 9:
                    masterlist[i+1][j-1] = masterlist[i+1][j-1]+1
                if j == 8:
                    break
                if i !=8 and j != 8 and masterlist[i+1][j+1] != 9:
                    masterlist[i+1][j+1] = masterlist[i+1][j+1]+1


while play == True:
    if restart == True:
        masterlist.clear()
        for i in range (9):
            list1 = [0,0,0,0,0,0,9,0,0]
            shuffle(list1)
            masterlist.append(list1[:])
        for i in range(9):
            for j in range(9):
                if masterlist[i][j] == 9:
                    if i !=0 and j != 0 and masterlist[i-1][j-1] != 9:
                        masterlist[i-1][j-1] = masterlist[i-1][j-1]+1
                    if  j != 0 and masterlist[i][j-1] != 9:
                        masterlist[i][j-1] = masterlist[i][j-1]+1
                    if i != 0 and masterlist[i-1][j] != 9:
                        masterlist[i-1][j] = masterlist[i-1][j]+1
                    if i != 0 and j != 8 and masterlist[i-1][j+1] != 9:
                        masterlist[i-1][j+1] = masterlist[i-1][j+1]+1
                    if j != 8 and masterlist[i][j+1] != 9:
                        masterlist[i][j+1] = masterlist[i][j+1]+1
                    if i == 8:
                        break
                    if masterlist[i+1][j] != 9:
                        masterlist[i+1][j] = masterlist[i+1][j]+1
                    if j != 0 and masterlist[i+1][j-1] != 9:
                        masterlist[i+1][j-1] = masterlist[i+1][j-1]+1
                    if j == 8:
                        break
                    if i !=8 and j != 8 and masterlist[i+1][j+1] != 9:
                        masterlist[i+1][j+1] = masterlist[i+1][j+1]+1
                   
        restart = False
    elif restart == False:
        print ("    ", end = "")
    for i in range (9):
        print (i +1, end = "   ")
    print ()
    for i in range (9):
        print (i + 1, end = " | ")
        for j in range (9):
            if masterlist[i][j] <= 9:
                print("*", end = " | ")
            if masterlist[i][j] == 10:
                print (" ", end = " | ")
            if masterlist[i][j] == 11:
                print ("1", end = " | ")
            if masterlist[i][j] == 12:
                print ("2", end = " | ")
            if masterlist[i][j] == 13:
                print ("3", end = " | ")
            if masterlist[i][j] == 14:
                print ("4", end = " | ")
        print()
    go = False
    while go != True:
        PSQ = input("Do you wish to \'C\'ontinue playing, \'S\'ave and quit, or \'Q\'uit without saving: ")
        if PSQ == "c" or PSQ == "C":
            go = True
        elif PSQ == "q" or PSQ == "Q":
            f = open("savegame.txt", "w")
            f.close()
            exit()
        elif PSQ == "S" or PSQ == "s":
            f = open("savegame.txt", "w")
            f.close()
            for i in range (9):
                for j in range(9):
                    f = open("savegame.txt", "a")
                    f.write(str(masterlist[i][j]))
                    f.write(" ")
                if i == 8 and j == 8:
                    f = open("savegame.txt", "a")
                    f.write(str(masterlist[8][8]))
                f.write("\n")
           

            exit()
        elif PSQ != "S" or "s" or "c" or "C" or "q" or "Q":
            print("Please type C, S, or Q")
    go = False
    while go != True:
        number1 = input("Enter Coordinate 1: ")
        try:
            int(number1)
        except:
            print("Please enter a number")
            go = False
            continue
        Coord1 = int(number1)
        if Coord1 > 9:
            print ("Please enter a value less than nine")
            go = False
            continue
        if Coord1 < 1:
            print ("Please enter a number greater than 0")
            go = False
            continue
        go = True
    go = False
    while go != True:
        number2 = input("Enter Coordinate 2: ")
        try:
            int(number2)
        except:
            print("Please enter a number")
            go = False
            continue
        Coord2 = int(number2)
        if Coord2 > 9:
            print ("Please enter a value less than nine")
            go = False
            continue
        if Coord2 < 1:
            print ("Please enter a number greater than 0")
            go = False
            continue
        go = True

    if masterlist[Coord1-1][Coord2-1] == 9:
        print ("YOU LOSE!")
        f = open("savegame.txt", "w")
        f.write("")
        f.close()
        go = False
        while go != True:
            playagain = input("Play Again? Y/N: ")
            go = False
            go = True
            if playagain == "y" or playagain =="Y":
                f = open("savegame.txt", "w")
                f.close()
                restart = True
                play = True
            elif playagain == "n" or playagain == "N":
                play = False
                exit
            elif playagain != "y" or "n" or "Y" or "N":
                print("Please enter y or n")
                go = False
    if masterlist[Coord1-1][Coord2-1] == 0:
        masterlist[Coord1-1][Coord2-1] = 10
        for i in range (Coord1-1, 9, 1):
            j = Coord2-1
            if j == 8:
                pass
            elif masterlist[i][j] == 0 and masterlist[i][j+1] == 10:
                masterlist[i][j] = 10
            if j == 0:
                pass
            elif masterlist[i][j] == 0 and masterlist[i][j-1] == 10:
                masterlist[i][j] = 10
            if i == 0:
                pass
            elif masterlist[i][j] == 0 and masterlist[i-1][j] == 10:
                masterlist[i][j] = 10

        for i in range (Coord1-1, -1, -1):
            for j in range (Coord2-1,9,1):
                if j == 8:
                    pass
                elif masterlist[i][j] == 0 and masterlist[i][j-1] == 10:
                    masterlist[i][j] = 10
                if i == 0:
                    pass
                elif masterlist[i][j] == 0 and masterlist[i-1][j] == 10:
                    masterlist[i][j] = 10

        for i in range (Coord1-1, 9, 1):
            for j in range (Coord2-1,9,1):
                if masterlist[i][j] == 0 and masterlist[i][j-1] == 10:
                    masterlist[i][j] = 10
                elif masterlist[i][j] == 0 and masterlist[i-1][j] == 10:
                    masterlist[i][j] = 10  

        for i in range (Coord1-1, -1, -1):
            for j in range (Coord2-1,-1,-1):
                if j == 8:
                    pass
                elif masterlist[i][j] == 0 and masterlist[i][j+1] == 10:
                    masterlist[i][j] = 10
                if i == 8:
                    pass
                elif masterlist[i][j] == 0 and masterlist[i+1][j] == 10:
                    masterlist[i][j] = 10

        for i in range (Coord1-1, -1, -1):
            j = Coord2-1
            if masterlist[i][j] == 0 and masterlist[i][j+1] == 10:
                masterlist[i][j] = 10
            if masterlist[i][j] == 0 and masterlist[i][j-1] == 10:
                masterlist[i][j] = 10
            if masterlist[i][j] == 0 and masterlist[i-1][j] == 10:
                masterlist[i][j] = 10 
       
    found = True
    while found == True:
        found = False
        for i in range(9):
            for j in range(9):
                if j == 0:
                    pass
                elif masterlist[i][j] == 0 and masterlist[i][j-1] == 10:
                    masterlist[i][j] = 10
                    found = True
                if j == 8:
                    pass
                elif masterlist[i][j] == 0 and masterlist[i][j+1] == 10:
                    masterlist[i][j] = 10
                    found = True
                if i == 0:
                    pass
                elif masterlist[i][j] == 0 and masterlist[i-1][j] == 10:
                    masterlist[i][j] = 10
                    found = True
                if i == 8:
                    pass
                elif masterlist[i][j] == 0 and masterlist[i+1][j] == 10:
                    masterlist[i][j] = 10

        continue
    if masterlist[Coord1-1][Coord2-1] != 0 and masterlist[Coord1-1][Coord2-1] != 9 and masterlist[Coord1-1][Coord2-1] < 9:
        masterlist[Coord1-1][Coord2-1] = masterlist[Coord1-1][Coord2-1] + 10
                    




