from utils.verifications import verifier_matrice_carree, verifier_tolerance
from utils.linear_utils import copie_matrice

def crout(A, tol=1e-12):
    """
    Factorisation LU de Crout : A = L * U avec L triangulaire inférieure (diagonale = 1) et U triangulaire supérieure.
    Paramètres :
        A : matrice carrée (liste de listes)
        tol : seuil pour détecter un pivot nul
    Retourne :
        (L, U) : deux matrices (listes de listes)
    Lève une exception si un pivot est nul (matrice singulière).
    """
    n = verifier_matrice_carree(A)
    tol = verifier_tolerance(tol)

    # Initialisation de L et U
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]

    for i in range(n):
        # Calcul de la colonne i de U (ligne i de U)
        for j in range(i, n):
            s = sum(L[i][k] * U[k][j] for k in range(i))
            U[i][j] = A[i][j] - s

        # Vérification du pivot pour éviter une division par zéro plus tard
        if abs(U[i][i]) < tol:
            raise ValueError(f"Pivot nul dans la factorisation LU à l'indice ({i},{i}) : |U[{i}][{i}]| = {abs(U[i][i])} < {tol}. Matrice singulière.")

        # Calcul de la ligne i de L (en dessous de la diagonale)
        for j in range(i, n):
            if j == i:
                L[j][i] = 1.0  # diagonale unité
            else:
                s = sum(L[j][k] * U[k][i] for k in range(i))
                L[j][i] = (A[j][i] - s) / U[i][i]

    return L, U