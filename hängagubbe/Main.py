import WordChoice
import screen
import MusicProducer
import os

Word = WordChoice.Word()
CorectLetters = {" "}
WordSemiHidden = "".join(char if char in CorectLetters else "_" for char in Word)
TriedLetters = {" "}
Game = True
i = 5
WinGame = False

while i > 0:
    WordSemiHidden = "".join(char if char in CorectLetters else "_" for char in Word)
    screen.InGame(WordSemiHidden, i, TriedLetters)
    gues = input("Guess letter:\n").upper()
    if gues.upper() in Word.upper():
        CorectLetters.add(gues)
    else:
        i = i - 1
        TriedLetters.add(gues)

    if Word == WordSemiHidden:
        i = 0
        WinGame = True
    else:
        WinGame = False


if WinGame == True:
    MusicProducer.terminator()
    screen.Win()
elif WinGame == False:
    MusicProducer.napoleon()
    screen.Lose()
else:
    print("Somehow you didn't lose yet you didn't win")

WordChoice.AdWord()
os.system("clear")
