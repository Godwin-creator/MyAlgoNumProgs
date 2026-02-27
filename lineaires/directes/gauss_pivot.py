from utils.verifications import verifier_egalite_dimensions, verifier_tolerance
from utils.linear_utils import copie_matrice, copie_vecteur

def gauss_pivot(A, b, tolerance=1e-12):
    n = verifier_egalite_dimensions(A, b)
    tolerance = verifier_tolerance(tolerance)

    A = copie_matrice(A)
    b = copie_vecteur(b)

    for k in range(n-1):
        ligne_pivot = max(range(k, n), key=lambda r: abs(A[r][k]))
        valeur_pivot = abs(A[ligne_pivot][k])
        if valeur_pivot < tolerance:
            raise ValueError(f"Matrice singulière ou numériquement instable : pivot trop petit (|a[{ligne_pivot}][{k}]| = {valeur_pivot} < {tolerance}).")

        if ligne_pivot != k:
            A[k], A[ligne_pivot] = A[ligne_pivot], A[k]
            b[k], b[ligne_pivot] = b[ligne_pivot], b[k]

        for i in range(k+1, n):
            factor = A[i][k] / A[k][k]
            for j in range(k+1, n):
                A[i][j] -= factor * A[k][j]
            b[i] -= factor * b[k]

    # Vérification du dernier pivot
    if abs(A[n-1][n-1]) < tolerance:
        raise ValueError("Matrice singulière : dernier pivot nul.")

    # Résolution par remontée
    x = [0.0] * n
    for i in range(n-1, -1, -1):
        s = sum(A[i][j] * x[j] for j in range(i+1, n))
        x[i] = (b[i] - s) / A[i][i]

    return x