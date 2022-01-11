#! /usr/bin/env python3


def afficher_jeu(nombre_allumettes):              
    """Affiche le plateau du jeu.

    :param nombre_allumettes: doit être positif ou nul.
    :type nombre_allumettes: int.
    """

    assert nombre_allumettes >=0, "nombre allumette inférieur à 0"
    if nombre_allumettes >=0 :
        print ("|"*nombre_allumettes)
 

def prise_ia(nombre_allumettes, gagnant_dernier):                #Matthias 
    """Implémentation de la statégie gagnante : donne le nombre
    d'allumettes à prendre en fonction de nombre restant et de la
    variante du jeu.

    :param nombre_allumettes: doit être positif ou nul.
    :type nombre_allumettes: int.
    :param gagnant_dernier: indique si celui qui prend la dernière
                            allumette est le gagnant.
    :type gagnant_dernier: bool.
    :returns: nombre d'allumettes à prendre.
    :rtype: int.
    """
  
  


def partie(nombre_allumettes, gagnant_dernier, ia_joueur_2):                #Gaëtan   #Albert
    """Une seule partie du jeu de Nim.

    :param nombre_allumettes: nombre d'allumettes au début de la partie,
                              doit être positif ou nul.
    :type nombre_allumettes: int.
    :param gagnant_dernier: indique si celui qui prend la dernière
                            allumette est le gagnant.
    :type gagnant_dernier: bool.
    :param ia_joueur_2: indique si le joueur 2 est la machine (True)
                  ou l'utilisateur (False).
    :type ia_joueur_2: bool.
    """

  afficher_message_bienvenue() 
gagnant_dernier = ("Le gagnant est celui qui prends la dernière allumette ?")
ia_joueur2 = ("Le joueur 2 est la machine?")
liste = ["O","o","N","n"] 
reponse = input(gagnant_dernier)
reponse2 = inût(ia_joueur2) 
while reponse not in liste:
    reponse = input(gagnant_dernier)
    if reponse == "Oui" or reponse == "oui":
        ia_joueur2 = int(input("Le joueur 2 est la machine ?"))
    else:
        reponse = input(gagnant_dernier)
while ia_joueur2 not in liste:
        ia_joueur2 = input(ia_joueur2)
    if reponse == "Oui" or reponse == "oui":
            jouer()
        else:
            afficher_message_fin()

def afficher_message_bienvenue():
    """Affiche le message de bienvenue."""
      print("Bienvenue.")


def afficher_message_fin():
    """Affiche le message de fin."""
   print("Fin de partie.")


def reponse_oui_non(question):                                           
    """Pose une question binaire (oui/non) à l'utilisateur qui répond
    soit 'o', soit 'n' (éventuellement 'O' ou 'N').
    La question est reposée tant que la réponse n'est pas comprise.

    :param question: la question à poser.
    :type question: str.
    :returns: la réponse sous forme de booléen.
    :rtype: bool.
    """
    liste = ["O,"o","N","n"]
    reponse = input(question)
    while reponse not in liste:
            reponse = input(question)
     if reponse == "O" or reponse == "o":
            return(True)
     else:
            return(False)

def reponse_entier(question, vmin, vmax):                               
    """Pose une question à l'utilisateur dont la réponse est un entier
    compris dans l'intervalle [vmin ; vmax]. vmin >= 0.
    La question est reposée tant que la réponse n'est pas correcte.

    :param question: la question à poser.
    :type question: str.
    :param vmin: la valeur minimale possible (>=0).
    :type vmin: int.
    :param vmax: la valeur maximale possible (>= vmin).
    :type vmax: int.
    :returns: l'entier choisi.
    :rtype: int.
    """
    assert vmin >= 0, "vmin inférieur à 0" 
    val = -1
    while not vmin<=val<=vmax:
        val = int(input(question))
    print("Vous prenez",val,"allumettes")
    return val    
reponse_entier("Combien voulez-vous retirer d'allumettes ?", 1, 100) 
  


def jouer():
    """Lance le jeu de Nim.
    On peut lancer autant d'instances du jeu que l'on souhaite.
    L'utilisateur a le choix de rejouer à chaque fin de partie.
    """
    afficher_message_bienvenue()

    while True:
        # paramètres de la partie
        ia = reponse_oui_non("Jouer contre la machine ?")
        gagnant_dernier = reponse_oui_non(
            "Le gagnant est celui qui prend la dernière allumette ?")
        nombre_allumettes = reponse_entier("Combien d'allumettes ?", 1, 100)
        # lancement de la partie
        partie(nombre_allumettes, gagnant_dernier, ia)
        # on rejoue ?
        if not reponse_oui_non("Rejouer ?"):
            break

    afficher_message_fin()


if __name__ == "__main__":
    # si le programme est exécuté directement, on lance une partie
    jouer()
