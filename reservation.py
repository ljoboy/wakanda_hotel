from dbConnexion import db_connect

def recup_reservation():
    cnx = db_connect()
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM reservation")
    reservation = cursor.fetchall()
    cnx.commit()
    return reservation