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
                word = random.choice(words)





            #beginning guessing process
    elif BeginInput == "N":
        print("No worries, come back when you are ready!")
        exit()
    else:
        print("Please enter a valid response (Y/N)")
        BeginInput = input("Are you ready to begin? (Y/N) (not case sensitive)").upper().strip()
    