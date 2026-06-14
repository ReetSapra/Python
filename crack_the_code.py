

import random

# Function: isSingleDigit
# Parameter: userStr is a string that holds input from the user
# Return value: a bool (True or False) depending if the userStr is a string
# containing one single digit
# This function determines if the userStr contains a single digit (0 – 9).

def isSingleDigit(userStr):
    if userStr.isdigit() and len(userStr) == 1:
        return True
    else:
        return False

# Function: createSecretCode
# Parameter: numDigits is an integer which is the number of digits in the secret
# code list created in this function
# Return value: a list containing randomly selected integers between 0 and 9
# (inclusive) and the length of the list is the numDigits parameter
# This function creates a list of single digits where the length is numDigits.

def createSecretCode(numDigits):
    secretList = []
    for i in range(numDigits):
        num = random.randint(0, 9)
        secretList.append(num)
    return secretList



# Function: createUserGuess
# Parameter: numDigits is an integer which is the number of digits in the list
# created in this function
# Return value: a list containing integers between 0 and 9 (inclusive) that the user
# entered and the length of the list is the numDigits parameter
# This function creates a list of single digits entered by the user.
def createUserGuess(numDigits):
    print("The number of digits in the code is", numDigits)
    userList = []

    for i in range(numDigits):
        userInput = input("Enter a digit (0-9) for index " + str(i) + ": ")

        while not isSingleDigit(userInput):
            userInput = input("Enter a digit (0-9) for index " + str(i) + ": ")

        userList.append(int(userInput))

    print("Your guess is", userList)
    return userList


# Function: displayCorrectDigits
# Parameter 1: secretCode is a list containing integers with the secret code that
# the user is trying to crack
# Parameter 2: userGuess is a list containing integers with the user’s guess of the
# secret code
# Parameter 3: numDigits is an integer that is the number of digits in each list (the
# lists are the same length)
# Return value: None
# This function displays message about each digit in the userGuess list.
def displayCorrectDigits(secretCode, userGuess, numDigits):
    print("Let's see if you have any correct digits")

    for i in range(numDigits):
        guessDigit = userGuess[i]
        secretDigit = secretCode[i]
        count = secretCode.count(guessDigit)

        if guessDigit == secretDigit and count == 1:
            print(str(guessDigit) + " at index " + str(i) + " is correct")

        elif guessDigit == secretDigit and count > 1:
            print(str(guessDigit) + " at index " + str(i) + " is correct and occurs " + str(count) + " times")

        elif count == 0:
            print(str(guessDigit) + " is not in the secret code")

        elif count == 1:
            print(str(guessDigit) + " at index " + str(i) + " occurs 1 time")

        else:  # count > 1 (but not correct position)
            print(str(guessDigit) + " at index " + str(i) + " occurs " + str(count) + " times")



def main():
    numDigits = 3
    secretCode = createSecretCode(numDigits)
    userGuess = createUserGuess(numDigits)

    count = 1

    while secretCode != userGuess:
        displayCorrectDigits(secretCode, userGuess, numDigits)
        userGuess = createUserGuess(numDigits)
        count += 1

    if count == 1:
        print("You cracked the code in 1 guess!")
    else:
        print("You cracked the code in", count, "guesses!")


main()





