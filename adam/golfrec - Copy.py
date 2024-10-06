
import random
import math
def menu():
    user = 0
    while user != 8:
        printMenu()
        user = int(input("type in the number of your choice "))
        if user == 1:
            printRectangle(3.55,2.54)
        if user == 2:
            uiRectangle()
        if user == 3:
            golf()
        if user == 4:
            loops()
        if user == 5:
            rollingDice()
        if user == 6:
            palindromicNumbers()
        if user == 8:
            print("thank you for using the menu")


def printMenu():
    print("1. Item Rectangle")
    print("2. Item uiRectangle")
    print("3. Item golf")
    print("4. Item loops")
    print("5. Item rolling dice")
    print("6. Item palindromic numbers")
    print("8. exit")

def printRectangle(height, width):
    area = height * width
    per = height * 2 + width * 2
    print("A rectangle with the height of ", height, "and width of:", width, "has an area of: ",area, "and a perimeter of:", per)
def uiRectangle():
    height = float(input("type in the height "))
    width = float(input("type in the width "))
    printRectangle(height,width)
def golf():
    hole = float(input("what hole are you on "))
    par = float(input("what is the par for the hole "))
    stroke = float(input("what is the nimbeer of strokes "))
    points = ""
    if par + 5 == stroke:
        points = "Over par"
    elif par + 4 == stroke:
        points = "Over par"
    elif par + 3 == stroke:
        points = "Triple bogey"
    elif par + 2 == stroke:
        points = "Double bogey"
    elif par + 1 == stroke:
        points = "Bogey"
    elif stroke == par:
        points = "Even par"
    elif par - 1 == stroke:
        points = "Birdie"
    elif par - 2 == stroke:
        points = "Egale"
    elif par - 3 == stroke:
        points = "Albatross"
    elif par - 4 == stroke:
        points = "Condor"
    elif par - 5 == stroke:
        points = "Ostrich"
    elif par * 2 == stroke:
        points = "Beagle"
    print("on hole", hole, "a par", par, "how many time you missed the hole",stroke,points)

def loops():
    start = int(input("what is your starting number "))
    end = int(input("what is your ending number "))
    total = 0
    for x in range (start, end + 1):
        if x % 3 != 0 and x % 4 != 0 and x % 5 != 0:

            total += x
        print (total)

def DiceRolled ():

    return random.randint(1,6)

def rollingDice():
    timesrolled = int(input("how many times do you want to roll "))

    Doubles = 0
    total2 = 0
    total3 = 0
    total4 = 0
    total5 = 0
    total6 = 0
    total7 = 0
    total8 = 0
    total9 = 0
    total10 = 0
    total11 = 0
    total12 = 0
    for dice in range (timesrolled):
        Dice1 = DiceRolled()
        print(Dice1)
        Dice2 = DiceRolled()
        print(Dice2)
        total = Dice1 + Dice2
        if Dice1 == Dice2:
            print("Doubles")
            Doubles += 1
        if total == 2:
            total2 += 1
        if total == 3:
            total3 += 1
        if total == 4:
            total4 += 1
        if total == 5:
            total5 += 1
        if total == 6:
            total6 += 1
        if total == 7:
            total7 += 1
        if total == 8:
            total8 += 1
        if total == 9:
            total9 += 1
        if total == 10:
            total10 += 1
        if total == 11:
            total11 += 1
        if total == 12:
            total12 += 1
    print("how many times you got 2 on the dice",total2,"how many times you got 3 on the dice",total3,"how many times you got 4 on the dice",total4,"how many times you got 5 on the dice",total5,"how many times you got 6 on the dice",total6,"how many times you got 7 on the dice",total7,"how many times you got 8 on the dice",total8,"how many times you got 9 on the dice",total9,"how many times you got 10 on the dice",total10,"how many times you got 11 on the dice",total11,"how many times you got 12 on the dice",total12,"your Doubles",Doubles)
    percent2 = total2 / timesrolled
    percent3 = total3 / timesrolled
    percent4 = total4 / timesrolled
    percent5 = total5 / timesrolled
    percent6 = total6 / timesrolled
    percent7 = total7 / timesrolled
    percent8 = total8 / timesrolled
    percent9 = total9 / timesrolled
    percent10 = total10 / timesrolled
    percent11 = total11 / timesrolled
    percent12 = total12 / timesrolled
    percentDoubles = Doubles / timesrolled
    print(percent2,percent3,percent4,percent5,percent6,percent7,percent8,percent9,percent10,percent11,percent12,percentDoubles)

def palindromicNumbers():
    start = int(input("what is your starting number "))
    end = int(input("what is your ending number "))

def main():
    menu()

if __name__ == '__main__':
    main()