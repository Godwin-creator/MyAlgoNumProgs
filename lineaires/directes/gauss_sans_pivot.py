from utils.verifications import verifier_egalite_dimensions, verifier_tolerance
from utils.linear_utils import copie_matrice, copie_vecteur

def gauss_sans_pivot(A, b, tolerance=1e-12):

    n = verifier_egalite_dimensions(A, b)
    tolerance = verifier_tolerance(tolerance)

    A = copie_matrice(A)
    b = copie_vecteur(b)

    # Triangularisation
    for k in range(n-1):
        if abs(A[k][k]) < tolerance:
            raise ValueError(f"Pivot nul à l'étape {k} : |a[{k}][{k}]| = {abs(A[k][k])} < {tolerance}. Utilisez la méthode avec pivot.")
        for i in range(k+1, n):
            factor = A[i][k] / A[k][k]
            # Mise à jour de la ligne i à partir de k+1
            for j in range(k+1, n):
                A[i][j] -= factor * A[k][j]
            b[i] -= factor * b[k]
            # Optionnel : A[i][k] = 0.0

    # Vérification du dernier pivot
    if abs(A[n-1][n-1]) < tolerance:
        raise ValueError("Matrice singulière : dernier pivot nul.")

    # Résolution par remontée
    x = [0.0] * n
    for i in range(n-1, -1, -1):
        s = sum(A[i][j] * x[j] for j in range(i+1, n))
        x[i] = (b[i] - s) / A[i][i]

    return x