import json
import pandas as pd
import random
from nltk.corpus import words

maxGuesses = 6
numWrongGuesses = -1
lettersGuessed = []
guessedLetter = ""

hung = [
    "     _____\n    |     |\n    |     O\n    |\n    |\n    |\n____|____\n",
    "     _____\n    |     |\n    |     O\n    |     |\n    |\n    |\n____|____\n",
    "     _____\n    |     |\n    |     O\n    |    \|\n    |\n    |\n____|____\n",
    "     _____\n    |     |\n    |     O\n    |    \|/\n    |\n    |\n____|____\n",
    "     _____\n    |     |\n    |     O\n    |    \|/\n    |     |\n    |\n____|____\n",
    "     _____\n    |     |\n    |     O\n    |    \|/\n    |     |\n    |    /\n____|____\n",
    "     _____\n    |     |\n    |     O\n    |    \|/\n    |     |\n    |    / \\\n____|____\n",
]


df = pd.DataFrame(words.words())
df.columns = ["words"]
filt = (
    (df["words"].str.len() > 5)
    & (df["words"].str.len() < 15)
    & (df["words"].str.islower())
)
df = df.loc[filt]
randomNumber = random.randrange(len(df))
magicWord = df.iloc[randomNumber].values[0]
dictWord = list(magicWord)
dfw = pd.DataFrame([dictWord])
dfw = dfw.T
dfw.index.rename("Id", inplace=True)
dfw.columns = ["letter"]
dfw["isGuessed"] = "_ "

print(f"Ready! Set! Go! Your word is {len(magicWord)} letters long. Good luck!")


def currentWord(pd_df):
    columnSeriesObj = dfw["isGuessed"]
    currentword = ""
    for c in columnSeriesObj:
        currentword = currentword + c
    # print(currentWord)
    return currentword


def userGuess(letter, frame):
    global numWrongGuesses
    if (letter.isalpha() == False) or (len(letter) > 1):
        print("You can only enter a single letter.")
        return False
    elif letter in lettersGuessed:
        print("You already guessed that letter. Please pick another.")
        return False
    elif letter in dfw.letter.values:
        filt = dfw["letter"] == letter
        dfw.loc[filt, "isGuessed"] = letter
        if currentWord(dfw) == magicWord:
            return True
    else:
        numWrongGuesses = numWrongGuesses + 1
        print(hung[numWrongGuesses])
    lettersGuessed.append(guessedLetter)
    return False


while numWrongGuesses < maxGuesses:
    guessedLetter = input("Please enter a letter: ")
    guessedLetter = guessedLetter.lower()
    if userGuess(guessedLetter, dfw):
        print(f"Congratulations. You figured out the magic word")
        break
    else:
        print(currentWord(dfw))
if numWrongGuesses == maxGuesses:
    print("Game Over! You failed to guess the word.")
