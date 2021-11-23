# Program 1: Number Sorter
# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.

def userInput():
    number1 = int(input("Enter 1st number: "))
    number2 = int(input("Enter 2nd number: "))
    number3 = int(input("Enter 3rd number: "))
    number4 = int(input("Enter 4th number: "))
    return number1, number2, number3, number4

one, two, three, four = userInput()

if one > two and one > three and one > four:
    highest = one
elif two > one and two > three and two > four:
    highest = two
elif three > one and three > two and three > four:
    highest = three
else:
    highest = four

if highest == one:
    if two >= three and two >= four:
        third = two
    elif three >= two and three >= four:
        third = three
    else:
        third = four
elif highest == two:
        if one >= three and one >= four:
            third = one
        elif three >= two and three >= four:
            third = three
        else:
            third = four
elif highest == three:
        if one >= three and one >= four:
            third = one
        elif two >= one and three >= four:
            third = two
        else:
            third = four
else:
    if highest == four:
        if one >= three and one >= two:
            third = one
        elif three >= two and three >= one:
            third = three
        else:
            third = two

if one < two and one < three and one < four:
    lowest = one
elif two < one and two < three and two < four:
    lowest = two
elif three < one and three < two and three < four:
    lowest = three
else:
    lowest = four

if lowest == one:
    if two <= three and two <= four:
        second = two
    elif three <= two and three <= four:
        second = three
    else:
        second = four
elif lowest == two:
    if one <= three and one <= four:
        second = one
    elif three <= one and three <= four:
        second = three
    else:
        second = four
elif lowest == three:
    if one <= two and one <= four:
        second = one
    elif two <= one and two <= four:
        second = two
    else:
        second = four
else:
    if lowest == four:
        if one <= two and one <= three:
            second = one
        elif two <= one and two <= three:
            second = two
        else:
            second = three


print(f"The order from highest to lowest is: {highest}, {third}, {second}, {lowest}")