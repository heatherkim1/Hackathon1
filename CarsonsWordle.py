#TO DO:
#create guessing system
#UI improvements
#adjust timing
#randomize words
#Call spanish/english txt file
#------------------------------------------
#importing QOL 
import random
import time
from time import sleep
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
                    allText = file.read()
                    words = list(map(str, allText.split()))
                    print("english file opened!")
            elif language == "spanish":
                #opening spanish file
                print("¡Has seleccionado español!")
                print("abriendo archivo en español..")
                with open("WordleWordsSpanish.txt", "r") as file:
                    allText = file.read()
                    words = list(map(str, allText.split()))
                    print("¡Archivo en español abierto!")

            else:
                print("Please pick either english or spanish!")
                sleep(2)
                language()
        language()
        break
    elif BeginInput == "N":
        print("Okay, goodbye!")
        sleep(2)
        quit()
    else:
        print("Please pick either Y or N!")
        sleep(2)
        BeginInput = input("Are you ready to begin? (Y/N) (not case sensitive)").upper().strip()
