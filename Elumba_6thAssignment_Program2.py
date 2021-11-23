# Program 2: Addition Trainer
# Create a program that automatically generate two random numbers to add (0 to 99)
# Let the user answer and evaluate if the user has the correct answer
# The program will ask the user 10 addition operation
# Display the result summary of the 10 operations (ex 9/10)

import random
def firstQuestion():
    first = random.randint(0, 99)
    second = random.randint(0, 99)
    calculation = first + second
    answer = int(input("Enter your first guess: "))
    if answer == calculation:
        return 1
    else:
        return 0

def secondQuestion():
    first = random.randint(0, 99)
    second = random.randint(0, 99)
    calculation = first + second
    answer = int(input("Enter your second guess: "))
    if answer == calculation:
        return 1
    else:
        return 0

def thirdQuestion():
    first = random.randint(0, 99)
    second = random.randint(0, 99)
    calculation = first + second
    answer = int(input("Enter your third guess: "))
    if answer == calculation:
        return 1
    else:
        return 0

def fourthQuestion():
    first = random.randint(0, 99)
    second = random.randint(0, 99)
    calculation = first + second
    answer = int(input("Enter your fourth guess: "))
    if answer == calculation:
        return 1
    else:
        return 0

def fifthQuestion():
    first = random.randint(0, 99)
    second = random.randint(0, 99)
    calculation = first + second
    answer = int(input("Enter your fifth guess: "))
    if answer == calculation:
        return 1
    else:
        return 0

def sixthQuestion():
    first = random.randint(0, 99)
    second = random.randint(0, 99)
    calculation = first + second
    answer = int(input("Enter your sixth guess: "))
    if answer == calculation:
        return 1
    else:
        return 0

def seventhQuestion():
    first = random.randint(0, 99)
    second = random.randint(0, 99)
    calculation = first + second
    answer = int(input("Enter your seventh guess: "))
    if answer == calculation:
        return 1
    else:
        return 0

def eighthQuestion():
    first = random.randint(0, 99)
    second = random.randint(0, 99)
    calculation = first + second
    answer = int(input("Enter your eighth guess: "))
    if answer == calculation:
        return 1
    else:
        return 0

def ninthQuestion():
    first = random.randint(0, 99)
    second = random.randint(0, 99)
    calculation = first + second
    answer = int(input("Enter your ninth guess: "))
    if answer == calculation:
        return 1
    else:
        return 0

def tenthQuestion():
    first = random.randint(0, 99)
    second = random.randint(0, 99)
    calculation = first + second
    answer = int(input("Enter your tenth guess: "))
    if answer == calculation:
        return 1
    else:
        return 0

def displayOutput(first, second, third, fourth, fifth, sixth, seventh, eighth, ninth, tenth):
    summary = first + second + third + fourth + fifth + sixth + seventh + eighth + ninth + tenth
    print(f"Your score is {summary}/10. Thank you for participating.")

firstPoint = firstQuestion()
secondPoint = secondQuestion()
thirdPoint = thirdQuestion()
fourthPoint = fourthQuestion()
fifthPoint = fifthQuestion()
sixthPoint = sixthQuestion()
seventhPoint = seventhQuestion()
eighthPoint = eighthQuestion()
ninthPoint = ninthQuestion()
tenthPoint = tenthQuestion()

displayOutput(firstPoint, secondPoint, thirdPoint, fourthPoint, fifthPoint, sixthPoint, seventhPoint, eighthPoint, ninthPoint, tenthPoint)