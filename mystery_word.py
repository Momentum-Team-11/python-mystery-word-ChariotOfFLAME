import string
from random import choice


file = open("words.txt")  # Open the file
words = file.read().upper().split()  # read the file and make it a string that is uppercase


def play_game():
    play = True
    while play is True:
        word = choice(words)
        word = word.replace("\n", "")  # erase the \n
        wordList = []  # make an empty list for the word
        wordList[:0] = word  # take each letter and make them the items of the list
        guessList = []  # make a list for the guessed letters
        print(f"Your word is {len(word)} letters long.")  # tell the player how long the word is
        resultsList = str("_ " * len(word)).split()  # create a list of for the results with each item being "_ "
        guessedLetters = ''  # make a string for guessed letters
        guesses = 8  # create a counter for the number of incorrect guesses available
        guessCounter = 0  # create a counter for the number of total guesses
        while guesses != 0 and resultsList != wordList:
            results = ' '.join([str(item) for item in resultsList])  # create a text string to show the results to the player
            print(f"""
{results}
""")  # show the user the current results
            print(f"You've guessed{guessedLetters}")  # show the user the letters they've guessed
            playerLetter = input(f"You have {guesses} incorrect guesses left. What letter do you guess?").upper()  # uppercase the users input
            print("_____________________________________________")
# ---------- HANDLE ERRORS --------------- #
            if playerLetter.isdigit():  # filter out numbers
                print("Only letters are in this word!")
                continue  # start the while loop over
            if playerLetter in string.punctuation:  # filter out symbols
                print("Only letters are in this word!")
                continue  # start the while loop over
            if playerLetter == " ":  # filter out spaces
                print("Only letters are in this word!")
                continue  # start the while loop over
            if len(playerLetter) != 1:  # filter out more than one letter
                print("Just one letter please!")
                continue  # start the while loop over
            if playerLetter in guessList:  # filter out previous guesses
                print("WHOOPS! You guessed this letter already. Try a different one!")
                continue  # start the while loop over
# ---------- END ERROR HANDLING ---------- #
            if playerLetter not in wordList:  # if they guess wrong...
                guesses = guesses - 1  # decriment the incorrect guess counter
                guessList.append(playerLetter)  # add the guessed letter to the LIST of guessed letters
                guessedLetters += f" {playerLetter}, "  # add the guessed letter to the STRING of guessed letters
                print("""
OH NO! That wasn't right...
""")  # and start the while loop over
            else:  # if they guess right...
                idx = 0  # create an index counter for the results list
                for letter in wordList:
                    if playerLetter != letter:  # if the guessed letter isn't the current letter...
                        idx += 1  # incriment the index
                    if playerLetter == letter:  # if the guessed letter IS the current letter...
                        resultsList[idx] = letter  # make the results list item at the indicated index position the current letter
                        idx += 1  # incriment the index
                guessList.append(playerLetter)  # add the guessed letter to the LIST of guessed letters
                guessedLetters += f" {playerLetter}, "  # add the guessed letter to the STRING of guessed letters
            guessCounter += 1  # incriment the guess counter
        if guesses == 0:  # if you run out of inccorect guesses...
            print(f"You ran out of guesses... the word was {word}. Better luck next time!")
        if resultsList == wordList:  # if the results list is the same as the word list...
            results = ' '.join([str(item) for item in resultsList])  # create a text string to show the results to the player
            print(results)
            print(f"""CONGRADULATIONS! The word was {word}!
You guessed{guessedLetters}, which means...
You got the word in {guessCounter} guesses!""")
        playAgain = input("Would you like to play again?")
        if "n" in playAgain:
            print("""_____________________________________________
Ok! Run me again when you want to play!""")
            play = False
        if "y" in playAgain:
            print("""_____________________________________________
Alright!!! Here we go!!!
""")


if __name__ == "__main__":
    play_game()
