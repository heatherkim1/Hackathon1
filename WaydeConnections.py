import random, os, time
score = 0
wins = 0
loss = 0
#all three set counts for loss win and score
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
#a shortcut for "animations" between calling defs
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
#three wordsets for the main game
def clear():
    os.system("clear")
#clears the screen, makes the game look cleaner
def printing(words):
    for i in range(0, len(words), 4):
        print("  ".join(f"{word:<12}" for word in words[i:i+4]))
#the printing format for connections, prints 4 words in 4 rows

def connections():
    clear()
    choice = random.choice(ofwords)
    words = list(choice.keys())
    random.shuffle(words)
    #selects one of the word sets in 'ofwords', and randomizes the order of the words
    matched = []
    #empty list used to gathered the correct matched words
    failed = 0
    #count that is updated when a player gets a row of words incorrect
    while len(matched) < 4 and failed < 4:
        clear()
        print("connections:")
        board = [word for word in words if word not in sum(matched, [])]
        printing(board)
        guess = input("Enter your guess, (seperate each word with commas)\n>> ").split(",")
        guess = [word.strip().title() for word in guess]
        #input for player; allows for the player to seperate each word with commas through .split(",")

        if len(guess) != 4:
            print("You must enter 4 words!")
            print("Press Enter to try Again")
            input()
            #causes the player to reenter if they do not enter 4 words initailly.
            
        if not all(word in board for word in guess):
            print("Invalid words entered!")
            print("Press Enter to try Again")
            input()
            #causes the player to reenter if inputted words are not in the given word set
            
        group = [choice[word] for word in guess]
        if len(set(group)) == 1:
            print("Correct Group")
            score += 1
            matched.append(guess)
        #checks if the inputted words are correct, if they are score is increased, and the inputed word is appended to the 'matched' list
        else:
            failed += 1
            print("Incorrect Group; Remaining Attempts: ", 4 - failed)
        #'failed' adds to the incorrect limit, and shows the user how much attempts there are left
        input("Press Enter to Continue\n")
    clear()
    if len(matched) == 4:
        print("4/4 Groups Found: You Win!")
        wins += 1
        #checks if there are 4 correct rows/answers, and increases the win count
        print("Returning to Menu...")
        loading()
        lobby()
        #sends player back to the menu with animation
    else:
        print("Game Over: You did not find all groups!")
        loss += 1
        #player loses, loss counter is increased
        print("Returning to Menu...")
        loading()
        lobby()
        #animation and lobby again
def lobby():
    clear()
    print("Welcome to Connections")
    time.sleep(1.5)
    print("Instructions: \n1. In order to clear a level, you must group the words that share the same topic\n2. If a player enters an incorrect group of words four times, the game ends\n3.If all 4 rows are matched, the player wins ")
    time.sleep(2)
    #displays rules and title, with timed intervals before printing
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
    #user choices through input, b begins game, m sends to main menu, s shows player wins,loss, and score
    else:
        clear()
        print("Invalid Input; Returning to menu")
        time.sleep(2)
        lobby()
    #if the user does not enter a valid input, they are sent again to enter a new input
lobby()




