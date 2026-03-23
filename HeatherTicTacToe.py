# Heather Kim 
# Period 6 
# Tic Tac Toe
# 150 minutes

import random, time
rec = open('XORecords.txt','a') # Creates the file that will be read by the UI

def resetgame():
    global user_move, available_moves,r1c1,r1c2,r1c3,r2c1,r2c2,r2c3,r3c1,r3c2,r3c3, winner, playtictactoe, gameplayed, rec
    r1c1 = '[ ]' # Clears all the variables to create a new board
    r1c2 = '[ ]'
    r1c3 = '[ ]'
    r2c1 = '[ ]'
    r2c2 = '[ ]'
    r2c3 = '[ ]'
    r3c1 = '[ ]'
    r3c2 = '[ ]'
    r3c3 = '[ ]'
    gameplayed += 1 # Increases the counter that tracks the number of times the game was played
    print(f'{r1c1}{r1c2}{r1c3}\n{r2c1}{r2c2}{r2c3}\n{r3c1}{r3c2}{r3c3}') # Prints the board
    playtictactoe = "None" # Sets the variable to none 

    available_moves = ['r1c1','r1c2','r1c3','r2c1','r2c2','r2c3','r3c1','r3c2','r3c3'] # The list of all the moves available to the players

def user_turn():
    global user_move, available_moves,r1c1,r1c2,r1c3,r2c1,r2c2,r2c3,r3c1,r3c2,r3c3, winner, playtictactoe
    user_move = input("Choose a square (eg. r1c1, r1c2, r1c3): ") # Asks the user to choose a square

    while user_move not in available_moves: # Continues to ask until the input is valid
        user_move = input("Invalid input or square already take, try again: ") 

    if user_move == 'r1c1': r1c1 = '[O]' # Places an "O" to the square the user chose
    elif user_move == 'r1c2': r1c2 = '[O]'
    elif user_move == 'r1c3': r1c3 = '[O]'
    elif user_move == 'r2c1': r2c1 = '[O]'
    elif user_move == 'r2c2': r2c2 = '[O]'
    elif user_move == 'r2c3': r2c3 = '[O]'
    elif user_move == 'r3c1': r3c1 = '[O]'
    elif user_move == 'r3c2': r3c2 = '[O]'
    elif user_move == 'r3c3': r3c3 = '[O]'

    available_moves.remove(user_move) # Removes the square as a choice


    print(f'{r1c1}{r1c2}{r1c3}\n{r2c1}{r2c2}{r2c3}\n{r3c1}{r3c2}{r3c3}') # Prints the updated board
    
def computer_turn():
    global user_move, available_moves,r1c1,r1c2,r1c3,r2c1,r2c2,r2c3,r3c1,r3c2,r3c3,winner,playtictactoe
    print("Computer's turn")
    time.sleep(2) # Dramatic pause
    computer_moves = random.choice(available_moves) # The computer randomly chooses a move from the available list of moves
    if computer_moves == 'r1c1': r1c1 = '[X]'
    elif computer_moves == 'r1c2': r1c2 = '[X]'
    elif computer_moves == 'r1c3': r1c3 = '[X]'
    elif computer_moves == 'r2c1': r2c1 = '[X]'
    elif computer_moves == 'r2c2': r2c2 = '[X]'
    elif computer_moves == 'r2c3': r2c3 = '[X]'
    elif computer_moves == 'r3c1': r3c1 = '[X]'
    elif computer_moves == 'r3c2': r3c2 = '[X]'
    elif computer_moves == 'r3c3': r3c3 = '[X]'

    available_moves.remove(computer_moves) # Removes the square as a choice
    print(f'{r1c1}{r1c2}{r1c3}\n{r2c1}{r2c2}{r2c3}\n{r3c1}{r3c2}{r3c3}') # Prints the updated board

