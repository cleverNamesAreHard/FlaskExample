import requests
import json
from my_types import Player


def load_csv():
    print("Please enter the name of a file to upload to the database")
    f_in = input("> ")
    files = {"file": open(f_in, "rb")}
    url = "http://localhost:5000/load_csv"
    req = requests.post(url, files=files)
    if req.status_code == 200:
        print("Successfully added the records!")
    else:
        print("There was an error while adding the records")

def list_players():
    url = "http://localhost:5000/list_players?ret=cli"
    req = requests.get(url)
    if req.status_code == 200:
        players = json.loads(req.text)
        print("ID  |  Name")
        for player in players:
            print(f"{player}  |  {players[player]}")
        print("Successfully got list of players!")
    else:
        print("There was an error while getting the player list")

def select_player():
    print("Please enter the ID of a player to look up")
    player_id = input("> ")
    url = f"http://localhost:5000/search_players?player_id={player_id}&ret=cli"
    req = requests.get(url)
    if req.status_code == 200:
        print("Name, Height, Weight, Age, Position")
        name = req.text.split(",")[0]
        height = req.text.split(",")[0]
        weight = req.text.split(",")[0]
        age = req.text.split(",")[0]
        position = req.text.split(",")[0]
        team_id = req.text.split(",")[0]
        print(name, height, weight, age, position)
        print("Successfully added the records!")
        print("\nWould you like to add a game to this player? [y/n]")
        new_game = False
        new_game_str = input("> ")
        if new_game_str == "y":
            print("Please enter a valid game date: ")
            game_date = input("> ")
            print("Please enter the number of runs for this player: ")
            runs = input("> ")
            player_id = 
            url = f"http://localhost:5000/search_players?player_id={team_id}&runs={runs}&ret=cli"
            req = requests.get(url)
            print(req.text)
    else:
        print("There was an error while adding the records")



print("[1] LOAD a file from csv to a table")
print("[2] LIST all players from the players table")
print("[3] SELECT a player, and add game results")

functions = {
    1: load_csv,
    2: list_players,
    3: select_player
}

num_in = 0
try:
    num_in = int(input("> "))
    if not num_in >= 1 and not num_in <= 3:
        raise ValueError("Please enter a valid number between 1 and 3")
except ValueError:
    print("Please enter a valid number between 1 and 3")
functions[num_in]()