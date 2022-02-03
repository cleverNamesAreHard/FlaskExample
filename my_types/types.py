class Player():
    def __init__(self, name, height, weight, age, position, team_name):
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age
        self.position = position
        self.team_id = 0
        self.team_name = team_name

    def set_team_id(self, team_id):
        self.team_id = team_id

    def load_players(players, db_conn):
        cursor = db_conn.cursor()
        cols = "(name, height, weight, age, position, team_id)"
        sql = f"INSERT INTO players {cols} VALUES (%s,%s,%s,%s,%s,%s)"
        for player in players:
            cursor.execute(sql, (player.name, player.height, player.weight, player.age, player.position, player.team_id))
        db_conn.commit()
        print(cursor.rowcount, "records inserted.")

    def get_players(db_conn):
        cursor = db_conn.cursor()
        sql = "SELECT DISTINCT id, name FROM players"
        players = {}
        cursor.execute(sql)
        for row in cursor:
            id_ = row[0]
            name = row[1]
            players[id_] = name
        return players

    def get_player(db_conn, player_id):
        cursor = db_conn.cursor()
        cols = "name, weight, height, age, position"
        sql = f"SELECT DISTINCT {cols} FROM players WHERE id={player_id}"
        cursor.execute(sql)
        row = cursor.fetchone()
        name = row[0]
        weight = row[1]
        height = row[2]
        age = row[3]
        position = row[4]
        player = Player(name, height, weight, age, position, "")
        return player



class Team():
    def __init__(self, name):
        self.name = name

    def load_teams(teams, db_conn):
        cursor = db_conn.cursor()
        sql = "INSERT IGNORE INTO teams (name) VALUES (%s)"
        for team in teams:
            cursor.execute(sql, (team.name,))
        db_conn.commit()
        print(cursor.rowcount, "records inserted.")

    def get_teams(db_conn):
        cursor = db_conn.cursor()
        sql = "SELECT DISTINCT id, name FROM teams"
        teams = {}
        cursor.execute(sql)
        for row in cursor:
            name = row[1]
            if name not in teams:
                teams[name] = row[0]
        return teams

class Game():
    def __init__(self, game_date, player_id, runs):
        self.game_date = game_date
        self.player_id = player_id
        self.runs = runs
