import mysql.connector


def ajout_plat(Nom_art,Prix_art,Stock,Detail,Type_art):
    cnx=mysql.connector.connect(host="localhost", user='root', passwd="", db='new_wakanda')
    cursor=cnx.cursor()
    print("L'HOTEL WAKANDA VOUS OFFRE DES SERVICES DE RESTAURATOIN DE TOUT TYPE ")
    # Nom_art=input("Veuiller saisir le nom de l'article: ")
    # Prix_art=input("Inserer prix de l'artticle inscrit: ")
    # Stock=input("combien en avez vous en stock ?: ")
    # Detail=input("Donnez des détail sur l'articule: ")
    # Type_art=input("Dans quel type voulez-vous le(la) classé(e)?: ")
    cursor.execute("""INSERT INTO plats(Nom_art, Prix_art, Stock, Details, Type_art)VALUES(%s,%s,%s,%s,%s)""",(Nom_art, Prix_art, Stock, Detail, Type_art))
    cnx.commit()


def AffichagePlat():
    cnx = mysql.connector.connect(host="localhost", user='root', passwd="", db='new_wakanda')  # Ceci est la syntaxe connection avc la BDD
    cursor = cnx.cursor()

    cursor.execute("SELECT * FROM plats")
    plats = cursor.fetchall()
    for plat in plats:
        print(plat)
    cnx.commit()

def AffichageClientSelonLeTypeRestauration(Nom_art):
    cnx=mysql.connector.connect(host="localhost", user='root', passwd="", db='new_wakanda')#Ceci est la syntaxe connection avc la BDD
    cursor=cnx.cursor()
    #Nom_art=input("Veuillez inserer le nom de l'article du ou des client(s) à rechercher: ")
    cursor.execute("""SELECT * FROM plats WHERE Type_art LIKE '%s'""" % (Nom_art))
    plats=cursor.fetchall()
    return plats


def ajout_Type():
    cnx = mysql.connector.connect(host="localhost", user='root', passwd="", db='new_wakanda')
    cursor = cnx.cursor()
    Nom_type=input("Saisir le type de chambre: ")
    Prix_unitaire=input("Saisir le prix du type de chambre: ")
    Detail_type=input("Saisir des détails sur le chambre: ")
    Nb_perso=input("Saisir le nombre de personne permise dans la chambre au max: ")
    cursor.execute("""INSERT INTO type(Nom_type, Prix_unitaire, Detail_type, Nb_perso)VALUES(%s,%s,%s,%s)""",(Nom_type, Prix_unitaire, Detail_type, Nb_perso))
    cnx.commit()

def AffichageType():
    cnx = mysql.connector.connect(host="localhost", user='root', passwd="", db='new_wakanda')  # Ceci est la syntaxe connection avc la BDD
    cursor = cnx.cursor()

    cursor.execute("SELECT * FROM type")
    type = cursor.fetchall()
    for types in type :
        print(types)
    cnx.commit()


def AffichageClientSelonLeTypeDeChambre():
    cnx=mysql.connector.connect(host="localhost", user='root', passwd="", db='new_wakanda')#Ceci est la syntaxe connection avc la BDD
    cursor=cnx.cursor()
    Type_Chambre=input("Veuillez inserer le nom du type du ou des client(s) à rechercher: ")
    cursor.execute("""SELECT * FROM type WHERE Nom_type LIKE '%s'""" % (Type_Chambre))
    clients=cursor.fetchall()
    for client in clients:
        print(client)
     # return clients