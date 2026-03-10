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
    if BeginInput == "Y":
        #get language
        def language():

            language = input("What language would you like to use? (English/Spanish) (not case sensitive)").lower().strip()
            #Language selection, about to call for language file.
            if language == "english":
                print("You have selected english!")
                #opening english file
                print("opening english file..")
                with open("WordleWords.txt", "r") as file:
                    sleep(1)
                    allText = file.read()
                    words = list(map(str, allText.split()))
                    print("english file opened!")
                    wordle = random.choice(words)

                #spacing lets me see easier.

            elif language == "spanish":
                #opening spanish file
                print("¡Has seleccionado español!")
                print("abriendo archivo en español..")
                with open("WordleWordsSpanish.txt", "r") as file:
                    sleep(1)
                    allText = file.read()
                    words = list(map(str, allText.split()))
                    print("¡Archivo en español abierto!")
                    wordle = random.choice(words)
            #if they dont pick either, reask



            else:
                print("Please pick either english or spanish!")
                sleep(2)
                language()
        language()
        break
    elif BeginInput == "N":
        #ends
        print("Okay, goodbye!")
        sleep(2)
        quit()


    else:
        #if they dont pick either, reask
        print("Please pick either Y or N!")
        sleep(2)
        BeginInput = input("Are you ready to begin? (Y/N) (not case sensitive)").upper().strip()
