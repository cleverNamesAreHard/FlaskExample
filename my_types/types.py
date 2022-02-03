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
        cols = "(name, height, weight, age,position, team_id)"
        sql = f"INSERT INTO players {cols} VALUES (%s,%d,%d,%f,%s,%d)"
        for player in players:
            cursor.execute(sql, (player.name, player.height, player.weight,
                player.age, player.position, player.team_id))
        db_conn.commit()
        print(mycursor.rowcount, "records inserted.")


class Team():
    def __init__(self, name):
        self.name = name

    def load_teams(teams, db_conn):
        cursor = db_conn.cursor()
        sql = "INSERT IGNORE INTO teams (name) VALUES (%s)"
        for team in teams:
            cursor.execute(sql, (team.name))
        db_conn.commit()
        print(mycursor.rowcount, "records inserted.")

    def get_teams():
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
