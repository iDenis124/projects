import time
import getpass
import webbrowser
import pyttsx3
import os
import random
import pyperclip
import colorama
from colorama import Fore, Style
# -----------------------------------
user = getpass.getuser()
engine = pyttsx3.init()
greetings = ["Good day", "Good night", "How the fuck are you",
             "It's you", "Motherfucking", "Fuck boy"]
# -----------------------------------


def bootup():
    print(Fore.MAGENTA + r"""
     ____                    ____   _____
    |  _ \                  / __ \ / ____|
    | |_) | ___  __ _ _ __ | |  | | (___  
    |  _ < / _ \/ _` | '_ \| |  | |\___ \ 
    | |_) |  __/ (_| | | | | |__| |____) |
    |____/ \___|\__,_|_| |_|\____/|_____/
    """)
    print(Fore.WHITE + "")
    engine.say("{0}, {1}".format(random.choice(greetings), user))
    engine.runAndWait()
    print("Opening the Bootloader")
    time.sleep(3)
    print("Ensuring Dank Memes")
    time.sleep(3)
    print("Removing Past Data")
    time.sleep(3)
    print("DONE")
    time.sleep(1)
    clear()


def clear():
    return os.system('cls')


def MainMenu():
    print("Please choose an option")
    print("")
    time.sleep(1)
    print("1: Google")
    print("2: Reddit")
    print("3: Games")
    print("4: File Manager")
    print("?: Learn more about BeanOS")
    option = str(input())
    clear()
    if(option == "1"):
        googleRAW = input("What would you like to search?\n")
        google = googleRAW.replace(" ", "+")
        webbrowser.open_new_tab(
            "https://www.google.com/search?q={0}".format(google))
    elif(option == "2"):
        print("Please specify a subreddit")
        print("")
        print("Here are some suggestions:")
        print("r/dankmemes")
        print("r/whoooosh")
        print("r/yiff")
        subredditRAW = input()
        subreddit = subredditRAW.replace("r/", "")
        webbrowser.open_new_tab(
            "https://www.reddit.com/r/{0}".format(subreddit))
    elif(option == "3"):
        print("Games still WIP")
        clear()
        MainMenu()
    elif(option == "4"):
        print("Booting up")
        time.sleep(1)
        clear()
        FileManager()
    elif(option == "?"):
        print("Copyright Fern#8592")
        input()
    else:
        print("That in not an option!")
        input()


def FileManager():
    print("1: Drive C:")
    print("2: Drive D:")
    files = str(input())
    if(files == "1"):
        clear()
        print("1: {0}'s files".format(user))
        print("2: Programs")
        print("3: BeanOS")
        files = str(input())
        if(files == "1"):
            clear()
            print("*empty*")
            input()
            clear()
            FileManager()
        elif(files == "2"):
            clear()
            print("1: Boot")
            print("2: Main Menu")
            print("3: File Manager")
            print("4: English to Standard Galactic Alphabet")
            files = str(input())
            if(files == "1"):
                clear()
                bootup()
                clear()
                FileManager()
            elif(files == "2"):
                clear()
                MainMenu()
            elif(files == "3"):
                clear()
                FileManager()
            elif(files == "4"):
                clear()
                SGAtranslator()
                FileManager()
            else:
                print("That is not an option")
                input()
                clear()
                FileManager()
        elif(files == "3"):
            clear()
            print("1: Somalia man")
            print("2: Club penguin")
            files = str(input())
            if(files == "1"):
                clear()
                print("Hello am 48 year man from somalia. Sorry for my bed england. I selled my wife for internet connection for play 'conter stirk' and i want to become the goodest player like you I play with 400 ping on brazil server and i am Global elite 2.pls no copy pasterino my story.")
                engine.say("Hello am 48 year man from somalia. Sorry for my bed england. I selled my wife for internet connection for play 'conter stirk' and i want to become the goodest player like you I play with 400 ping on brazil server and i am Global elite 2.pls no copy pasterino my story.")
                engine.runAndWait()
                clear()
                FileManager()
            elif(files == "2"):
                clear()
                print("apology for bad english where were u wen club penguin die i was at house eating dorito when phone ring 'club penguin is kill' 'no'")
                engine.say(
                    "apology for bad english where were u wen club penguin die i was at house eating dorito when phone ring 'club penguin is kill' 'no'")
                engine.runAndWait()
                clear()
                FileManager()
        else:
            print("That is not an option")
            input()
            clear()
            FileManager()
    elif(files == "2"):
        print("You can't afford another drive")
        input()
        clear()
        FileManager()
    else:
        print("That is not an option")
        input()
        clear()
        FileManager()


