wordBank = open("Wordle word list.txt").read().splitlines()
keyboardDisplay = {"q" : "white", "w" : "white", "e" : "white", "r" : "white", "t" : "white", "y" : "white", "u" : "white", "i" : "white", "o" : "white", "p" : "white", "a" : "white", "s" : "white", "d" : "white", "f" : "white", "g" : "white", "h" : "white", "j" : "white", "k" : "white", "l" : "white", "z" : "white", "x" : "white", "c" : "white", "v" : "white", "b" : "white", "n" : "white", "m" : "white",}
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
    print("       ", end="")
    for letter in guessContents:
        if userGuess[counter] is answerContents[counter]:
            x = 1
            keyboardDisplay[letter] = "green"
            if counter != 5:
                print(colored(userGuess[counter], "green"), end="")
                print(" ", end="")
            else:
                print(colored(userGuess[counter], "green"))
                print(" ")

        if userGuess == answer:
            win = 1
            print(win, end="")

        if userGuess[counter] in answer and x == 0:
            keyboardDisplay[letter] = "yellow"
            if counter != 5:
                print(colored(userGuess[counter], "yellow"), end="")
                print(" ", end="")
            else:
                print(colored(userGuess[counter], "yellow"))
                print(" ")
        if letter not in answer:
            keyboardDisplay[letter] = "dark_grey"
            if counter != 5:
                print(colored(letter, "dark_grey"), end="")
                print(" ", end="")
            else:
                print(colored(letter, "dark_grey"))
                print(" ")
        counter += 1
        x = 0
    print("\n")
    print(colored("Q ", keyboardDisplay["q"]), end="")
    print(colored("W ", keyboardDisplay["w"]), end="")
    print(colored("E ", keyboardDisplay["e"]), end="")
    print(colored("R ", keyboardDisplay["r"]), end="")
    print(colored("T ", keyboardDisplay["t"]), end="")
    print(colored("Y ", keyboardDisplay["y"]), end="")
    print(colored("U ", keyboardDisplay["u"]), end="")
    print(colored("I ", keyboardDisplay["i"]), end="")
    print(colored("O ", keyboardDisplay["o"]), end="")
    print(colored("P ", keyboardDisplay["p"]))
    print(" ", end="")
    print(colored("A ", keyboardDisplay["a"]), end="")
    print(colored("S ", keyboardDisplay["s"]), end="")
    print(colored("D ", keyboardDisplay["d"]), end="")
    print(colored("F ", keyboardDisplay["f"]), end="")
    print(colored("G ", keyboardDisplay["g"]), end="")
    print(colored("H ", keyboardDisplay["h"]), end="")
    print(colored("J ", keyboardDisplay["j"]), end="")
    print(colored("K ", keyboardDisplay["k"]), end="")
    print(colored("L ", keyboardDisplay["l"]))
    print("  ", end="")
    print(colored("Z ", keyboardDisplay["z"]), end="")
    print(colored("X ", keyboardDisplay["x"]), end="")
    print(colored("C ", keyboardDisplay["c"]), end="")
    print(colored("V ", keyboardDisplay["v"]), end="")
    print(colored("B ", keyboardDisplay["b"]), end="")
    print(colored("N ", keyboardDisplay["n"]), end="")
    print(colored("M ", keyboardDisplay["m"]))

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