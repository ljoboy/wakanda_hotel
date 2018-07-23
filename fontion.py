from Chambre import *

types = afficher_type()
for t in types:
    print(t[2])
    print(chambre_by_type(t[0]))