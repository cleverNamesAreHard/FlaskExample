import mysql.connector


host = "0.0.0.0"
user = "root"
database = "mlb_players"
password = ""
with open("secret.txt", "r") as f_in:
    password = f_in.read().split("\n")[0]
db_conn = mysql.connector.connect(
    host = host,
    user = user,
    password = password,
    database = database
)


# How many players are there?
# SELECT COUNT(id) FROM players
def question_1(db_conn):
    cursor = db_conn.cursor()
    sql = "SELECT COUNT(id) FROM players"
    cursor.execute(sql)
    row = cursor.fetchone()
    return row[0]

# Select players whose names start with 'Jo'
# SELECT name FROM players WHERE name LIKE('Jo%');
def question_2(db_conn):
    cursor = db_conn.cursor()
    sql = "SELECT name FROM players WHERE name LIKE('Jo%')"
    players = []
    cursor.execute(sql)
    for row in cursor.fetchall()
        players.append(row[0])
    return players

# Select players who played this month
'''
SELECT 
    p.name 
FROM 
    players AS p
LEFT JOIN 
    games AS g 
ON
  g.player_id = p.id
WHERE 
    YEAR(g.game_date) = YEAR(NOW()) AND
    MONTH(g.game_date) = MONTH(NOW());
'''
def question_3(db_conn):
    cursor = db_conn.cursor()
    sql = "SELECT p.name FROM players AS p LEFT JOIN games AS g ON g.player_id = p.id" +
        "WHERE YEAR(g.game_date) = YEAR(NOW()) AND MONTH(g.game_date) = MONTH(NOW());"z
    players = []
    cursor.execute(sql)
    for row in cursor.fetchall()
        players.append(row[0])
    return players

# Select the number of each players for each position
# SELECT DISTINCT position, COUNT(id) FROM players GROUP BY position;
def question_4(db_conn):
    cursor = db_conn.cursor()
    sql = "SELECT DISTINCT position, COUNT(id) FROM players GROUP BY position"
    positions = {}
    cursor.execute(sql)
    for row in cursor.fetchall()
        position = row[0]
        players = row[1]
        positions[position] = players
    return positions

# Select the names of all players with 'Catcher' position
# SELECT DISTINCT name FROM players WHERE position = 'Catcher';
def question_5(db_conn):
    cursor = db_conn.cursor()
    sql = "SELECT DISTINCT name FROM players WHERE position = 'Catcher'"
    players = []
    cursor.execute(sql)
    for row in cursor.fetchall()
        players.append(row[0])
    return players

print("How many players are there?")
print(question_1(db_conn))
print("\nSelect players whose names start with 'Jo'")
for player in question_2(db_conn):
    print(player)
print("\nSelect players who played this month")
for player in question_3(db_conn):
    print(player)
print("\nSelect the number of each players for each position")
q4 = question_4(db_conn)
print("Position,Players")
for position in q4:
    print(position, q4[position])
print("\nSelect the names of all players with 'Catcher' position")
for player in question_5(db_conn):
    print(player)
