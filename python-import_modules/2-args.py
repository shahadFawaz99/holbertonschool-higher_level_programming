#!/usr/bin/python3

if __name__ == "__main__":
    # Importe sys pour accéder aux arguments de la ligne de commande
    import sys

    if len(sys.argv) == 1:
        print("0 arguments.")  # Affiche 0 si aucun argument n'est passé

    elif len(sys.argv) == 2:
        # Affiche "1 argument:" si un seul argument est passé
        # en soustrayant 1 car on ne compte pas le nom du script lui-même
        print("{} argument:".format(len(sys.argv) - 1))
        for i in range(1, len(sys.argv)):
            # La boucle for commence à 1 car on saute sys.argv[0](nom script)
            # On parcourt tous les arguments donnés par l'utilisateur
            # À chaque itération, i est l'index de l'argument
            # sys.argv[i] est la valeur de l'argument à cet index
            print("{}: {}".format(i, sys.argv[i]))

    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
