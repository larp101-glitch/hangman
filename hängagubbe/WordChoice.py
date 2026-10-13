import random
import os

def Word():
    with open("GlobalWord.txt", "r", encoding="utf-8") as file:
        words = file.read().split()

    RandomWord = random.choice(words)
    CleanWord = "".join(char for char in RandomWord if char.isalnum() or char.isspace())

    return(CleanWord.upper())


def AdWord():
    WordAd = input("Add word to word pool?(if not: ENTER)\n")
    os.system(f"echo {WordAd} >> GlobalWord.txt")

