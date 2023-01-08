CREATE DATABASE poker; 
USE poker;

CREATE TABLE players (
	player_id INTEGER PRIMARY KEY, 
    name TEXT NOT NULL, 
    chip_count INTEGER NOT NULL
); 

CREATE TABLE hand_history (
	hand_id INTEGER PRIMARY KEY, 
    game_id INTEGER NOT NULL,
    hand_number INTEGER NOT NULL,  
    hole_cards TEXT NOT NULL, 
    flop TEXT, 
    turn TEXT, 
    river TEXT, 
    final_hand TEXT NOT NULL, 
    bet_sizing TEXT NOT NULL,
    player_id INTEGER NOT NULL, 
	FOREIGN KEY (player_id) REFERENCES players (player_id)
); 

