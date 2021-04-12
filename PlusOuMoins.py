from random import randint

# Le jeu du plus ou moins

# version 1.0
# date 13 avril 2020

print("Jeu du + ou -")
utilisateur = input("Entrer votre nom : ")

nb_utilisateur = int ( input("Entrer votre nombre : ") )
nb_trouve = randint(1,100) # Génére un nombre entre 1 et 100
nb_essai = 0
etat = ""

while nb_utilisateur != nb_trouve:

    if nb_utilisateur > nb_trouve: 
        print("Non, C'est moins !")
    else: 
        print("Non, C'est plus !")

    nb_utilisateur = int ( input("Retentez : ") )
    nb_essai += 1

print("Bravo ! " + str(utilisateur) +  " Le numero etait : " + str(nb_trouve))

essai = "essai"
if nb_essai > 1: essai = "essais"

print("Nombre " + str(essai) + " " +  str(nb_essai))

print("Hello, World!")