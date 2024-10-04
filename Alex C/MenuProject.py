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

hieght = float
width = float


def menu():
    user = 0
    while user != 8:
        printMenu()
        user = int(input("type in the number of your choice"))
        if user == 1:
            printRectangle()
        if user == 2:
            uiRectangle()
        if user == 3:
            golf()
        if user == 4:
            totalLoop()
        if user == 5:
            diceRolls()
        if user == 6:
            menuItemSix()
        if user == 7:
            menuItemSeven()
        if user == 8:
            print("thank you for using the menu")


def printMenu():
    print("1. Print Rectangle")
    print("2. UI Rectangle")
    print("3. Golf Score")
    print("4. Total Number")
    print("5. Item five")
    print("6. Item six")
    print("7. Item seven")
    print("8. exit")

def printRectangle(x,y):
    area = x * y
    perimeter = (x+y)*2
    print("A rectangle with the height of:",y,"and a width of: ",x," has an area of:",area," and a perimeter of: ",perimeter)

def uiRectangle():
    height = float(input("Height of rectangle?"))
    width = float(input("Width of rectangle"))
    printRectangle(width, height)

def golf():
    hole = float(input("what is your hole number?"))
    parValue = float(input("what is your par value?"))
    strokes = float(input("How many strokes?"))
    shot = parValue - strokes
    rating = ""
    beagle = ""
    strokeRate = ""

    if shot == -5:
        rating = "Ostrich"
    if shot == -4:
        rating = "Condor"
    if shot == -3:
        rating = "albatross"
    if shot == -2:
        rating = "Eagle"
    if shot == -1:
        rating = "Birdie"
    if shot == 0:
        rating = "Even Par"
    if shot == 1:
        rating = "Bogey"
    if shot == 2:
        rating = "Double Bogey"
    if shot == 3:
        rating = "Triple Bogey"
    if shot > 3:
        rating = (shot,"over par")

    if strokes == parValue * 2:
        beagle = ",Beagle"
    if strokes >= 1:
        strokeRate = "Hole in One of Ace"
    if strokes >= 4:
        strokeRate = "Sailboat"
    if strokes >= 8:
        strokeRate = "Snowman"
    if strokes >= 10:
        strokeRate = "Bo Derek"

    print("On hole #",hole,"a par",shot,",you shot a",rating,",with a",strokeRate,beagle,"!")




def totalLoop():
    startNum = int(input("Pick the starting mumber"))
    endNum = int(input("Pick the ending number"))
    total = 0

    for eachNum in range(startNum, endNum + 1):

        if eachNum%3 != 0 and eachNum%4 != 0 and eachNum%5 != 0:
            total = total + eachNum
    print(total)

def diceRolls():
    userRolls = int(input("How many dice rolls?"))
    results = [0,0,0,0,0,0,0,0,0,0,0,0,0]

    rolls = 0
    dice1 = 0
    dice2 = 0
    doubles = 0
    diceTotal = 0

    for x in range (0, userRolls):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        diceTotal = dice1 + dice2
        results[diceTotal] += 1

        if dice1 == dice2:
            doubles += 1

    print(doubles/userRolls)
    print(results)




def menuItemSix():
    print("This is Menu Item 6")
def menuItemSeven():
    print("This is Menu Item 7")

def main():
    menu()

if __name__ == '__main__':
    main()
