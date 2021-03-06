from dbConnexion import *


def ajouter_chambre(id_type, nom_chambre, details):
    cnx = db_connect()
    cursor = cnx.cursor()
    cursor.execute("""INSERT INTO chambre(Id_type, nom_chambre, details) VALUES(%s, %s, %s)""",
                   (id_type, nom_chambre,  details))
    cnx.commit()


def afficher_chambre():
    cnx = db_connect()
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM chambre")
    chambres = cursor.fetchall()
    cnx.commit()
    return chambres


def chambre_dispo():
    cnx = db_connect()
    cursor = cnx.cursor()
    cursor.execute("SELECT c.*, t.Prix_unitaire FROM chambre As c, type as t WHERE c.Disponibilite = 1 AND t.Id = c.Id_type")
    chambres = cursor.fetchall()
    cnx.commit()
    return chambres


def chambre_type():
    cnx = db_connect()
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM chambre, type WHERE type.Id = chambre.Id_type ORDER BY Id_type")
    chambres = cursor.fetchall()
    cnx.commit()
    return chambres


def chambre_by_type(id_type):
    cnx = db_connect()
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM chambre WHERE Id_type=%s" % id_type)
    chambres = cursor.fetchall()
    cnx.commit()
    return chambres


def ajouter_reservation(id_client, id_chambre, check_in, check_out, prix, details="details"):
    cnx = db_connect()
    cursor = cnx.cursor()
    cursor.execute("""INSERT INTO reservation(Id_client, Id_chambre, Check_in, Check_out, Prix, Details)
    VALUES (%s, %s, %s, %s, %s, %s)""", (id_client, id_chambre, check_in, check_out, prix, details))
    cnx.commit()


def ajouter_type(pu, nom, details, nb):
    cnx = db_connect()
    cursor = cnx.cursor()
    cursor.execute("""INSERT INTO type(Prix_unitaire, Nom_type, Detail_type, Nb_perso) 
    VALUES(%s, %s, %s, %s)""", (pu, nom, details, nb))
    cnx.commit()


def afficher_type():
    cnx = db_connect()
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM type")
    types = cursor.fetchall()
    cnx.commit()
    return types


def indispo_chambre(id_chambre):
    cnx = db_connect()
    cursor = cnx.cursor()
    cursor.execute("UPDATE chambre SET Disponibilite=0 WHERE Id = %s", id_chambre)
    cnx.commit()


def dispo_chambre(id_chambre):
    cnx = db_connect()
    cursor = cnx.cursor()
    cursor.execute("UPDATE chambre SET Disponibilite=1 WHERE Id = %s", id_chambre)
    cnx.commit()


def prix_total():
    cnx = db_connect()
    cursor = cnx.cursor()
    cursor.execute("SELECT SUM(Prix) FROM reservation")
    stats = cursor.fetchone()
    cnx.commit()
    return stats


def total_type(id):
    cnx = db_connect()
    cursor = cnx.cursor()
    cursor.execute("SELECT SUM(t.Prix_unitaire) FROM type As t, chambre As c WHERE t.Id = %s AND c.Id_type = %s AND c.Disponibilite = 0" % (id, id))
    stats = cursor.fetchone()
    cnx.commit()
    return stats

print(total_type(3))
