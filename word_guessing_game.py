# File: homework6.py
# Assignment: Homework 6
# Description: This program is a word guessing game using lists.
# Author: Reet Sapra
# Email: reetsapr@usc.edu
# Section: Tictacs
# Instructor: Emily Millard

import random

# defining lists
words = ["tirebiter", "flower", "trashcan", "chocolate"]
jumbled = ["bretitier", "wlerfo", "arhcntsa", "ahotoeclc"]
hint = ["dog", "spring", "waste", "dessert"]

print ("There are", len(words), "word in the guessing game.\n")

# assigning random to lists
randWord = random.choice(words)
indexWord = words.index(randWord)

jumbleWord = jumbled[indexWord]
wordHint = hint[indexWord]

print ("A random word has been picked for you, and it has", len(jumbleWord), "letters.")

print ("The jumbled version of the word is \'", jumbleWord, "'", sep = "")

guess = input ("\nEnter your guess: ").strip().lower()
count = 1

# while loop if user guesses wrong answer
while guess != randWord:
    print ("Your guess is incorrect.")
    userHint = input ("Do you want a hint (y or n)? ")
    if userHint == "y" or userHint == "Y":
        print ("The hint is '", wordHint, "'", sep = "")

    print ("The jumbled word is \'", jumbleWord, "'", sep = "")
    guess = input ("\nEnter your guess: ").strip().lower()
    count += 1

# output if user guesses word correctly 
print ("The word is '", randWord, "'", sep = "")
print ("The number of guesses is", count)

