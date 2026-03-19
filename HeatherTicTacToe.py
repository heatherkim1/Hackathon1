# Heather Kim
# Tic Tac Toe
# Period 6
# duration



import time, random

def tictactoe ():
    global gameplayed, xorecords
    
    xorecords = open("XORecords.txt", "a")
    xorecords.close
    
    print("Welcome to Tic Tac Toe! You will be playing against a computer whose choices are completely randomized.")
    play_tictactoe = True
    while True:
        resetgame()
        round()
        if play_tictactoe == False: 
            break

def round(): 
    print("Welcome to a new round!")
    user_turn()
    determine_winner()
    computer_turn()
    determine_winner()

def resetgame():
    global user_move, available_moves,r1c1,r1c2,r1c3,r2c1,r2c2,r2c3,r3c1,r3c2,r3c3,play_tictactoe,winner, gameplayed
    
    gameplayed += 1
    r1c1 = '[ ]'
    r1c2 = '[ ]'
    r1c3 = '[ ]'
    r2c1 = '[ ]'
    r2c2 = '[ ]'
    r2c3 = '[ ]'
    r3c1 = '[ ]'
    r3c2 = '[ ]'
    r3c3 = '[ ]'

    print(f'{r1c1}{r1c2}{r1c3}\n{r2c1}{r2c2}{r2c3}\n{r3c1}{r3c2}{r3c3}')
    
    available_moves = ['r1c1','r1c2','r1c3','r2c1','r2c2','r2c3','r3c1','r3c2','r3c3']

    winner = None

def user_turn():
    global user_move, available_moves,r1c1,r1c2,r1c3,r2c1,r2c2,r2c3,r3c1,r3c2,r3c3,play_tictactoe,winner
    user_move = input("Choose a square (eg. r1c1, r1c2, r1c3): ")

    while user_move not in available_moves: 
        user_move = input("Invalid input or square already take, try again: ")

    if user_move == 'r1c1': r1c1 = '[O]'
    elif user_move == 'r1c2': r1c2 = '[O]'
    elif user_move == 'r1c3': r1c3 = '[O]'
    elif user_move == 'r2c1': r2c1 = '[O]'
    elif user_move == 'r2c2': r2c2 = '[O]'
    elif user_move == 'r2c3': r2c3 = '[O]'
    elif user_move == 'r3c1': r3c1 = '[O]'
    elif user_move == 'r3c2': r3c2 = '[O]'
    elif user_move == 'r3c3': r3c3 = '[O]'

    available_moves.remove(user_move)

    print(f'{r1c1}{r1c2}{r1c3}\n{r2c1}{r2c2}{r2c3}\n{r3c1}{r3c2}{r3c3}')


def computer_turn():
    global computer_moves,user_move, available_moves,r1c1,r1c2,r1c3,r2c1,r2c2,r2c3,r3c1,r3c2,r3c3,play_tictactoe,winner
    print("Computer's turn")
    time.sleep(1)
    computer_moves = random.choice(available_moves)
    if computer_moves == 'r1c1': r1c1 = '[X]'
    elif computer_moves == 'r1c2': r1c2 = '[X]'
    elif computer_moves == 'r1c3': r1c3 = '[X]'
    elif computer_moves == 'r2c1': r2c1 = '[X]'
    elif computer_moves == 'r2c2': r2c2 = '[X]'
    elif computer_moves == 'r2c3': r2c3 = '[X]'
    elif computer_moves == 'r3c1': r3c1 = '[X]'
    elif computer_moves == 'r3c2': r3c2 = '[X]'
    elif computer_moves == 'r3c3': r3c3 = '[X]'

    available_moves.remove(computer_moves)
    print(f'{r1c1}{r1c2}{r1c3}\n{r2c1}{r2c2}{r2c3}\n{r3c1}{r3c2}{r3c3}')

def determine_winner():
    global computer_moves,user_move, available_moves,r1c1,r1c2,r1c3,r2c1,r2c2,r2c3,r3c1,r3c2,r3c3,play_tictactoe,winner, gameplayed, xorecords
    if r1c1 == "[O]" and r1c2 == "[O]" and r1c3 == "[O]": # Top row
        winner = "User"
    elif r1c1 == "[X]" and r1c2 == "[X]" and r1c3 == "[X]":
        winner = "Computer"
    
    elif r2c1 == "[O]" and r2c2 == "[O]" and r2c3 == "[O]": # Second row
        winner = "User"
    elif r2c1 == "[X]" and r2c2 == "[X]" and r2c3 == "[X]":
        winner = "Computer"

    elif r3c1 == "[O]" and r3c2 == "[O]" and r3c3 == "[O]": # Third row
        winner = "User"
    elif r3c1 == "[X]" and r3c2 == "[X]" and r3c3 == "[X]":
        winner = "Computer"

    elif r1c1 == "[O]" and r2c1 == "[O]" and r3c1 == "[O]": # First column 
        winner = "User"
    elif r1c1 == "[X]" and r2c1 == "[X]" and r3c1 == "[X]":
        winner = "Computer"

    elif r1c2 == "[O]" and r2c2 == "[O]" and r3c2 == "[O]": # Second column 
        winner = "User"
    elif r1c2 == "[X]" and r2c2 == "[X]" and r3c2 == "[X]":
        winner = "Computer"

    elif r1c3 == "[O]" and r2c3 == "[O]" and r3c3 == "[O]": # Third column 
        winner = "User"
    elif r1c3 == "[X]" and r2c3 == "[X]" and r3c3 == "[X]":
        winner = "Computer"

    elif r1c1 == "[O]" and r2c2 == "[O]" and r3c3 == "[O]": # First diagonal
        winner = "User"
    elif r1c1 == "[X]" and r2c2 == "[X]" and r3c3 == "[X]":
        winner = "Computer"

    elif r3c1 == "[O]" and r2c2 == "[O]" and r1c3 == "[O]": # Second diagonal
        winner = "User"
    elif r3c1 == "[X]" and r2c2 == "[X]" and r1c3 == "[X]":
        winner = "Computer"

    if winner == "User" or winner == "Computer":
        print(f"\n**********{winner} won!**********")
        xorecords = open("XORecords.txt", "a")
        
        xorecords.write(f"Game #: {gameplayed}\n Winner: {winner}")

        xorecords.close
       
        return
    if available_moves == [] and winner == None:
        winner = "Tie"
        print(f"\n**********It's a tie!**********")
        xorecords = open("XORecords.txt", "a")
        
        xorecords.write(f"Game #: {gameplayed}\n Winner: {winner}")

        xorecords.close

        return

gameplayed = 0
tictactoe()