import requests


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
    pass

def select_player():
    pass

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