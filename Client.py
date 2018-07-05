#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dbConnexion import *


# Add from - where (by client)
# num, identite_complete, personne(avec), dest, coming_from, add a bar
# ajouter plaintes dans la db
# personnel resto - hotel

def ajouter_client(nom, postnom, prenom, email, tel, nationalite, profession, sexe):
    r = True
    cnx = db_connect()
    cursor = cnx.cursor()
    try:
        cursor.execute("""
        INSERT INTO client(Nom_client, PostNom_client, Prenom_client, Email_client, Tel_client, Nationalite_client,
        Profession_client, Sexe_client) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)""",
                       (nom, postnom, prenom, email, tel, nationalite, profession, sexe))
        cnx.commit()
    except Exception as e:
        cnx.rollback()
        print(e)
        r = False
    finally:
        return r


def recup_client_par_id(id_client):
    cnx = db_connect()
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM client WHERE Id=%s" % id_client)
    client = cursor.fetchone()
    cnx.commit()
    return client


def recup_client_par_nom(nom):
    cnx = db_connect()
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM client WHERE Nom_client LIKE '%{}%'".format(nom))
    client = cursor.fetchall()
    cnx.commit()
    return client


def recup_client_par_nom_complet(nom, postnom, prenom):
    cnx = db_connect()
    cursor = cnx.cursor()
    cursor.execute("""
    SELECT * FROM client WHERE Nom_client LIKE '%{}%' AND 
    Postnom_client LIKE '%{}%' AND Prenom_client LIKE '%{}%'""".format(nom, postnom, prenom))
    client = cursor.fetchone()
    cnx.commit()
    return client


def modifier_client(id_client, client_new):
    client = recup_client_par_id(id_client)
    cnx = db_connect()  # Ceci est la syntaxe connection avc la BDD
    cursor = cnx.cursor()
    cursor.execute("""
    UPDATE client SET  Nom_client=%s, PostNom_client=%s, Prenom_client=%s, Email_client=%s,
    Tel_client=%s, Nationalite_client=%s, Profession_client=%s, Sexe_client=%s WHERE client.Id = %s""", (
        client_new[1], client_new[2], client_new[3], client_new[4], client_new[5], client_new[6], client_new[7],
        client_new[8], client[0]))
    cnx.commit()
    return client


def affichage_client():
    cnx = db_connect()  # Ceci est la syntaxe connection avc la BDD
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM client")
    client = cursor.fetchall()
    cnx.commit()
    return client


def client_profession(profession):
    cnx = db_connect()  # Ceci est la syntaxe connection avc la BDD
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM client WHERE Profession_client = %s" % profession)
    client = cursor.fetchall()
    cnx.commit()
    return client


def client_nationalite(nationalite):
    cnx = db_connect()  # Ceci est la syntaxe connection avc la BDD
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM client WHERE Nationalite_client = %s" % nationalite)
    client = cursor.fetchall()
    cnx.commit()
    return client
