



#defining variables
nonNegative = 0
evenNonNegative = 0
total = 0
evenTotal = 0


print ("Even numbers")
print ("Enter an integer (negative number to quit)")

# getting user input
num = int(input("> "))



while num >= 0:
    nonNegative += 1
    total += num

#checking if number is even
    if num % 2 == 0:
        evenNonNegative += 1
        evenTotal += num

    num = int(input("> "))

print ("The count is", nonNegative)
print ("The total is", total)
print ("The count of even numbers is", evenNonNegative)
print ("The total of even numbers is", evenTotal)


#resetting values
nonNegative = 0
total = 0
oddCount = 0
oddTotal = 0

print ("\nOdd numbers")
print ("Enter an integer (negative number to quit)")

num = int(input("> "))

while num >= 0:
    nonNegative += 1
    total += num

# checking if number is odd
    if num % 2 != 0:
        oddCount += 1
        oddTotal += num

    num = int(input("> "))

print ("The count is", nonNegative)
print ("The total is", total)
print ("The count of odd numbers is", oddCount)
print ("The total of odd numbers is", oddTotal)


