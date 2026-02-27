from utils.verifications import verifier_egalite_dimensions, verifier_tolerance
from utils.linear_utils import copie_matrice, copie_vecteur

def gauss_jordan(A, b, tolerance=1e-12):

    n = verifier_egalite_dimensions(A, b)
    tolerance = verifier_tolerance(tolerance)

    A = copie_matrice(A)
    b = copie_vecteur(b)

    for k in range(n):
        # Pivot partiel
        ligne_pivot = max(range(k, n), key=lambda r: abs(A[r][k]))
        valeur_pivot = abs(A[ligne_pivot][k])
        if valeur_pivot < tolerance:
            raise ValueError(f"Matrice singulière : pivot trop petit (|a[{ligne_pivot}][{k}]| = {valeur_pivot} < {tolerance}).")

        if ligne_pivot != k:
            A[k], A[ligne_pivot] = A[ligne_pivot], A[k]
            b[k], b[ligne_pivot] = b[ligne_pivot], b[k]

        # Normalisation de la ligne k
        pivot = A[k][k]
        for j in range(k, n):
            A[k][j] /= pivot
        b[k] /= pivot

        # Élimination dans toutes les autres lignes
        for i in range(n):
            if i != k:
                factor = A[i][k]
                if abs(factor) > tolerance:
                    for j in range(k, n):
                        A[i][j] -= factor * A[k][j]
                    b[i] -= factor * b[k]

    # La solution est b (car la matrice est devenue identité)
    return b