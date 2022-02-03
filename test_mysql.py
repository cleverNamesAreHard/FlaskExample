import mysql.connector


def test():
    host = "localhost"
    user = "pythonUser"
    database = "mlb_players"
    password = "X57e85e78*"

    db_conn = mysql.connector.connect(
        host = host,
        user = user,
        password = password,
        database = database
    )

test()
