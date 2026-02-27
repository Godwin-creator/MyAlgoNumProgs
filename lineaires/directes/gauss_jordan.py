from utils.verifications import verifier_egalite_dimensions, verifier_tolerance
from utils.linear_utils import copie_matrice, copie_vecteur

def gauss_jordan(A, b, tol=1e-12):
    """
    Résolution par la méthode de Gauss-Jordan.
    Paramètres :
        A : matrice carrée (liste de listes)
        b : second membre (liste)
        tol : seuil pour considérer un pivot comme nul
    Retourne :
        x : vecteur solution (liste)
    Lève une exception si la matrice est singulière.
    """
    n = verifier_egalite_dimensions(A, b)
    tol = verifier_tolerance(tol)

    A = copie_matrice(A)
    b = copie_vecteur(b)

    for k in range(n):
        # Pivot partiel
        pivot_row = max(range(k, n), key=lambda r: abs(A[r][k]))
        pivot_val = abs(A[pivot_row][k])
        if pivot_val < tol:
            raise ValueError(f"Matrice singulière : pivot trop petit (|a[{pivot_row}][{k}]| = {pivot_val} < {tol}).")

        if pivot_row != k:
            A[k], A[pivot_row] = A[pivot_row], A[k]
            b[k], b[pivot_row] = b[pivot_row], b[k]

        # Normalisation de la ligne k
        pivot = A[k][k]
        for j in range(k, n):
            A[k][j] /= pivot
        b[k] /= pivot

        # Élimination dans toutes les autres lignes
        for i in range(n):
            if i != k:
                factor = A[i][k]
                if abs(factor) > tol:  # Éviter de soustraire pour des valeurs très petites
                    for j in range(k, n):
                        A[i][j] -= factor * A[k][j]
                    b[i] -= factor * b[k]
                # Optionnel : A[i][k] = 0.0

    # La solution est b (car la matrice est devenue identité)
    return b