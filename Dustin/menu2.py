import random

def print_rectangle(width: float, height: float) -> None:
    print(f"A rectangle with a height of: {height} and a width of: {width} has an area of: {(width*height)} and a permiter of: {(width*2)+(height*2)}")

def ui_rectangle() -> None:
    width: float = float(input("What is the width: "))
    height: float = float(input("What is the height: "))

    print_rectangle(width, height)

def golf_slang() -> None:
    hole: int = int(input("Enter the hole number: "))
    par: int = int(input("Enter the par number: "))
    strokes: int = int(input("Enter the number of strokes: "))

    actual_count: int = strokes-par
    slang_one: str = ""

    match actual_count:
        case -5:
            slang_one = "Ostrich"
        case -4:
            slang_one = "Condor"
        case -3:
            slang_one = "Albatross"
        case -2:
            slang_one = "Eagle"
        case -1:
            slang_one = "Birdie"
        case 0:
            slang_one = "Even Par"
        case 1:
            slang_one = "Bogey"
        case 2:
            slang_one = "Double Bogey"
        case 3:
            slang_one = "Triple Bogey"
        case _:
            slang_one = f"{actual_count} over par"

    slang_two: str = ""
    match strokes:
        case 1:
           slang_two = "Hole in One of Ace"
        case 4:
            slang_two = "Sailboat"
        case 8:
            slang_two = "Snowman, Frosty"
        case 10:
            slang_two = "Bo Derek"

    print(f"On hole # {hole} a par {par} you shot a {slang_one}, with a {slang_two}")

def total_numbers() -> None:
    start: int = int(input("Starting number: "))
    end: int = int(input("Ending number: "))
    total: int = 0

    for num in range(start, end+1):
        if num % 3 != 0 or num % 4 != 0 or num % 5 != 0:
            total += num

    print(f"Total: {total}")

def dice_roll() -> None:
    num_to_simulate: int = int(input("How many roles do you wanna simulate: "))
    total_count: int = 0
    double_count: int = 0

    for x in range(num_to_simulate):
        roll_one: int = random.randint(1, 6)
        roll_two: int = random.randint(1, 6)

        total_count += roll_one + roll_two
        if (roll_one == roll_two):
            double_count += 1

        print(f"{x+1} - {total_count} {total_count/num_to_simulate}") 
    print(f"Doubles - {double_count} - {double_count/num_to_simulate}")

def reverse_string(string: str) -> str:
    res: str = ""
    for i in string:
        res = i + res
    return res

def calc_divisor(num_of_digits: int) -> int:
    if num_of_digits <= 2:
        return 10

    divisor: int = 10
    for _ in range(num_of_digits-2):
        divisor *= 10
    return divisor

def is_palindrom(num: int) -> bool:
    if num < 10:
        return True

    num_of_digits: int = 0
    temp: int = num
    valid: bool = True 
    while temp:
        num_of_digits += 1
        temp = int(float(temp)/10)

    while valid and num_of_digits > 2:
        divisor: int = calc_divisor(num_of_digits)
        left_most: int = int(num/divisor)
        right_most: int = num % 10

        if (left_most != right_most):
            valid = False

        num_of_digits -= 2
        num = int((float(num-divisor))/10)

    return valid 

def sum_palindrom_num() -> None:
    start: int = int(input("What is that start value: "))
    end: int = int(input("What is the end value: "))
    total: int = 0

    for num in range(start, end+1):
        if is_palindrom(num):
            total += num

    print(f"Total of all palindrom numbers from {start} to {end}: {total}")

def menu(menuNumber: int) -> None:
    match menuNumber:
        case 1:
            print_rectangle(3.55, 2.54)
        case 2:
            ui_rectangle()
        case 3:
            golf_slang()
        case 4:
            dice_roll()
        case 5:
            sum_palindrom_num()


def main() -> None:
    max_menus: int = 5

    while True:
        print("Your menu options: ")
        for x in range(1, max_menus+1):
            match x:
                case 1:
                    print(f"Menu Item {x} - print rectangle")
                case 2:
                    print(f"Menu Item {x} - ui rectangle")
                case 3:
                    print(f"Menu Item {x} - golf slang")
                case 4:
                    print(f"Menu Item {x} - dice roller")
                case 5:
                    print(f"Menu Itme {x} - sum of palindrom number")

        print("or exit")

        user_input = input(f"Your input (exit or 1-{max_menus} for the menu item): ")
        if (user_input == "exit"):
            break

        menu(int(user_input))

if __name__ == "__main__":
    main()
