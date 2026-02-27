from utils.verifications import verifier_egalite_dimensions, verifier_tolerance
from utils.linear_utils import copie_matrice, copie_vecteur

def gauss_pivot(A, b, tol=1e-12):
    """
    Résolution par élimination de Gauss avec pivot partiel.
    Paramètres :
        A : matrice carrée (liste de listes)
        b : second membre (liste)
        tol : seuil pour considérer un pivot comme nul (par défaut 1e-12)
    Retourne :
        x : vecteur solution (liste)
    Lève une exception si la matrice est singulière ou mal conditionnée.
    """
    # Vérifications des entrées
    n = verifier_egalite_dimensions(A, b)
    tol = verifier_tolerance(tol)

    # Création des copies pour ne pas modifier les originaux
    A = copie_matrice(A)
    b = copie_vecteur(b)

    # Triangularisation avec pivot partiel
    for k in range(n-1):
        # Recherche du pivot maximal dans la colonne k à partir de la ligne k
        pivot_row = max(range(k, n), key=lambda r: abs(A[r][k]))
        pivot_val = abs(A[pivot_row][k])
        if pivot_val < tol:
            raise ValueError(f"Matrice singulière ou numériquement instable : pivot trop petit (|a[{pivot_row}][{k}]| = {pivot_val} < {tol}).")

        # Échange des lignes si nécessaire
        if pivot_row != k:
            A[k], A[pivot_row] = A[pivot_row], A[k]
            b[k], b[pivot_row] = b[pivot_row], b[k]

        # Élimination
        for i in range(k+1, n):
            factor = A[i][k] / A[k][k]
            # On ne met pas à jour les colonnes avant k (déjà nulles), on peut commencer à k+1 pour optimiser
            for j in range(k+1, n):
                A[i][j] -= factor * A[k][j]
            b[i] -= factor * b[k]
            # A[i][k] n'est pas utilisé ensuite, on peut le laisser ou le mettre à zéro (optionnel)
            # A[i][k] = 0.0  # pour la clarté, mais inutile

    # Vérification du dernier pivot
    if abs(A[n-1][n-1]) < tol:
        raise ValueError("Matrice singulière : dernier pivot nul.")

    # Résolution par remontée (substitution arrière)
    x = [0.0] * n
    for i in range(n-1, -1, -1):
        s = sum(A[i][j] * x[j] for j in range(i+1, n))
        x[i] = (b[i] - s) / A[i][i]

    return x