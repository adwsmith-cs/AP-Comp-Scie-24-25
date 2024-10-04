import random

golfDict = {
    -5: "Ostrich",
    -4: "Condor",
    -3: "Albatross",
    -2: "Eagle",
    -1: "Birdie",
    0: "Par",
    1: "Bogey",
    2: "Double Bogey",
    3: "Triple Bogey"
}

specialDict = {
    1: "Hole in One!",
    4: "Sailboat",
    8: "Snowman",
    10: "Bo Derek"
}



def menu():
    user = 0
    while user != 7:

        user = int(input("type in the number of your choice"))
        if user == 1:
            printRectangle(3.55, 2.54)
        if user == 2:
            uiRectangle(input("Give me a height"), input("Give me a width"))
        if user == 3:
            golfTime()
        if user == 4:
            findNumbers()
        if user == 5:
            diceRolls()
        if user == 6:
            totalPalindromeFinder()
        if user == 7:
            print("thank you for using the menu")




def printMenu():
    print("1. Print Rectangle")
    print("2. Custom Rectangle")
    print("3. Golf Finder")
    print("4. Find Numbers")
    print("5. Dice Rolls")
    print("6. Total Palindrome Finder")
    print("7. exit")


def printRectangle(height, width):
    print("A rectangle with the height of: " + str(height) + " and a width of: " + str(width) + ", has an area of: " + str(height * width) + " and a perimeter of: " + str((height + width) * 2))
def uiRectangle(h, w):
    printRectangle(float(h), float(w))

def golfTime():
    holeNum = input("Give me the hole number")
    parNum = int(input("Give me par for the hole"))
    strokeNum = int(input("Give me the number of strokes"))
    special = ""
    if strokeNum - parNum in golfDict:
        birdName = golfDict.get(strokeNum - parNum)
    elif strokeNum - parNum < -5:
        birdName = str(abs(strokeNum - parNum)) + " under par"
    elif strokeNum - parNum > 3:
        birdName = str(strokeNum - parNum) + " over par"
    if strokeNum in specialDict:
        special = specialDict.get(strokeNum)

    print("On hole #" + holeNum + " there was a par of " + str(parNum) + ", and you shot a " + birdName, end="")
    if special != "":
        print(" with a " + special, end="")
    if strokeNum == parNum * 2:
        print(", a Beagle!")
    print("\n")

def findNumbers():
    start = int(input("Give me a starting number (inclusive)"))
    ending = int(input("Give me an ending number (inclusive)"))
    total = 0

    for x in range(start, ending + 1):
        if x % 3 != 0 and x % 4 != 0 and x % 5 != 0:
            total += x

    print("Total: " + str(total))


def diceRolls():
       numberRolls = int(input("Give me the number of rolls"))
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

       for x in range (0, numberRolls):
            roll1 = random.randint(1,6)
            roll2 = random.randint(1,6)
            roll = roll1 + roll2
            if roll1 == roll2:
                doubles += 1
            if roll == 2:
                twos += 1
            elif roll == 3:
                threes += 1
            elif roll == 4:
                fours += 1
            elif roll == 5:
                fives += 1
            elif roll == 6:
                sixes += 1
            elif roll == 7:
                sevens += 1
            elif roll == 8:
                eights += 1
            elif roll == 9:
                nines += 1
            elif roll == 10:
                tens += 1
            elif roll == 11:
                elevens += 1
            elif roll == 12:
                twelves += 1

       print("2  " + str(twos) + " rolls of 2, " + "{}%".format(str(round(((twos / numberRolls) * 100), 2))) + " of " + str(numberRolls))
       print("3  " + str(threes) + " rolls of 3, " + "{}%".format(str(round(((threes / numberRolls) * 100), 2))) + " of " + str(numberRolls))
       print("4  " + str(fours) + " rolls of 4, " + "{}%".format(str(round(((fours / numberRolls) * 100), 2))) + " of " + str(numberRolls))
       print("5  " + str(fives) + " rolls of 5, " + "{}%".format(str(round(((fives / numberRolls) * 100), 2))) + " of " + str(numberRolls))
       print("6  " + str(sixes) + " rolls of 6, " + "{}%".format(str(round(((sixes / numberRolls) * 100), 2))) + " of " + str(numberRolls))
       print("7  " + str(sevens) + " rolls of 7, " + "{}%".format(str(round(((sevens / numberRolls) * 100), 2))) + " of " + str(numberRolls))
       print("8  " + str(eights) + " rolls of 8, " + "{}%".format(str(round(((eights / numberRolls) * 100), 2))) + " of " + str(numberRolls))
       print("9  " + str(nines) + " rolls of 9, " + "{}%".format(str(round(((nines / numberRolls) * 100), 2))) + " of " + str(numberRolls))
       print("10  " + str(tens) + " rolls of 10, " + "{}%".format(str(round(((tens / numberRolls) * 100), 2))) + " of " + str(numberRolls))
       print("11  " + str(elevens) + " rolls of 11, " + "{}%".format(str(round(((elevens / numberRolls) * 100), 2))) + " of " + str(numberRolls))
       print("12  " + str(twelves) + " rolls of 12, " + "{}%".format(str(round(((twelves / numberRolls) * 100), 2))) + " of " + str(numberRolls))
       print("Doubles  " + str(doubles) + " rolls of doubles, " + "{}%".format(str(round(((doubles / numberRolls) * 100), 2))) + " of the time")

def reverseString(y):
    newString = ""
    for x in reversed(range(0, len(y))):
        newString = newString + y[x]
    return(newString)
def isPalindrome(givenString):
    if givenString == reverseString(givenString):
        return(True)
    else:
        return(False)
def isNumberPalindrome(num):
    if isPalindrome(str(num)):
        return(True)
    else:
        return(False)

def totalPalindromeFinder():
    starting = int(input("Give me a starting number"))
    ending = int(input("Give me an ending number"))
    total = 0
    for count in range (starting, ending + 1):
        if isNumberPalindrome(count):
            total = total + count
    print(total)


def main():
    menu()

if __name__ == '__main__':
    printMenu()
    main()
