

import random

# Function: displayRules
# Parameter: None
# Return value: None
# This function displays information about the game.

print("Start \nEnd")

def displayGameInfo():
    print("Let's play Odds and Evens")
    print("\tThe user chooses odds or evens.")
    print("\tThe user enters a number of fingers (1-5)")
    print("\tThe winner is determined based on the sum of the numbers.")
    print("\tIf the user is evens and the sum is even, then the user won.")

# Function: chooseOption
# Parameter: optionsList is a list of strings
# Return value: an int which is the index of the user’s choice in the optionsList
# This function allows the user to choose an option in the optionsList.

def chooseOption(optionsList):
    print("\nThe options are", optionsList)

    choice = input("Enter your choice: ").strip().lower()

    while choice not in optionsList:
        choice= input("Enter your choice: ").strip().lower()

    print("User entered", choice)

    index = optionsList.index(choice)

    return index


#Function: getUserNum
#Parameter: None
#Return value: an int between 1 and 5 (inclusive)
#This function gets an integer from the user and ensures it’s between 1 and 5,
#which represents the user’s number of fingers.

def getUserNum():
    fingers = int(input("Enter the number of fingers (1-5):"))
    while fingers < 1 or fingers > 5:
        fingers = int(input("Enter the number of fingers (1-5): "))

    print("User shows", fingers)

    return fingers


#Function: getComputerNum
#Parameter: None
#Return value: an int between 1 and 5 (inclusive)
#This function randomly gets an integer between 1 and 5, which represents
#the computer's number of fingers.

def getComputerNum():
    num = random.randint(1,6)
    print("Computer shows", num)
    return num

#Function: determineWinner
#Parameter 1: userOption is an int (0 or 1) representing the user’s option
#Parameter 2: userInt is an int with the number of fingers (1-5)
#Parameter 3: computerInt is an int with the number of fingers (1-5)
#Return value: a string with the winner: "user" or "computer"
#This function determines the winner based on the sum of the number of fingers. '

def determineWinner(userOption, userInt, computerInt):
    total = userInt + computerInt
    print("The sum of the fingers is", total)

    if total % 2 == 0:  # even
        if userOption == 1:
            winner = "user"
        else:
            winner = "computer"
    else:
        if userOption == 0:  # odd
            winner = "user"
        else:
            winner = "computer"

    print("The winner is the", winner)
    return winner



#Function: main
#Parameters: None
#Return value: None
#This function is the starting point of this program.

def main():
    evenOdd = ["evens", "odds"]
    compWins = 0
    userWins = 0

    displayGameInfo()

    while userWins < 2 and compWins < 2:
        userOption = chooseOption(evenOdd)
        userNum = getUserNum()
        computerNum = getComputerNum()

        winner = determineWinner(userOption, userNum, computerNum)

        if winner == "user":
            userWins += 1
        else:
            compWins += 1

    if userWins == 2:
        print("You won 2 games!")
    else:
        print("Computer won 2 games.")


main()
