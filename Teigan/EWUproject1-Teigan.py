#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      adsmith
#
# Created:     20/09/2024
# Copyright:   (c) adsmith 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random

def menu():
    user = 0
    while user != 8:
        printMenu()
        user = int(input("type in the number of your choice"))
        if user == 1:
            printRectangle(3.55, 2.54)
        if user == 2:
            uiRectangle()
        if user == 3:
            golfSlang()
        if user == 4:
            totalNumber(int(input("Give me a starting number")),int(input("Give me a end number")))
        if user == 5:
            diceRoll(int(input("How many dice do you want to roll?")))
        if user == 6:
            menuItemSix()
        if user == 7:
            menuItemSeven()
        if user == 8:
            print("thank you for using the menu")


def printMenu():
    print("1. Item one")
    print("2. Item two")
    print("3. Item three")
    print("4. Item four")
    print("5. Item five")
    print("6. Item six")
    print("7. Item seven")
    print("8. exit")

def printRectangle(x,y):
    print("A rectangle with the height of:",x," and a width of:",y," has an area of:",x*y, "and a perimeter of:",2*x+2*y)
def uiRectangle():
    height = float(input("Give me a height"))
    width = float(input("Give me a width"))
    printRectangle(height,width)
def golfSlang():
    slang = ""
    slang2 = ""
    slang3 = ""
    holeNum = int(input("What was the hole number?"))
    par = int(input("What was the par for the hole?"))
    numOfStrokes = int(input("How many strokes did you take?"))
    numOff = numOfStrokes-par
    if numOff == -5:
        slang = "Ostrich"
    elif numOff == -4:
        slang = "Condor"
    elif numOff == -3:
        slang = "Albatross"
    elif numOff == -2:
        slang = "Eagle"
    elif numOff == -1:
        slang = "Birdie"
    elif numOff == 0:
        slang = "On par"
    elif numOff == 1:
        slang = "Bogey"
    elif numOff == 2:
        slang = "Double Bogey"
    elif numOff == 3:
        slang = "Triple Bogey"
    elif numOff == 4:
        slang = "4 over par"
    elif numOff == 5:
        slang = "5 over par"

    if numOfStrokes == 1:
        slang += "with a HOLE IN 1!"
    elif numOfStrokes == 4:
        slang += "with a Sailboat"
    elif numOfStrokes == 8:
        slang += "with a frosty"
    elif numOfStrokes == 10:
        slang += "with a BO DEREK"

    if numOfStrokes == par*2:
        slang += ", a Beagle!"

    print("On hole #",holeNum,"a par",par,"you shot a",slang)

def totalNumber(x,y):
    total = 0
    for eachNum in range(x,y+1):
        if eachNum % 3 != 0 and eachNum % 4 != 0 and eachNum % 5 != 0:
            total = total + eachNum
    print("Your starting number was:",x)
    print("Your ending number was:",y)
    print("Total:",total)
def diceRoll(numOfRolls):
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    sixes = 0
    sevens = 0
    eights = 0
    nines = 0
    tens = 0
    elevens = 0
    twelves = 0
    doubles = 0
    for x in range(0,numOfRolls):
        d1 = random.randint(1,6)
        d2 =random.randint(1,6)
        added = d1 + d2
        if added == 2:
            twos += 1
        elif added == 3:
            threes += 1
        elif added == 4:
            fours += 1
        elif added == 5:
            fives += 1
        elif added == 6:
            sixes += 1
        elif added == 7:
            sevens += 1
        elif added == 8:
            eights += 1
        elif added == 9:
            nines += 1
        elif added == 10:
            tens += 1
        elif added == 11:
            elevens += 1
        elif added == 12:
            twelves += 1
        if d1 == d2:
            doubles += 1
    print("2 -",twos, twos/numOfRolls*100,"%")
    print("3 -",threes, threes/numOfRolls*100,"%")
    print("4 -",fours, fours/numOfRolls*100,"%")
    print("5 -",fives, fives/numOfRolls*100,"%")
    print("6 -",sixes, sixes/numOfRolls*100,"%")
    print("7 -",sevens, sevens/numOfRolls*100,"%")
    print("8 -",eights, eights/numOfRolls*100,"%")
    print("9 -",nines, nines/numOfRolls*100,"%")
    print("10 -",tens, tens/numOfRolls*100,"%")
    print("11 -",elevens, elevens/numOfRolls*100,"%")
    print("12 -",twelves, twelves/numOfRolls*100,"%")
    print("Doubles -",doubles, doubles/numOfRolls*100,"%")

#def reverseString(x):
    #for eachNum in range(1,x):


def menuItemSeven():
    print("This is Menu Item 7")

def main():
    menu()

if __name__ == '__main__':
    main()
