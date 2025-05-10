#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":

    # Récupère tous les noms définis dans le module hidden_4
    boite_avec_tt_les_names = dir(hidden_4)

    # Trie les noms par ordre alphabétique grâce à la fonction sorted()
    # trie par défaut dans l'ordre croissantoption reverse=true
    #
    for name in sorted(boite_avec_tt_les_names):

        # Ignore les noms qui commencent par __ grâce à texte.startswith("mot")
        # startswith() → "Est ce que name NE commence PAS par "__" ?"
        if not name.startswith("__"):

            #si oui, tu print les éléments correspondant (les noms sans "__")
            print(name)

# fonction sorted()

# La fonction ne modifie pas l'itérable d'origine,
# elle retourne une nouvelle liste contenant les éléments triés.

# Ordre croissant : Si tu ne spécifies pas d'option,
# sorted() trie les éléments en ordre croissant.

# Si tu veux un tri en ordre décroissant,
# tu peux utiliser le paramètre reverse=True. Cela inverse l'ordre du tri.

# Le paramètre key est une option de trie supplémentaire
# Cela est utile si tu veux trier les éléments selon un critère spécifique,
# comme la longueur des mots (len), ou la deuxième lettre d'une chaîne.
# Pour key=len, cela va trier par longueur de mot et après par ordre croissant.

############################################################################

# Fonction startswith

# La méthode startswith vérifie si une chaîne de caractères commence
# par une sous-chaîne donnée. Elle renvoie True si c'est le cas, sinon False.
# Exemple 1 : "bonjour".startswith("bon") renvoie True
# Exemple 2 : "bonjour".startswith("jour") renvoie False
# On peut aussi vérifier plusieurs débuts possibles avec un tuple :
# Exemple 3 : "bonjour".startswith(("bon", "salut")) renvoie True

