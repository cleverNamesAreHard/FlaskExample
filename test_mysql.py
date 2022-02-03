import mysql.connector


def test():
    host = "localhost"
    user = "pythonUser"
    database = "mlb_players"
    password = ""
    with open("secret.txt", "r") as f_in:
        password = f_in.read()
    print(password)
    db_conn = mysql.connector.connect(
        host = host,
        user = user,
        password = password,
        database = database
    )

test()
