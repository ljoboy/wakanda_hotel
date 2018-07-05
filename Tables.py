from dbConnexion import *


def ajouter_table(nom_table, nbr_max, detail, dispo):
    cnx = db_connect()
    cursor = cnx.cursor()

    cursor.execute("""INSERT INTO tables(Nom_table, Nb_max, Details, Dispo) 
    VALUES(%s,%s,%s,%s)""" % (nom_table, nbr_max, detail, dispo))
    cnx.commit()


def restab(nom, postnom, prenom, email, tel, nationalite, profession, sexe_client):
    cnx = db_connect()
    cursor = cnx.cursor()
    cursor.execute("""INSERT INTO client
(Nom_client, PostNom_client, Prenom_client, Email_client, Tel_client, Nationalite_client, Profession_client, Sexe_client)
  VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""" % (nom, postnom, prenom, email, tel, nationalite, profession, sexe_client))
    cnx.commit()


def affichage_client():
    cnx = db_connect()
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM client")
    cnx.commit()


def check_in():
    cnx = db_connect()
    cursor = cnx.cursor()
    cursor.execute("INSERT INTO check_in(jour, heure)values(%s,%s)""",(jour, heure))
    cnx.commit()



def quantite():
    cnx=mysql.connector.connect(host="localhost", user='root', passwd="", db='new_wakanda')#Ceci est la syntaxe connection avc la BDD
    cursor=cnx.cursor()

    cursor.execute("INSERT INTO nb_perso(nombre)value(%s)""",(nombre))
    cnx.commit()

