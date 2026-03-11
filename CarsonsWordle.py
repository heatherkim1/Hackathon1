#TO DO:
#create guessing system
#UI improvements
#implement  retry feature
#reveal word at end

#------------------------------------------
#importing QOL imports (time, random, sleep)
import random
import time
from time import sleep
#spacing is simply for speeding up wait process.
spacing = 0
#beginning tutorial and welcoming, preparing file.
print("Hello there! Welcome to wordle!")
sleep(spacing)
print("There will be a random 5 letter word you have to guess!")
sleep(spacing)
print("Please make sure to guess when told to! we will tell you which letters are correct, incorrect, or in the wrong place.")
sleep(spacing + 1)
print("your job is to guess the correct word!")
sleep(spacing)
#beginning input!!!
BeginInput = input("Are you ready to begin? (Y/N) (not case sensitive)").upper().strip()

while True:
    #beginning inputs
    if BeginInput == "Y":
        print("Great! Let's get started!")
        sleep(spacing)
        language = input("Please select a language (English/Spanish) (not case sensitive)").upper().strip()
        if language == "ENGLISH":
            #ENGLISH PICKING!!
            print("You have chosen english!")
            sleep(spacing)
            #beginning word selection process
            with open("WordleWords.txt", "r") as file:
                alltext = file.read()
                words = list(map(str, alltext.split()))
                #picking random word
                wordle = random.choice(words)
        elif language == "SPANISH":
            #spanish word sleection process
            print("You have chosen spanish!")
            sleep(spacing)
            with open("WordleWordsSpanish.txt", "r") as file:
                alltext = file.read()
                words = list(map(str, alltext.split()))
                #picking random word
                wordle = random.choice(words)
        else:
            print("Please enter a valid response (English/Spanish)")
            language = input("Please select a language (English/Spanish) (not case sensitive)").upper().strip()
            sleep(0.5)
        





            #beginning guessing process
    elif BeginInput == "N":
        print("No worries, come back when you are ready!")
        exit()
    else:
        print("Please enter a valid response (Y/N)")
        BeginInput = input("Are you ready to begin? (Y/N) (not case sensitive)").upper().strip()
    def check_place(char_g, char_w, place):
        if char_g == char_w:
            print(place + " letter: right letter, right place!")
    guess = input("Please enter your first guess! (5 letter word)").lower().strip()
    #Checks to make sure its a 5 letter word.
    while len(guess) != 5:
        print("That was not a 5 letter word, please try again!")
        guess = input("Please enter your first guess! (5 letter word)").lower().strip()
    #a loop that repeats for each guess
    for i in range(5):
        #checks if guess is correct, if not, checks each letter and gives feedback.
        if wordle == guess:
            print("Congratulations! You guessed the word correctly!")
            break
        check_place(guess[0], wordle[0], "First")
        if guess[0] == wordle[1] or guess[0] == wordle[2] or guess[0] == wordle[3] or guess[0] == wordle[4]:
            print("First letter: right letter, wrong place!")
        check_place(guess[1], wordle[1], "Second")
        if guess[1] == wordle[0] or guess[1] == wordle[2] or guess[1] == wordle[3] or guess[1] == wordle[4]:
            print("Second letter: right letter, wrong place!")
        check_place(guess[2], wordle[2], "Third")
        if guess[2] == wordle[0] or guess[2] == wordle[1] or guess[2] == wordle[3] or guess[2] == wordle[4]:
            print("Third letter: right letter, wrong place!")
        check_place(guess[3], wordle[3], "Fourth")
        if guess[3] == wordle[0] or guess[3] == wordle[1] or guess[3] == wordle[2] or guess[3] == wordle[4]:
            print("Fourth letter: right letter, wrong place!")
        check_place(guess[4], wordle[4], "Fifth")
        if guess[4] == wordle[0] or guess[4] == wordle[1] or guess[4] == wordle[2] or guess[4] == wordle[3]:
            print("Fifth letter: right letter, wrong place!")
        guess = input("please enter your next guess! (5 letter word)").lower().strip()
        while len(guess) != 5:
            print("That was not a 5 letter word, please try again!")
            guess = input("Please enter your next guess! (5 letter word)").lower().strip()
        if guess != wordle:
            print("You have no more guesses, sadly the word was " + wordle + "!")
            sleep(spacing)
            print("beter luck next time!")
            break


    
