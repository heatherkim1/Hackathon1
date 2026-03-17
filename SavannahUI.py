
main_menu = input("Welcome to our Hackathon project. What would you like to do?(View games, View records, or View game history. Note: please type as you see here.) ")
if main_menu == 'View games':
    print("Connections: ")
    print("Wordle: ")
    print("Bloons: ")
    print("Tic-Tac-Toe: ")
    play_game = input('Which game would you like to play? (If you would like to return to the main menu type: Main menu)')
if main_menu == 'View records':
    which_rec = input('Which game would you like to see the records for? (Bloons, Wordle, Connections, Tic-Tac-Toe)')
    if which_rec == 'Wordle':
        with open('WordlePlayLogs.txt','r') as log:
            log_read = log.read()
            print(log_read)
    if which_rec == 'Tic-Tac-Toe':
        with open('')
       
if main_menu == 'View game history':
    which_his = input('Would you like to view full history or single game history? (If you would like to view a single game please type the games name and history after.)')
    if which_his == 'full history':
        with open('FullHistory.txt','r') as full_his:
            his_read = full_his.read()
            print(his_read)
            