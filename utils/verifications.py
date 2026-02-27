#Fonctions de vérification des entrées pour les algorithmes numériques.
#Elles lèvent des exceptions avec des messages clairs en cas de problème.

def verifier_matrice(A, nom="A"):
    if not isinstance(A, list):
        raise TypeError(f"{nom} doit être une liste.")
    if not A:
        raise ValueError(f"{nom} ne peut pas être vide.")
    if not all(isinstance(ligne, list) for ligne in A):
        raise TypeError(f"Chaque ligne de {nom} doit être une liste.")

    n_lignes = len(A)
    n_colonnes = len(A[0]) if n_lignes > 0 else 0
    if n_colonnes == 0:
        raise ValueError(f"{nom} a des lignes vides.")

    for i, ligne in enumerate(A):
        if len(ligne) != n_colonnes:
            raise ValueError(
                f"La ligne {i} de {nom} a {len(ligne)} colonnes, mais la première ligne en a {n_colonnes}.")
        for j, val in enumerate(ligne):
            if not isinstance(val, (int, float)):
                raise TypeError(f"L'élément {nom}[{i}][{j}] n'est pas un nombre (type: {type(val).__name__}).")

    return n_lignes, n_colonnes


def verifier_matrice_carree(A, nom="A"):
    n_lignes, n_colonnes = verifier_matrice(A, nom)
    if n_lignes != n_colonnes:
        raise ValueError(f"{nom} doit être carrée : {n_lignes} lignes mais {n_colonnes} colonnes.")
    return n_lignes


def verifier_vecteur(b, taille_attendue=None, nom="b"):
    if not isinstance(b, list):
        raise TypeError(f"{nom} doit être une liste.")
    if not b:
        raise ValueError(f"{nom} ne peut pas être vide.")
    if not all(isinstance(x, (int, float)) for x in b):
        raise TypeError(f"Tous les éléments de {nom} doivent être des nombres.")
    if taille_attendue is not None and len(b) != taille_attendue:
        raise ValueError(f"{nom} doit avoir {taille_attendue} éléments, mais il en a {len(b)}.")
    return len(b)


def verifier_egalite_dimensions(A, b):
    n = verifier_matrice_carree(A)
    m = verifier_vecteur(b, n)
    # n et m sont déjà égaux grâce à la vérification
    return n


def verifier_tolerance(tolerance, nom="tol"):
    #Vérifie que la tolérance est un nombre positif.
    if not isinstance(tolerance, (int, float)):
        raise TypeError(f"{nom} doit être un nombre.")
    if tolerance <= 0:
        raise ValueError(f"{nom} doit être strictement positif.")
    return float(tolerance)


def verifier_iterations(max_iteration, nom="max_iter"):
    #Vérifie que le nombre d'itérations est un entier positif.
    if not isinstance(max_iteration, int):
        raise TypeError(f"{nom} doit être un entier.")
    if max_iteration <= 0:
        raise ValueError(f"{nom} doit être un entier positif.")
    return max_iteration