def SGAtranslator():
    print("1: English to Standard Galactic Alplabet")
    print("2: Standard Galactic Alplabet to English")
    TranslationMode = str(input())
    if(TranslationMode == "1"):
        Sentence = input("What sentence would you like translated?\n")
        Sentence = Sentence.replace("a", "ᔑ")
        Sentence = Sentence.replace("b", "ʖ")
        Sentence = Sentence.replace("c", "ᓵ")
        Sentence = Sentence.replace("d", "↸")
        Sentence = Sentence.replace("e", "ᒷ")
        Sentence = Sentence.replace("f", "⎓")
        Sentence = Sentence.replace("g", "⊣")
        Sentence = Sentence.replace("h", "⍑")
        Sentence = Sentence.replace("i", "╎")
        Sentence = Sentence.replace("j", "⋮")
        Sentence = Sentence.replace("k", "ꖌ")
        Sentence = Sentence.replace("l", "ꖎ")
        Sentence = Sentence.replace("m", "ᒲ")
        Sentence = Sentence.replace("n", "リ")
        Sentence = Sentence.replace("o", "𝙹")
        Sentence = Sentence.replace("p", "!¡")
        Sentence = Sentence.replace("q", "ᑑ")
        Sentence = Sentence.replace("r", "∷")
        Sentence = Sentence.replace("s", "ᓭ")
        Sentence = Sentence.replace("t", "ℸ ̣")
        Sentence = Sentence.replace("u", "⚍")
        Sentence = Sentence.replace("v", "⍊")
        Sentence = Sentence.replace("w", "∴")
        Sentence = Sentence.replace("x", "̇/")
        Sentence = Sentence.replace("y", "||")
        Sentence = Sentence.replace("z", "⨅")
    elif(TranslationMode == "2"):
        Sentence = input("What sentence would you like translated?\n")
        Sentence = Sentence.replace("ᔑ", "a")
        Sentence = Sentence.replace("ʖ", "b")
        Sentence = Sentence.replace("ᓵ", "c")
        Sentence = Sentence.replace("↸", "d")
        Sentence = Sentence.replace("ᒷ", "e")
        Sentence = Sentence.replace("⎓", "f")
        Sentence = Sentence.replace("⊣", "g")
        Sentence = Sentence.replace("⍑", "h")
        Sentence = Sentence.replace("╎", "i")
        Sentence = Sentence.replace("⋮", "j")
        Sentence = Sentence.replace("ꖌ", "k")
        Sentence = Sentence.replace("ꖎ", "l")
        Sentence = Sentence.replace("ᒲ", "m")
        Sentence = Sentence.replace("リ", "n")
        Sentence = Sentence.replace("𝙹", "o")
        Sentence = Sentence.replace("!¡", "p")
        Sentence = Sentence.replace("ᑑ", "q")
        Sentence = Sentence.replace("∷", "r")
        Sentence = Sentence.replace("ᓭ", "s")
        Sentence = Sentence.replace("ℸ ̣", "t")
        Sentence = Sentence.replace("⚍", "u")
        Sentence = Sentence.replace("⍊", "v")
        Sentence = Sentence.replace("∴", "w")
        Sentence = Sentence.replace("/", "x")
        Sentence = Sentence.replace("||", "y")
        Sentence = Sentence.replace("⨅", "z")
    pyperclip.copy(Sentence)
    print("It has been copied to your clipboard!")
    time.sleep(1)
    clear()
    SGAtranslator()


# -----------------------------------
bootup()
while True:
    clear()
    MainMenu()
