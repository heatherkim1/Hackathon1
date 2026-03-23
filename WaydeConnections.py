import random, os, time
score = 0
wins = 0
loss = 0
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

ofwords = [
    {
        'Toast':'1','Cheers':'1','Salute':'1','Tribute':'1',
        'Ring':'2','Match':'2','Bout':'2','Duel':'2',
        'Diamond':'3','Stud':'3','Hoop':'3','Drop':'3',
        'Chain':'4','Block':'4','Bar':'4','Gate':'4'
    },
    {
        'Pitch':'1','Note':'1','Tone':'1','Key':'1',
        'Bat':'2','Glove':'2','Base':'2','Diamond':'2',
        'Court':'3','Serve':'3','Volley':'3','Net':'3',
        'Deck':'4','Shuffle':'4','Deal':'4','Hand':'4'
    },
    {
        'Current':'1','Charge':'1','Field':'1','Force':'1',
        'Crown':'2','Scepter':'2','Throne':'2','Orb':'2',
        'Palm':'3','Pine':'3','Cedar':'3','Oak':'3',
        'Scale':'4','Chord':'4','Note':'4','Clef':'4'
    }
]
def clear():
    os.system("clear")
def printing(words):
    for i in range(0, len(words), 4):
        print("  ".join(f"{word:<12}" for word in words[i:i+4]))

def connections():
    clear()
    choice = random.choice(ofwords)
    words = list(choice.keys())
    random.shuffle(words)
    matched = []
    failed = 0
    while len(matched) < 4 and failed < 4:
        clear()
        print("connections:")
        board = [word for word in words if word not in sum(matched, [])]
        printing(board)
        guess = input("Enter your guess, (seperate each word with commas)\n>> ").split(",")
        guess = [word.strip().title() for word in guess]

        if len(guess) != 4:
            print("You must enter 4 words!")
            print("Press Enter to try Again")
            input()
            
        if not all(word in board for word in guess):
            print("Invalid words entered!")
            print("Press Enter to try Again")
            input()
            
        group = [choice[word] for word in guess]
        if len(set(group)) == 1:
            print("Correct Group")
            score += 1
            matched.append(guess)
        else:
            failed += 1
            print("Incorrect Group; Remaining Attempts: ", 4 - failed)
        input("Press Enter to Continue\n")
    clear()
    if len(matched) == 4:
        print("4/4 Groups Found: You Win!")
        wins += 1
        print("Returning to Menu...")
        loading()
        lobby()
    else:
        print("Game Over: You did not find all groups!")
        loss += 1
        print("Returning to Menu...")
        loading()
        lobby()
def lobby():
    clear()
    print("Welcome to Connections")
    time.sleep(1.5)
    print("Instructions: \n1. In order to clear a level, you must group the words that share the same topic\n2. If a player enters an incorrect group of words four times, the game ends\n3.If all 4 rows are matched, the player wins ")
    time.sleep(2)
    begin = input("B: Begin, M: Menu, S: Stats\n>> ").lower()
    if begin == "b":
        loading()
        connections()
    elif begin == "m":
        loading()
    elif begin == "s":
        clear()
        print(f"Score: {score}\nWins: {wins}\nLosses: {loss}")
        input("Press Enter to Return to Menu\n")
        loading()
        lobby()
    else:
        clear()
        print("Invalid Input; Returning to menu")
        time.sleep(2)
        lobby()
lobby()




