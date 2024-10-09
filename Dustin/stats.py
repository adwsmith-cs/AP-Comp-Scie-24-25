from typing import List
import math

values: List[int] = [ ] # An empty array (list) of integers that is our values /  data

def menu_add_value() -> None: # Will ask the user for a value, then add it to the list
    value: int = int(input("What value would you like to add: ")) # Get the user input
    values.append(value) # Add the value to the list of values

def menu_delete_value() -> None: # Will ask the user for a value in the array, then remove it
    value: int = int(input("What value would you like to remove: "))
    values.remove(value) # Remove that index from values

def menu_delete_index() -> None: # Will ask the user for an index in the values, then remove it
    index: int = int(input("What value would you like to remove (by index): "))
    values.pop(index)

def menu_display_values() -> None: # Will display all the values in the list
    print(values) # Prints all the values in the list

def menu_mean() -> None: # Will display the mean of the values
    sum: int = 0 # Starting sum value, initaliy zero
    for value in values: # Iterate over every element in the array values
        sum += value # Increment the sum value by the current element
    print(f"The mean of the values is {sum/len(values)}") # Display the mean (sum/number of elements)

def menu_median() -> None: # Will display the number that is in the middle of the array
    values.sort() # First, sort the array of values
    if len(values) % 2 != 0: # If there is an odd number of elements, return the middle most number
        print(f"The median is {values[int(len(values)/2)]}") # Print the middle number
    else: # Calculate the middle two numbers, since there is an even number of elements
        middle_left: int = values[int(len(values)/2)-1] 
        middle_right: int = values[int(len(values)/2)]
        print(f"The median is {(middle_left+middle_right)/2}") # Print the average of the two middle items

def menu_midpoint() -> None: # Will display the midpoint of the array
    start: int = values[0] # The first value in the array
    end: int = values[len(values)-1] # The last value in the array
    print(f"The midpoint is {start+(end-start)/2}") # The calculated midpoint of the two numbers

def menu_mode() -> None: # Will display the mode, the most frequent number
    number_count: dict[int, int] = { } # Create a dictionary (hashmap) to store the number, and how many times that number has occured
    for value in values: # Iterate through each value in the array
        number_count[value] += number_count.get(value, 0) + 1 # Icrement the number count for that number
    max_key: int = 0
    max_count: int = -1  # Use -1 to ensure that any count will be larger initially
    for key, count in number_count.items(): # Iterate through the elements in the dictionary (hashmap)
        if count > max_count: # If the current element is larger than the max, then update the max
            max_count = count
            max_key = key
    print(f"The mode, or most frequent number is {max_key}")

def menu_standard_devitation() -> None: # Will display the standard devitation of the array
    average: float = 0 # First find the average of all the elements
    for value in values:
        average += value
    average /= len(values)
    variance: float = 0 # Then, find the variance of the data
    for value in values:
        variance = value-average
    variance /= len(values)
    print(f"The standard devitation is {math.sqrt(variance)}") # Take the sqrt of variance, which gives you the standard deviation

# Will display menu options, then get user input, then execute the correct operation, running the menu, or exiting
def menu(menu_item: int) -> None:
    match menu_item: 
        case 0:
            menu_add_value()
        case 1:
            menu_delete_value()
        case 2:
            menu_delete_index()
        case 3:
            menu_display_values()
        case 4:
            menu_mean()
        case 5:
            menu_median()
        case 6:
            menu_midpoint()
        case 7:
            menu_mode()
        case 8:
            menu_standard_devitation()

# Main function, called in program entry point
def main() -> None:
    max_menus: int = 9 # Number of menu options available

    while True:
        print("Your menu options: ")
        for x in range(max_menus): # Go through all the available menus
            match x: # Determine the type of menu
                case 0: # Menu add value
                    print(f"Menu {x+1} - Add Value")
                case 1: # Menu delete value
                    print(f"Menu {x+1} - Delete Value")
                case 2: # Menu delete by index
                    print(f"Menu {x+1} - Delete by Index")
                case 3: # Menu display all the values in the data 
                    print(f"Menu {x+1} - Display all values")
                case 4: # Menu mean
                    print(f"Menu {x+1} - Display the mean of the values")
                case 5: # Menu median
                    print(f"Menu {x+1} - Display the median (middle number) of the array")
                case 6: # Menu midpoint
                    print(f"Menu {x+1} - Display the midpoint of the values")
                case 7: # Menu mode
                    print(f"Menu {x+1} - Display the mode, the most frequent number")
                case 8: # Menu standard devitation
                    print(f"Menu {x+1} - Display the standard devitation of the values")
        print("or exit")
        user_input = input(f"Your input (exit or 1-{max_menus} for the menu item): ")
        if user_input == "exit":
            break

        menu(int(user_input)-1)

# Entry point
if __name__ == "__main__":
    main()
