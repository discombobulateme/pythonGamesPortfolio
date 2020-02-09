# Based on tutorial https://trinket.io/python/e5a03e7cbc

# Setup
yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]
actions = ["scream", "talk", "help", "violence"]
 
# Introduction
name = input("What is your name, adventurer?\n")
print("Greetings, " + name + ". Let us go on a quest!")
print("You find yourself on the edge of a dark forest.")
print("Can you find your way through?\n")

# Start of game
response = ""
while response not in yes_no:
    response = input("Would you like to step into the forest?\nyes/no\n")
    if response == "yes":
        print("You head into the forest. You hear crows cawwing in the distance.\n")
    elif response == "no":
        print("You are not ready for this quest. Goodbye, " + name + ".")
        quit()
    else: 
        print("I didn't understand that.\n")
 
# First part of the game
response = ""
while response not in directions:
    print("To your left, you see a bear.")
    print("To your right, there is more forest.")
    print("There is a rock wall directly in front of you.")
    print("Behind you is the forest exit.\n")
    response = input("What direction do you move?\nleft/right/forward/backward\n")
    if response == "left":
        print("The bear eats you. Farewell, " + name + ".")
        quit()
    elif response == "right":
        print("You head deeper into the forest.\n")
    elif response == "forward":
        print("You cannot scale the wall.\n")
        response = "" 
    elif response == "backward":
        print("You leave the forest. Goodbye, " + name + ".")
        quit()
    else:
        print("I didn't understand that.\n")

# Second part of the game
response = ""
while response not in actions:
    print("You can scream and cry untill there's no more air out of your lungs.")
    print("You can talk and try to understand each other through comprehension and empathy.")
    print("You can hide and call for help.")
    print("You can use all the weapons around and try to kill the beast.\n")
    response = input("What do you do?\nscream/talk/help/violence\n")
    if response == "scream":
        print("You screamed and cried so much that now you will have a slow dehidrathion process, " + name + ".")
        quit()
    elif response == "talk":
        print("You don't speak the same language, a rational talk is not possible.\n")
    elif response == "help":
        print("There is no signal in the forrest, and no one can hear you.\n")
        response = "" 
    elif response == "violence":
        print("Oh no! You were smashed in the first hit. Goodbye, " + name + ".")
        quit()
    else:
        print("I didn't understand that.\n")
