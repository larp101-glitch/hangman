import WordChoice
import os

def InGame(SemiCorectWord,tryes,tryed):
    os.system("clear")
    print(f"[{tryed}]\nTries left: {tryes}\n{SemiCorectWord}")

def Lose():
    os.system("clear")
    os.system("cat Napoleon.txt")
    print("Just like Napoleon said, there's nothing we can do:(")

def Win():
    os.system("clear")
    os.system("cat Terminator.txt")
    print("Winning isn't for everyone but it is for you!!")
