from utils.verifications import verifier_egalite_dimensions, verifier_tolerance
from utils.linear_utils import copie_matrice, copie_vecteur

def gauss_pivot(A, b, tol=1e-12):
    n = verifier_egalite_dimensions(A, b)
    tol = verifier_tolerance(tol)

    A = copie_matrice(A)
    b = copie_vecteur(b)

    for k in range(n-1):
        pivot_row = max(range(k, n), key=lambda r: abs(A[r][k]))
        pivot_val = abs(A[pivot_row][k])
        if pivot_val < tol:
            raise ValueError(f"Matrice singulière ou numériquement instable : pivot trop petit (|a[{pivot_row}][{k}]| = {pivot_val} < {tol}).")

        if pivot_row != k:
            A[k], A[pivot_row] = A[pivot_row], A[k]
            b[k], b[pivot_row] = b[pivot_row], b[k]

        for i in range(k+1, n):
            factor = A[i][k] / A[k][k]
            for j in range(k+1, n):
                A[i][j] -= factor * A[k][j]
            b[i] -= factor * b[k]

    # Vérification du dernier pivot
    if abs(A[n-1][n-1]) < tol:
        raise ValueError("Matrice singulière : dernier pivot nul.")

    # Résolution par remontée
    x = [0.0] * n
    for i in range(n-1, -1, -1):
        s = sum(A[i][j] * x[j] for j in range(i+1, n))
        x[i] = (b[i] - s) / A[i][i]

    return x