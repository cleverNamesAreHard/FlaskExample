import mysql.connector


def test():
    host = "0.0.0.0"
    user = "pythonUser"
    database = "mlb_players"
    password = ""
    with open("secret.txt", "r") as f_in:
        password = f_in.read().split("\n")[0]

    db_conn = mysql.connector.connect(
        host = host,
        database = database,
        user = user,
        password = password
    )

test()
