
main_menu = input("Welcome to our Hackathon project. What would you like to do?(View games, View records, or View game history logs. Note: please type as you see here.)")
if main_menu == 'View games':
    print("Connections: Connections is a popular daily word-grouping puzzle created by The New York Times in 2023. Players are given a grid of 16 words and must organize them into four groups of four that share a common, hidden theme.")
    print("Wordle: Wordle is a popular daily online word game where players have six attempts to guess a secret five-letter word. After each guess, the letter tiles change color to show if they are correct (green), in the wrong place (yellow), or not in the word at all (gray). ")
    print('Bloons: Bloons is a popular, long-running tower defense series by Ninja Kiwi where players place monkey towers along a path to pop incoming waves of colorful "bloons." The goal is to stop them from reaching the end using strategic tower placement, upgrades, hero abilities, and diverse monkey types to counter special bloon types.')
    print("Tic-Tac-Toe: Tic-tac-toe is a classic two-player strategy game played on a 3x3 grid, where players alternate marking cells with 'X' or 'O'. The objective is to be the first to align three of their marks horizontally, vertically, or diagonally.")
    play_game = input('Which game would you like to play?')

if main_menu == 'View records':
    which_rec = input('Which game would you like to see the records for? (Bloons, Wordle, Connections, Tic-Tac-Toe)')
    if which_rec == 'Wordle':
        with open('WordlePlayLogs.txt','r') as log:
            log_read = log.read()
            print(log_read)
    if which_rec == 'Tic-Tac-Toe':
        with open('XORecords.txt','r') as rec:
            rec_read = rec.read()
            print(rec_read)
    if which_rec == 'Bloons':
        with open('BloonsRecords.txt','r') as rec:
            rec_read = rec.read()
            print(rec_read)
    if which_rec == 'Connections':
        with open ('ConnectionsRecords.txt') as rec:
            rec_read = rec.read()
            print(rec_read)

if main_menu == 'View game history':
    which_his = input('Would you like to view full history or single game history? (If you would like to view a single game please type the games name and history after.)')
    if which_his == 'Full history':
        with open('FullHistory.txt','r') as full_his:
            his_read = full_his.read()
            print(his_read)
    if which_his == 'Bloons history':   
        with open('BloonsHistory.txt','r') as bloons_his:
            read_his = bloons_his.read()
            print(read_his)
    if which_his == 'Wordle history':
        with open('WordleHistory.txt','r') as wordle_his:
            read_his = wordle_his.read()
            print(read_his)
    if which_his == 'Connections history':
        with open('ConnectionsHistory.txt','r') as connections_his:
            read_his = connections_his.read()
            print(read_his)
    if which_his == 'Tic-Tac-Toe history':
        with open('XOHistory.txt','r') as xo_his:
            read_his = xo_his.read()
            print(read_his)


