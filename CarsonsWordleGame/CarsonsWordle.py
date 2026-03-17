#Carson Everhart
#Period 6
#Python Group Project - Wordle
#Time spent: 3 days

#importing QOL imports (time, random, sleep)
import random
import time
from time import sleep
#spacing is simply for speeding up wait process.
spacing = 2
#beginning tutorial and welcoming, preparing file.
print("Hello there! Welcome to wordle!")
sleep(spacing)
name = input("What is your name?")
print("Alrighty " + name + "! There will be a random 5 letter word you have to guess!")
sleep(spacing)
print("Please make sure to guess when told to! we will tell you which letters are correct, incorrect, or in the wrong place.")
sleep(spacing + 1)
print("your job is to guess the correct word!")
sleep(spacing)
#beginning input process!
while True:
    BeginInput = input("Are you ready to begin? (Y/N) (not case sensitive)").upper().strip()
    #beginning inputs
    if BeginInput == "Y":
        print("Great! Let's get started!")
        sleep(spacing)
        break
    elif BeginInput == "N":
        #if not ready, ends program
        print("Take your time, we will be here when you are ready!")
        exit()
    else:
        #if invalid input, asks again infinently
        print("Please enter a valid response (Y/N) (not case sensitive)")
        sleep(0.5)
while True:
    language = input("Please select a language (English/Spanish) (not case sensitive)").upper().strip()
    if language == "ENGLISH":
        #ENGLISH PICKING!!
        print("You have chosen english!")
        sleep(spacing)
        #beginning word selection process
        with open("CarsonsWordleGame/WordleWords.txt", "r") as file:
            alltext = file.read()
            words = list(map(str, alltext.split()))
            #picking random word
            wordle = random.choice(words)
            break
        #- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
        #Picking spanish
    elif language == "SPANISH":
        #spanish word selection process
        print("¡Has elegido español!")
        sleep(spacing)
        with open("CarsonsWordleGame/WordleWordsSpanish.txt", "r") as file:
            alltext = file.read()
            words = list(map(str, alltext.split()))
            #picking random word
            wordle = random.choice(words)
            break
    else:
        #if invalid input, tries again infinently
        print("Please enter a valid response (English/Spanish)")
        print("Por favor ingrese una respuesta válida (Inglés/Español)")
        sleep(0.5)

while True:
    def check_place(char_g, char_w, place):
        if char_g == char_w:
            print(place + " letter: right letter, right place!")
    guess = input("Please enter your first guess! (5 letter word)").lower().strip()
    #Checks to make sure its a 5 letter word.
    while len(guess) != 5:
        print("That was not a 5 letter word, please try again!")
        guess = input("Please enter your first guess! (5 letter word)").lower().strip()
        print("Your guess was " + guess + "!")
    #a loop that repeats for each guess
    for i in range(5):
        #checks if guess is correct, if not, checks each letter and gives feedback.
        if wordle == guess:
            print("Congratulations! You guessed the word correctly!")
            with open("CarsonsWordleGame/WordlePlayLogs.txt", "a") as file:
                file.write((name + " guessed the word " + wordle + " in " + str(i + 1) + " guesses! in " + language + " \n"))
            file.close()
            exit()
        if not any(letter in wordle for letter in guess):
            print("Nothing matches!")
        #calculates whats correct
        check_place(guess[0], wordle[0], "First")
        if guess[0] == wordle[1] or guess[0] == wordle[2] or guess[0] == wordle[3] or guess[0] == wordle[4]:
            #checks first letter
            print("First letter: right letter, wrong place!")
        check_place(guess[1], wordle[1], "Second")
        if guess[1] == wordle[0] or guess[1] == wordle[2] or guess[1] == wordle[3] or guess[1] == wordle[4]:
            #checks second letter
            print("Second letter: right letter, wrong place!")
        check_place(guess[2], wordle[2], "Third")
        if guess[2] == wordle[0] or guess[2] == wordle[1] or guess[2] == wordle[3] or guess[2] == wordle[4]:
            #checks third letter
            print("Third letter: right letter, wrong place!")
        check_place(guess[3], wordle[3], "Fourth")
        if guess[3] == wordle[0] or guess[3] == wordle[1] or guess[3] == wordle[2] or guess[3] == wordle[4]:
            #checks fourth letter
            print("Fourth letter: right letter, wrong place!")
        check_place(guess[4], wordle[4], "Fifth")
        if guess[4] == wordle[0] or guess[4] == wordle[1] or guess[4] == wordle[2] or guess[4] == wordle[3]:
            #checks fifth letter
            print("Fifth letter: right letter, wrong place!")
        print("You have " + str(5 - i) + " guesses left!")
        guess = input("please enter your next guess! (5 letter word)").lower().strip()
        while len(guess) != 5:
            print("That was not a 5 letter word, please try again!")
            guess = input("Please enter your next guess! (5 letter word)").lower().strip()
    #if you have no more guesses, ends the game and reveals the word.
    if guess != wordle:
        print("You have no more guesses, sadly the word was " + wordle + "!")
        sleep(spacing)
        print("better luck next time!")
        with open("CarsonsWordleGame/WordlePlayLogs.txt", "a") as falsefile:
            falsefile.write((name + " failed to guess the word " + wordle + " in 6 guesses! in" + language + " \n"))
        falsefile.close()
        exit()


    
