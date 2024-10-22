import inspect
from typing import Callable, List
import math
from random import randint

menuDict = {}
def menu(key: str, argTypes: Callable): # The function called when you do @Menu()
    def decorator(fn: Callable): # The wrapper around the fn on the line below

        def wrapper(args):
            argsLen = len(args)
            typesLen = len(argTypes)

            if argsLen > typesLen:
                print(f'\x1b[0;33mToo many arguments provided, proceeding with first {typesLen}\x1b[0m')

            if argsLen < typesLen:
                print("\x1b[0;31mToo few arguments provided\x1b[0m")
                return None

            newArgs = []
            i = 0
            while i < argsLen and i < typesLen:
                try:
                    newArgs.append(argTypes[i](args[i]))
                except:
                    print(f'\x1b[0;31mArgument {i} must be of type {argTypes[i].__name__}\x1b[0m')
                    return None
                i += 1

            return fn(*newArgs)

        # convert function __name__ to a Title Case name for display
        name = bytearray(fn.__name__, "ascii")
        i = 0
        while i < len(name):
            if name[i] >= 65 and name[i] <= 90: # [A, Z]
                name.insert(i, 32) # 32 is Space
                i += 1 # increment extra to avoid retread
            i += 1
        name[0] -= 32 # makes first letter uppercase
        
        wrapper.__name__ = name.decode("ascii")

        menuDict[key] = (wrapper, fn) # store both the wrapped and original function

        # allows fn to still be looked up by name
        return fn

    return decorator


def showMenu():
    print("[#]=====[Function Name]===[Parameters]===") # add a little flair

    # display each menu item
    for key, (fn, ogFn) in menuDict.items():
        params = inspect.signature(ogFn).parameters
        # format the parameters
        paramStrs = []
        for k, v in params.items():
            paramStrs.append(str(k))
        paramsStr = str(paramStrs).replace("'", "")

        print(f'{key}:\t{fn.__name__}{" " * (18 - len(fn.__name__))}{paramsStr}')

    # display hardcoded Exit item
    print(
        "Exit:\tQuit the program\n"
        "----\n"
        "Example input: \x1b[0;36m2 arg1 arg2\x1b[0m\n"
        "> ",
        end=""
    )

def prompt(message: str):
    print(f'{message}:\n> ', end="")

# menu items

# returns a formatted string, which is upstream printed by the menu selection
@menu("1", [float, float])
def printRectangle(width: float , height: float):
    area = width * height
    perim = width*2 + height*2
    return f'A rectangle with the height of: {height} and a width of: {width} has an area of: {area} and a perimeter of: {perim}'


@menu("2", [])
def uiRectangle():
    prompt("Width")
    width = float(input())
    prompt("Height")
    height = float(input())

    return printRectangle(width, height)


@menu("3", [])
def golfSlang():
    # Hole number
    # Par on the hole
    # Stroke number
    # Output in accordance
    # Strokes - Par: [-5, 3] + 5: [0, 8]:
    birdNames = [
        'Ostrich',
        'Condor',
        'Albatross',
        'Eagle',
        'Birdie',
        'Even Par',
        'Bogey',
        'Double Bogey',
        'Triple Bogey',
    ]
    # Strokes
    specificNames = {
        1 : "Hole in One",
        4 : "Sailboat",
        8 : "Snowman, Frosty",
        10: "Bo Derek"
    }
    prompt("Hole number")
    holeNum = int(input())
    prompt("Par for the hole")
    par = int(input())
    prompt("Stroke count")
    strokes = int(input())

    birdNameIndex = strokes - par + 5
    specificName = specificNames.get(strokes)

    specificName = f', with a {specificName}' if specificName != None else ""
    beagle = ""
    if strokes == par*2:
        beagle = ", a Beagle!"
    else:
        specificName += "!" if strokes == 1 else "."
    # (Stokes = 2Par) = Beagle
    birdName = birdNames[birdNameIndex] if birdNameIndex < len(birdNames) else f'{birdNameIndex - 5} over par'

    return f'On hole #{holeNum} a par {par} you shot a {birdName}{specificName}{beagle}'


@menu("4", [int, int])
def loop(start, end):
    total = 0
    badNums = [3, 4, 5]
    for n in range(start, end+1):
        wasDivis = False
        for bad in badNums:
            if n % bad == 0:
                wasDivis = True
                break
        if not wasDivis:
            total += n

    return total


@menu("5", [int])
def rollDice(rollCount):
    # for storing total roll values, indexes are keys adjusted down by 2
    # so 0 is for rolls value 2 and 10 is 12
    rolls = [0] * 11
    doubles = 0
    total = 0
    for _ in range(0, rollCount):
        roll1 = randint(1, 6)
        roll2 = randint(1, 6)
        both = roll1 + roll2

        total += both
        rolls[both - 2] += 1
        if roll1 == roll2:
            doubles += 1

    # color
    print("\x1b[0;32m", end="")
    # print out all the rolls with %
    for i in range(len(rolls)):
        print(f'{i+2} - {rolls[i]} {rolls[i]/rollCount * 100}%')
    # print out doubles with %
    print(f'Doubles - {doubles} {doubles/rollCount * 100}%')
    # end color
    print("\x1b[0m", end ="")


def reverseString(s: str) -> str:
    # convert the string to bytes
    byteArr = bytearray(s, 'ascii')

    newStr = bytearray()
    # backwards iterate over byteArr
    for i in range(len(byteArr)-1, -1, -1):
        newStr.append(byteArr[i])

    return newStr.decode('ascii')
    
def isPalindrome(s: str) -> bool:
    # the string being the same bith ways is by definition a palindrome
    return s == reverseString(s)

def isNumPalindrome(n: int) -> bool:
    return isPalindrome(str(n))

@menu("6", [int, int])
def palindromicNums(start, end):
    total = 0
    for n in range(start, end+1):
        if isNumPalindrome(n):
            total += n
    return total

# end setup
# start runtime

showMenu()
last = ""
while((inp := input()) != "Exit"):
    # clear leading/trailing whitespace
    inp = inp.strip() 
    # split over whitespace, creating an easy to use set of the input
    inp = inp.split()

    # the command is at index 0, popping so the rest of the set can be assumed at argument inputs
    inpItem = inp.pop(0)
    # allow up arrow to access the last command input
    if inpItem == "\x1b[A": # up arrow
        inpItem = last

    fn = menuDict.get(inpItem)

    if fn:
        # get specifically the wrapped function, [1] is the unwrapped
        fn = fn[0]

        out = fn(inp)
        # print the output with some flair
        if out != None:
            print(f'\x1b[0;32m{out}\x1b[0m')
    else:
        print(f'\x1b[0;31m{inpItem} is not on the Menu\x1b[0m')

    last = inpItem
    showMenu()
