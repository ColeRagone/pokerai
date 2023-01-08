import random
import mysql.connector
import image_recognition

# CONSTAINTS

deck = [
    'Ace of Spades', '2 of Spades', '3 of Spades',
    '4 of Spades', '5 of Spades', '6 of Spades',
    '7 of Spades', '8 of Spades', '9 of Spades',
    '10 of Spades', 'Jack of Spades', 'Queen of Spades',
    'King of Spades',
    'Ace of Hearts', '2 of Hearts', '3 of Hearts',
    '4 of Hearts', '5 of Hearts', '6 of Hearts',
    '7 of Hearts', '8 of Hearts', '9 of Hearts',
    '10 of Hearts', 'Jack of Hearts', 'Queen of Hearts',
    'King of Hearts',
    'Ace of Diamonds', '2 of Diamonds', '3 of Diamonds',
    '4 of Diamonds', '5 of Diamonds', '6 of Diamonds',
    '7 of Diamonds', '8 of Diamonds', '9 of Diamonds',
    '10 of Diamonds', 'Jack of Diamonds', 'Queen of Diamonds',
    'King of Diamonds',
    'Ace of Clubs', '2 of Clubs', '3 of Clubs',
    '4 of Clubs', '5 of Clubs', '6 of Clubs',
    '7 of Clubs', '8 of Clubs', '9 of Clubs',
    '10 of Clubs', 'Jack of Clubs', 'Queen of Clubs',
    'King of Clubs'
  ]

buyin = 20.00

# SQL CODE 

db = mysql.connector.connect(user='root', password='root', host='localhost', database='poker') 

cur = db.cursor()

queryInsert = "INSERT INTO players (player_id, name, chip_count) VALUES (%s, %s, %s)"

players = ['Cole', 'Max', 'Cory', 'Knowles']

for i in range(0, len(players)): 
    try: 
        data = (i, players[i], buyin)
        cur.execute(queryInsert, data) 
    except: 
        pass 

db.commit()


# Define the table size

playerNum = len(players)

# We need a function to run to start the game: 
# Restart any needed tables
# We want to keep players total hand history tables so that we can gather data on them

def startup():
    pass 

# Starting at the big blind, we need the establish the order of players playing
# We can come back to this

# Add a table for each player that is playing in the game

def initializingPlayer(playerID):
    tableName = players[playerID] 
    db = mysql.connector.connect(user='root', password='root', host='localhost', database='poker') 
    cur = db.cursor()
    queryInsert = "CREATE TABLE {}_info ( hand_history_id INTEGER PRIMARY KEY, chip_count INTEGER NOT NULL, card1 INTEGER NOT NULL, card2 INTEGER NOT NULL, hand_won BINARY NOT NULL )".format(tableName)
    cur.execute(queryInsert) 
    db.commit()

#for i in range(playerNum): 
    #initializingPlayer(i) 

# we are going to input data into the hand_history table
# we can then extract the data to each players information from there
# we need to record as much data as we can from a poker table

# can we get this information from using a camera? 
# or do we need to manually input the information

# Let's pretend that we have just played a hand...
# Let's open up the bets

# players are those that made some sort of poker move during the hand (ei NOT folding preflop without betting) 
# stack is the amount of chips at the start of the hand by each of these players
# showdown is a binary decision on whether or not the hand was won because of a showdown

# NOTE: we should have their stack, so I am not including it to start 


# SCENARIO: Max, Cole, Ned see a post flop, with Ned on the big blind, Max on the small blind, and Cole UTG
# Everyone limps in 


def getStacks(activePlayers): 
    chip_count_list = [] 
    for i in activePlayers: 
        cur_playerID = players.index(i) # this works
        db = mysql.connector.connect(user='root', password='root', host='localhost', database='poker') 
        cur = db.cursor()
        cur.execute('select chip_count from players where player_id = {}'.format(cur_playerID))
        for row in cur: 
            chip_count_list.append(row) 

    return chip_count_list 


# play a pretend hand
# Cole and Max are playing, little and big blind to make it easy
# what are hands? 

def pretendHand(players, hands, flop, turn, river): 
    pass 

pretendPlayers = ['Cole', 'Cory'] 
pretendHands = ['AsAc', 'QsQc']

def insertFlop(image): 
    pass 

def seeTurn(image): 
    pass 

# pass in a players name
def overallWinnings(player): 
    cur_playerID = players.index(i)
    db = mysql.connector.connect(user='root', password='root', host='localhost', database='poker') 
    cur = db.cursor()
    cur.execute('select chip_count from players where player_id = {}'.format(cur_playerID)) 



