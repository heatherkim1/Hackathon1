import csv
with open('all_records.csv','w',newline='') as rec:
    writer = csv.writer(rec)
    headers = ['Computer wins','User wins','Ties']
    writer.writerow(headers)
with open('all_history.csv','w',newline='') as his:
    writer = csv.writer(his)
    headers = ['Game Played','Score','Winner']
    writer.writerow(headers)
with open('xo_records.csv','w',newline='') as rec:
    writer = csv.writer(rec)
    headers = ['Computer wins','User wins','Ties']
    writer.writerow(headers)
with open('bloons_records.csv','w',newline='') as rec:
    writer = csv.writer(rec)
    headers = ['Computer wins','User wins','Ties']
    writer.writerow(headers)
with open('connections_records.csv','w',newline='') as rec:
    writer = csv.writer(rec)
    headers = ['User wins','User losses']
    writer.writerow(headers)
with open('wordle_records.csv','w',newline='') as rec:
    writer = csv.writer(rec)
    headers = ['User wins','User losses']
    writer.writerow(headers)
with open('xo_history.csv','w',newline='') as his:
    writer = csv.writer(his)
    headers = ['Score','Winner']
    writer.writerow(headers)
with open('bloons_history.csv','w',newline='') as his:
    writer = csv.writer(his)
    headers = ['Score','Winner']
    writer.writerow(headers)
with open('connections_hisory.csv','w',newline='') as his:
    writer = csv.writer(his)
    headers = ['Score','Winner']
    writer.writerow(headers)
with open('wordle_history.csv','w',newline='') as his:
    writer = csv.writer(his)
    headers = ['Score','Winner']
    writer.writerow(headers)
main_menu = input("Welcome to our Hackathon project. What would you like to do?(View games, View records, or View game history. Note: please type as you see here.) ")
if main_menu == 'View games':
    print("Connections: ")
    print("Wordle: ")
    print("Bloons: ")
    print("Tic-Tac-Toe: ")
    print(":")
if main_menu == 'View records':
    choose_log = input('Would you like to see the complete records or single game records?')
    if choose_log == 'complete history':
        with open('all_records.csv','r') as rec:
            csv_reader = csv.reader(rec,delimiter=',')
            for row in csv_reader:
                print(row)
    elif choose_log == 'single game records':
        game_log = input('Which game do you want to see the records for?(Bloons, Connections, Wordle, Tic-Tac-Toe)')
        if game_log == 'Bloons':
            with open('bloons_records.csv','r') as rec:
                csv_reader = csv.reader(rec,delimiter=',')
                for row in csv_reader:
                    print(row)
        if game_log == 'Connections':
            with open('connections_records.csv','r') as rec:
                csv_reader = csv.reader(rec,delimiter=',')
                for row in csv_reader:
                    print(row)
        if game_log == 'Wordle':
            with open('wordle_records.csv','r') as rec:
                csv_reader = csv.reader(rec,delimiter=',')
                for row in csv_reader:
                    print(row)
        if game_log == 'Tic-Tac-Toe':
            with open('xo_records','r') as rec:
                csv_reader = csv.reader(rec,delimiter=',')
                for row in csv_reader:
                    print(row)
if main_menu == 'View game history':
    with open('xo_history.csv','r') as his:
