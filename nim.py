#! /usr/bin/env python3


def afficher_jeu(nombre_allumettes):                 #Matthias 
    """Affiche le plateau du jeu.

    :param nombre_allumettes: doit être positif ou nul.
    :type nombre_allumettes: int.
    """
    def afficher_jeu(nombre_allumettes):                 #Matthias 
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
    if gagnant_dernier:
        return nombre_allumettes %4
    else:
        if ((nombre_allumettes %4) == 0) | ((nombre_allumettes %4) == 1):
            return 1
        else:
            return nombre_allumettes %4-1
for x in range(1, 15):
  print(x, "allumettes",prise_ia(x,False))


def partie(nombre_allumettes, gagnant_dernier, ia_joueur_2):                #Gaëtan
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
    # À implémenter.
  
      nombre_allumettes = reponses_entier(question, vmin, vmax)
    gagnant_dernier = int(input("Celui qui prends la dernière allumette est la gagnant?"))
    for i in enumerate:
        if "Oui" in gagnant_dernier:
            print("Question suivante")
        else:
            int(input("Celui qui prends la dernière allumette est la gagnant?"))
    ia_joueur2 = int(input("Le joueur 2 est la machine ?")) 
    for a in enumerate:
            if "True" in ia_joueur2:
                jouer()
            else:
                 afficher_message_fin()

def afficher_message_bienvenue():
    """Affiche le message de bienvenue."""
    # À implémenter.
      print("Bienvenue.")


def afficher_message_fin():
    """Affiche le message de fin."""
    # À implémenter.
   print("Fin de partie.")


def reponse_oui_non(question):                                            #Albert
    """Pose une question binaire (oui/non) à l'utilisateur qui répond
    soit 'o', soit 'n' (éventuellement 'O' ou 'N').
    La question est reposée tant que la réponse n'est pas comprise.

    :param question: la question à poser.
    :type question: str.
    :returns: la réponse sous forme de booléen.
    :rtype: bool.
    """
    # À implémenter.
  

def reponse_entier(question, vmin, vmax):                               #Gaëtan   #Albert
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
    # À implémenter.
  
    vmin >= 0
    vmax >= vmin 
    question = str(input("Entrez un nombre compris entre",vmin,"et",vmax))
    return reponse_entier


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
