# description: Text-based space adventure game
# Based on tutorial from Doug McNally: https://www.youtube.com/watch?v=miuHrP2O7Jw

import random
import time

def displayIntro():
    print("It is the end of a long year fighting space criminals")
    print("you come to crossroads on your trip home, one path leads home")
    print("where will you will be handsomly rewarded for a job well done")
    print("and the other leads through a gamma ray burst that will desintegrate you")
    print()

def choosePath():
    path = ""
    while path != "1" and path != "2":
        path = input("Which path will you choose? (1 or 2): ")

    return path

def checkPath(chosenPath):
    print("You head down the path")
    time.sleep(2)
    print("there's an asteroid nearby that looks familiar, that must be a good sign...")
    print()
    time.sleep(2)

    correctPath = random.randint(1, 2)

    if chosenPath == str(correctPath):
        print("That tingling was just the feeling of admiration from the citizens of the galaxy!")
        print("Welcome home")
    else: 
        print("An extremely energetic burst of gamma rays pass through you")
        print("causing all the atoms in your body to dissociate")
        print("there is no record left of your existence.")

playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    displayIntro()
    choice = choosePath()
    checkPath(choice)
    playAgain = input("Do you want to play again? (yes or y to continue playing): ")

