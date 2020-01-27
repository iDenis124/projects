import time
import os
import random
#----------------------------------
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
words = open("wordlist.txt").readlines()
userwords = []
#----------------------------------
def clear():
    return os.system("cls")

def EndScreen(losereason, currentword):
    if losereason == "1":
        print("You lost because that word has been used before!")
    elif losereason == "2":
        print("You lost because that is not a real word!")
    elif losereason == "3":
        print("You lost because it didn't start with the letter '{0}' ended in!".format(currentword))
    print("1: Play again")
    print("2: Exit game")
    quityesorno = str(input())
    if quityesorno == "1":
        print("Restarting game...")
        time.sleep(4)
        clear()
        GameStarting()
    if quityesorno == "2":
        print("Quitting game...")
        time.sleep(3)
        exit()
    else:
        print("That is not an option!")
        time.sleep(3)
        clear()
        EndScreen(losereason, currentword)

def checkword(currentword, currentletter):
    with open("wordlist.txt") as f:
        if currentword[0] == currentletter:
            if currentword in f.read():
                MainGame(currentletter)
            else:
                losereason = "2"
                EndScreen(losereason, currentword)
        else:
            losereason = "3"
            EndScreen(losereason, currentword)

def GameStarting():
    currentword = 1
    currentletter = 1
    iscurrentwordaword = 1
    del currentword
    del currentletter
    del iscurrentwordaword
    print("Who should pick a letter?")
    print("1: User")
    print("2: Computer")
    #
    #
    # A D D  R U L E S
    #
    #
    starting = str(input())
    if starting == "1":
        currentletter = str(input("Pick a letter!\n"))
        MainGame(currentletter)

    elif starting == "2":
        print("Picking a letter...")
        time.sleep(2)
        currentletter = random.choice(letters)
        print("The letter I have chosen is {0}".format(currentletter))
        currentword = input("Now say a word!\n")
        checkword(currentword, currentletter)
        MainGame(currentletter)

    else:
        print("That is not an option!")
        time.sleep(2)
        clear()
        GameStarting()

def MainGame(currentletter):
    possiblewords = [idx for idx in words if idx[0].lower() == currentletter.lower()] 
    [x for x in possiblewords if x not in userwords]
    currentword = random.choice(possiblewords)
    currentword = currentword.replace("\n","")
    currentletter = currentword[-1]
    currentword = currentword.lower()
    userwords.append(currentword)
    print(currentword)
    currentword = input()
    if currentword in userwords:
        losereason = "1"
        EndScreen(losereason, currentword)
    else:
        currentword = currentword.lower()
        userwords.append(currentword)
        checkword(currentword, currentletter)

#----------------------------------
print("Welcome to Untitled Word Game!")
time.sleep(1)
GameStarting()