from utils.verifications import verifier_matrice_carree, verifier_tolerance
from utils.linear_utils import copie_matrice

def crout(A, tolerance=1e-12):

    n = verifier_matrice_carree(A)
    tolerance = verifier_tolerance(tolerance)

    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i, n):
            s = sum(L[i][k] * U[k][j] for k in range(i))
            U[i][j] = A[i][j] - s

        if abs(U[i][i]) < tolerance:
            raise ValueError(f"Pivot nul dans la factorisation LU à l'indice ({i},{i}) : |U[{i}][{i}]| = {abs(U[i][i])} < {tolerance}. Matrice singulière.")

        # Calcul de la ligne i de L (en dessous de la diagonale)
        for j in range(i, n):
            if j == i:
                L[j][i] = 1.0  # diagonale unité
            else:
                s = sum(L[j][k] * U[k][i] for k in range(i))
                L[j][i] = (A[j][i] - s) / U[i][i]

    return L, U