def determine_winner():
    global winner, r1c1,r1c2,r1c3,r2c1,r2c2,r2c3,r3c1,r3c2,r3c3,winner, playtictactoe,gameplayed, rec
    if r1c1 == "[O]" and r1c2 == "[O]" and r1c3 == "[O]": # Checks if the first row is fully "O's"
        winner = "User" 
    elif r1c1 == "[X]" and r1c2 == "[X]" and r1c3 == "[X]": # Checks if the first row is fully "X's"
        winner = "Computer" 
    
    elif r2c1 == "[O]" and r2c2 == "[O]" and r2c3 == "[O]": # Checks if the second row is fully "O's
        winner = "User"
    elif r2c1 == "[X]" and r2c2 == "[X]" and r2c3 == "[X]": # Checks if the second row is fully "X's"
        winner = "Computer"

    elif r3c1 == "[O]" and r3c2 == "[O]" and r3c3 == "[O]": # Checks if the third row is fully "O's
        winner = "User"
    elif r3c1 == "[X]" and r3c2 == "[X]" and r3c3 == "[X]": # Checks if the third row is fully "X's"
        winner = "Computer"

    elif r1c1 == "[O]" and r2c1 == "[O]" and r3c1 == "[O]": # Checks if the first column is fully "O's"
        winner = "User"
    elif r1c1 == "[X]" and r2c1 == "[X]" and r3c1 == "[X]": # Checks if the first column is fully "X's"
        winner = "Computer"

    elif r1c2 == "[O]" and r2c2 == "[O]" and r3c2 == "[O]": # Checks if the second column is fully "O's"
        winner = "User"
    elif r1c2 == "[X]" and r2c2 == "[X]" and r3c2 == "[X]": # Checks if the second column is fully "X's"
        winner = "Computer"

    elif r1c3 == "[O]" and r2c3 == "[O]" and r3c3 == "[O]": # Checks if the third column is fully "O's"
        winner = "User"
    elif r1c3 == "[X]" and r2c3 == "[X]" and r3c3 == "[X]": # Checks if the third column is fully "X's"
        winner = "Computer"

    elif r1c1 == "[O]" and r2c2 == "[O]" and r3c3 == "[O]": # Checks if the first diagonal is fully "O's"
        winner = "User"
    elif r1c1 == "[X]" and r2c2 == "[X]" and r3c3 == "[X]": # Checks if the first diagonal is fully "X's"
        winner = "Computer"

    elif r3c1 == "[O]" and r2c2 == "[O]" and r1c3 == "[O]": # Checks if the second diagonal is fully "O's"
        winner = "User"
    elif r3c1 == "[X]" and r2c2 == "[X]" and r1c3 == "[X]": # Checks if the second diagonal is fully "X's"
        winner = "Computer"

    if winner == "User" or winner == "Computer": # Updates the records and ends the game if either the user or the computer won
        print(f"\n**********{winner} won!**********")
        with open('XORecords.txt','a') as rec, open('FullHistory.txt','a') as full_his:
            rec.write(f"Game #: {gameplayed}\n Winner: {winner}\n")
            full_his.write(f"Game: Tic Tac Toe\nGame #: {gameplayed}\nWinner: {winner}\n")

        
    if available_moves == [] and winner == None: # Updates the records and ends the game if there is a tie and no available moves
        print(f"\n**********It's a tie!**********")
        with open('XORecords.txt','a') as rec:
            rec.write(f"Game #: {gameplayed}\n Winner: {winner}\n")
            full_his.write(f"Game: Tic Tac Toe\nGame #: {gameplayed}\nWinner: {winner}\n")
       

def round():
    global winner, playtictactoe
    winner = None 
    playtictactoe = None
    resetgame() # Resets the rest of the variables
    while winner == None: 
        user_turn()
        determine_winner()
        if winner:
            while playtictactoe not in ["cont", "menu"]:
                playtictactoe = input("Enter 'cont' to play another round or 'menu' to go back to the home screen: ").strip().lower() # Asks the user if they would like to play again or return to the menu
                if playtictactoe == "menu": 
                    playtictactoe = None # Ends the loop 
                    return
                if playtictactoe == "cont": return # Repeats the game
        computer_turn()
        determine_winner()
        if winner:
            while playtictactoe not in ["cont", "menu"]:
                playtictactoe = input("Enter 'cont' to play another round or 'menu' to go back to the home screen: ").strip().lower() # Asks the user if they would like to play again or return to the menu 
                if playtictactoe == "menu": 
                    playtictactoe = None # Ends the loop 
                    return
                if playtictactoe == "cont": return # Repeats the game
        

gameplayed = 0
print("Welcome to Tic Tac Toe! You start first. ") # Welcome message
playtictactoe = "cont" # Loops the game until the user inputs that they would like to go to the menu
while playtictactoe == "cont":
    round()
    if playtictactoe == "menu":
        break