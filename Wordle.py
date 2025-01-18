wordBank = open("Wordle word list.txt").read().splitlines()
numGuess = []
win = 0
guessNum = -1
import random
from termcolor import colored
answer = random.choice(wordBank)

def contents(word):
    contents = []
    for letter in word:
        contents += letter
    return contents
answerContents = contents(answer)

def build_display():
    global numGuess, guessNum
    counter = 0
    x = 0
    for letter in guessContents:
        if userGuess[counter] is answerContents[counter]:
            x = 1
            if counter != 5:
                print(colored(userGuess[counter], "green"), end="")
            else:
                print(colored(userGuess[counter], "green"))

        if userGuess == answer:
            win = 1
            print(win)

        if userGuess[counter] in answer and x == 0:
            if counter != 5:
                print(colored(userGuess[counter], "yellow"), end="")
                print("", end="")
            else:
                print(colored(userGuess[counter], "yellow"))
                print()
        if letter not in answer:
            if counter != 5:
                print(colored(letter, "dark_grey"), end="")
                print("", end="")
            else:
                print(colored(letter, "dark_grey"))
                print()
        counter += 1
        x = 0
    print()

while win != 1 or guessNum != 6:
    guessNum += 1
    while True:

        print("Please enter a 5-letter word.")
        userGuess = input("").lower()
        if len(userGuess) != 5:
            print("That is an invalid word.")
            continue
        else:
            numGuess = []
            numGuess += userGuess
            break

    guessContents = contents(userGuess)

    build_display()
    print(guessNum)