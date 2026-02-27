def saisir_matrice():
    n = int(input("Ordre de la matrice carrée : "))
    print("Entrez les coefficients ligne par ligne (séparés par des espaces) :")
    A = []
    for i in range(n):
        ligne = list(map(float, input(f"Ligne {i+1} : ").split()))
        if len(ligne) != n:
            raise ValueError("Le nombre de coefficients ne correspond pas à l'ordre.")
        A.append(ligne)
    return A

def saisir_vecteur(n):
    print(f"Entrez les {n} coefficients du second membre (séparés par des espaces) :")
    v = list(map(float, input().split()))
    if len(v) != n:
        raise ValueError("Le nombre de coefficients ne correspond pas.")
    return v