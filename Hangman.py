'''
Description:
        You must create a Hangman game that allows the user to play and guess a secret word.  
        See the assignment description for details.
    
@author: Aloye Oshotse    ajo24
'''

import random

def handleUserInputDifficulty():
    '''
    This function asks the user if they would like to play the game in (h)ard or (e)asy mode, then returns the
    corresponding number of misses allowed for the game.
    '''

    print("How many misses do you want? \nHard has 8 and Easy has 12.")
    ret = input("(h)ard or (e)asy> ")
    if ret == 'e':
        print('you have 12 misses to guess word')
        return 12
    if ret == 'h':
        print('you have 8 misses to guess word')
        return 8


def getWord(words, length):
    '''
    Selects the secret word that the user must guess.
    This is done by randomly selecting a word from words that is of length length.
    '''

    potenword = [x for x in words if len(x) == length]
    return random.choice(potenword)


def createDisplayString(lettersGuessed, missesLeft, hangmanWord):
    '''
    Creates the string that will be displayed to the user, using the information in the parameters.
    '''
    ret = ""
    for x in sorted(lettersGuessed):
        if x == sorted(lettersGuessed)[-1]:
            ret += x
        else:
            ret += x + " "
    disstring = "letters you've guessed: " + str(ret)+'\n' + "misses remaining = " + str(missesLeft)+'\n' + " ".join(hangmanWord)
    return disstring


def handleUserInputLetterGuess(lettersGuessed, displayString):
    '''
    Prints displayString, then asks the user to input a letter to guess.
    This function handles the user input of the new letter guessed and checks if it is a repeated letter.
    '''

    num = 0
    while num == 0:
        print('\n'+displayString)
        ret = input("letter> ")
        if ret in lettersGuessed:
            print("you already guessed that")
        else:
            num += 1
    return ret


def updateHangmanWord(guessedLetter, secretWord, hangmanWord):
    '''
    Updates hangmanWord according to whether guessedLetter is in secretWord and where in secretWord guessedLetter is in.
    '''

    lst = []
    for x in range(len(list(secretWord))):
        if list(secretWord)[x] == guessedLetter:
            lst.append(x)
    for x in lst:
        hangmanWord[x] = guessedLetter
    return hangmanWord


def processUserGuess(guessedLetter, secretWord, hangmanWord, missesLeft):
    '''
    Uses the information in the parameters to update the user's progress in the hangman game.
    '''

    if guessedLetter not in secretWord:
        missesLeft -= 1
    lst = [updateHangmanWord(guessedLetter,secretWord,hangmanWord), missesLeft, guessedLetter in secretWord]
    return lst


def runGame(filename):
    '''
    This function sets up the game, runs each round, and prints a final message on whether or not the user won.
    True is returned if the user won the game. If the user lost the game, False is returned.
    '''

    f = open(filename)
    wordsClean = [w.strip() for w in f.read().split()]
    x = random.randint(5, 11)
    secretwords = getWord(wordsClean, x)
    difficulty = handleUserInputDifficulty()
    hangmanword = ['_' for _ in range(len(secretwords))]
    missesLeft = difficulty
    lettersguessed = []
    while missesLeft >= 0:
        displaystring = createDisplayString(lettersguessed, missesLeft, hangmanword)
        guessedletter = handleUserInputLetterGuess(lettersguessed,displaystring)
        updateHangmanWord(guessedletter, secretwords, hangmanword)
        process = processUserGuess(guessedletter, secretwords, hangmanword, missesLeft)
        if process[2] == True:
            lettersguessed.append(guessedletter)
        if process[2] == False:
            lettersguessed.append(guessedletter)
            missesLeft -= 1
            print("you missed: " + guessedletter + " not in word")
        if '_' not in hangmanword:
            print("you guessed the word: " + secretwords)
            print("you made ", len(lettersguessed), " guesses with ", difficulty - missesLeft, " misses")
            return True
    print("\nyou're hung!!"+'\n'+"word is " + secretwords)
    return False


if __name__ == "__main__":
    '''
          Running Hangman.py should start the game, which is done by calling runGame, therefore, we have provided you this code below.
          '''
    count = 0
    wins = 0
    loses = 0
    while count == 0:
        r = runGame('lowerwords.txt')
        if r:
            wins += 1
        if not r:
            loses += 1
        i = input("Do you want to play again? y or n> ")
        print('\n')
        if i == 'n':
            count += 1
        if i == 'y':
            count = 0
    print("You have won",wins,"game(s) and lost",loses,"game(s)")