import random, os, time
score = 0
winner = False
def loading():
    time.sleep(1)
    clear()
    print("Loading.")
    time.sleep(.5)
    clear()
    print("Loading..")
    time.sleep(.5)
    clear()
    print("Loading...")
    time.sleep(.5)
    clear()

dicofwords1 = {
    'Toast':'1','Cheers':'1','Salute':'1','Tribute':'1',
    'Ring':'2','Match':'2','Bout':'2','Duel':'2',
    'Diamond':'3','Stud':'3','Hoop':'3','Drop':'3',
    'Chain':'4','Block':'4','Bar':'4','Gate':'4'
}
dicofwords2 = {
    'Pitch':'1','Note':'1','Tone':'1','Key':'1',
    'Bat':'2','Glove':'2','Base':'2','Diamond':'2',
    'Court':'3','Serve':'3','Volley':'3','Net':'3',
    'Deck':'4','Shuffle':'4','Deal':'4','Hand':'4'
}
dicofwords3 = {
    'Current':'1','Charge':'1','Field':'1','Force':'1',
    'Crown':'2','Scepter':'2','Throne':'2','Orb':'2',
    'Palm':'3','Pine':'3','Cedar':'3','Oak':'3',
    'Scale':'4','Chord':'4','Note':'4','Clef':'4'
}

def clear():
    os.system("clear")
def connections():
    print("Connections:")
    listofwords = []

    choice = random.choice(range(1,3))
    #used ai to assist below with printing format
    if choice == 3:
        listofwords.clear()
        words = list(dicofwords3.keys())
        random.shuffle(words)
        for i in range(4):
            print("  ".join(f"{words[i*4+j]:<12}" for j in range(4)))
        for key in dicofwords3:
            count = 0
            while count < 4:
                guess = input("Enter the Connected words: \n>> ")
                listofwords.append(guess)
                count += 1
            for words in listofwords:
                if listofwords[count2 + 1] == dicofwords3[key]:
                    print("Correct")
                else:
                    print("Incorrect")
    if choice == 2:
        count2 = -1
        listofwords.clear()
        words = list(dicofwords2.keys())
        random.shuffle(words)
        for i in range(4):
            print("  ".join(f"{words[i*4+j]:<12}" for j in range(4)))
        for key in dicofwords2:
            count = 0
            while count < 4:
                guess = input("Enter the Connected words: \n>> ")
                listofwords.append(guess)
                count += 1
            for words in listofwords:
                if listofwords[count2 + 1] == dicofwords2[key]:
                    print("Correct")
                else:
                    print("Incorrect")
    if choice == 1:
        count2 = -1
        listofwords.clear()
        words = list(dicofwords1.keys())
        random.shuffle(words)
        for i in range(4):
            print("  ".join(f"{words[i*4+j]:<12}" for j in range(4)))
        for key in dicofwords1:
            count = 0
            while count < 4:
                guess = input("Enter the Connected words: \n>> ")
                listofwords.append(guess)
                count += 1
            for words in listofwords:
                if listofwords[count2 + 1] == dicofwords1[key]:
                    print("Correct")
                else:
                    print("Incorrect")

def lobby():
    clear()
    print("Welcome to Connections")
    time.sleep(1.5)
    print("Instructions: \n1. In order to clear a level, you must group the words that share the same topic\n2. If a player enters an incorrect group of words four times, the game ends\n3. ")
    time.sleep(2)
    begin = input("If you would like to begin, enter B; if you would like to return to menu, enter M\n>> ").lower()
    if begin == "b":
        loading()
        connections()
    elif begin == "m":
        loading()
    else:
        clear()
        print("Invalid Input; Returning to menu")
        time.sleep(2)
        lobby()
lobby()




