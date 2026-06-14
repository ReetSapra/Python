# File: homework10.py
# Assignment: Homework 10
# Description: This program manages people's birthdays using a dict.
# Author: Reet Sapra
# Email: reetsapr@usc.edu
# Section: Tictacs
# Instructor: Emily Millard



# Function: displayChoice
# Parameter: none
# Return: none
# This function displays the choices to the user
def displayChoice():
    print("Birthday Dictionary")
    print("\tP) Print the birthdays")
    print("\tA) Add a birthday")
    print("\tU) Update a birthday")
    print("\tQ) Quit")


# Function: loadBirthdays
# Parameter: filenameStr is a str with the name of the CSV file to read and has a
# default value of "birthdays.csv"
# Return value: a dictionary containing birthdays where the keys are names of
# people (strings) and the values are birthdays (strings)
# This function reads a CSV file, creates a dictionary, and returns the dictionary.

def loadBirthdays(filenameStr="birthdays.csv"):
    birthdayDict = {}
    file = open(filenameStr, "r")
    for line in file:
        line = line.strip()
        parts = line.split(",")
        name = parts[0]
        date = parts[1].strip()
        year = parts[2].strip()
        birthday = date + ", " + year
        birthdayDict[name] = birthday

    file.close()

    return birthdayDict

# Function: printBirthdays
# Parameter: dateDict is a dictionary containing birthdays where the keys are
# names of people (strings) and the values are birthdays (strings)
# Return value: None
# This function displays the names of people in alphabetical order with each
# birthday on its own line.

def printBirthdays(dateDict):
    names = list(dateDict.keys())
    names.sort()
    for name in names:
        birthday = dateDict[name]
        print(name + " was born on " + birthday)



# Function: addBirthday
# Parameter: dateDict is a dictionary containing birthdays where the keys are
# names of people (strings) and the values are birthdays (strings)
# Return value: None
# This function gets user input to add a person and their corresponding birthday
# to the dateDict parameter.

def addBirthday(dateDict):
    name = input("Enter a person: ")
    name = name.title()

    if name in dateDict:
        print(name + " (" + dateDict[name] + ") is already in the dictionary")
    else:
        birthday = input("Enter their birthday: ")
        birthday = birthday.title()

        dateDict[name] = birthday

        print(name + " (" + birthday + ") has been added to the dictionary")


# Function: updateBirthday
# Parameter: dateDict is a dictionary containing birthdays where the keys are
# names of people (strings) and the values are birthdays (strings)
# Return value: None
# This function gets user input to update the birthday of a person in the dateDict
# parameter.

def updateBirthday(dateDict):
    name = input ("Enter a person ")
    name = name.title()

    if name not in dateDict:
        print(name, " is not in the dictionary")
    else:
        birthday = input("Enter their birthday: ")
        birthday = birthday.title()
        dateDict[name] = birthday
        print(name + "'s birthday has been updated to " + birthday)


# Function: saveBirthdays
# Parameter: dateDict is a dictionary containing birthdays where the keys are
# names of people (strings) and the values are birthdays (strings)
# Parameter: filenameStr is a str with the name of the CSV file to write to
# Return value: None
# This function writes the dictionary to a CSV file.

def saveBirthdays(dateDict, filenameStr):
    fileOut = open(filenameStr, "w")

    for name in dateDict:
        birthday = dateDict[name]

        parts = birthday.split(",")
        date = parts[0].strip()
        year = parts[1].strip()

        print(name + "," + date + "," + year, file=fileOut)

    fileOut.close()
    print("Data was written to " + filenameStr)


def main():
    dateDict = loadBirthdays()
    displayChoice()
    choice = input("Choice: ")
    choice = choice.upper()

    while choice != "Q":

        if choice == "P":
            printBirthdays(dateDict)
        elif choice == "A":
            addBirthday(dateDict)
        elif choice == "U":
            updateBirthday(dateDict)
        else:
            print("Invalid choice")

        displayChoice()
        choice = input("Choice: ")
        choice = choice.upper()

    filename = input("Enter a filename to save to: ")
    saveBirthdays(dateDict, filename)


main()




