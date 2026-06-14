

print(basketball[1])
import random

score = 0

for num in range(1,6):
    print("\nPlay game #" + str(num))
    caseNum = int(input("Enter a case number (1-5): "))

    while caseNum < 1 or caseNum > 5:
        caseNum = int(input("Enter a case number (1-5): "))

    print("You are playing for Case", caseNum)
    print ("To win, roll one of the following numbers")
    if caseNum == 1:
        for win in range(2, 21, 2):
            print(win, end="  ")
    if caseNum == 2:
        for win in range (1, 20, 2):
            print(win, end="  ")
    if caseNum ==3:
        for win in range(5,11):
            print(win, end="  ")
    if caseNum == 4:
        for win in range(10, 21, 2):
            print(win, end="  ")
    if caseNum == 5:
        for win in range(3, 19, 3):
            print(win, end="  ")
    roll = random.randint(1,20)
    print ("\nYou rolled a", roll)

    if caseNum == 1 and roll % 2 == 0:
        print ("You win 50 points!")
        score +=50
    elif caseNum == 2 and roll % 2 == 1:
        score +=50
        print("You win 50 points!")
    elif caseNum ==3 and roll >=5 and roll <=10:
        score +=50
        print("You win 50 points!")
    elif caseNum == 4 and roll >=10 and roll % 2 == 0:
        score +=50
        print("You win 50 points!")
    elif caseNum == 5 and roll % 3 == 0:
        score +=50
        print("You win 50 points!")
    else:
        print ("You didn't win.")

print ("Your total score is", score, "points.")
