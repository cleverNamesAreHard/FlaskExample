import mysql.connector


def test():
    host = "0.0.0.0"
    user = "root"
    database = "mlb_players"
    password = "X57e85e78*"

    db_conn = mysql.connector.connect(
        host = host,
        database = database,
        user = user,
        password = password
    )

test()
