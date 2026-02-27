from utils.verifications import verifier_matrice_carree, verifier_tolerance
from utils.linear_utils import copie_matrice

def cholesky(A, tolerance=1e-12):
    n = verifier_matrice_carree(A)
    tolerance = verifier_tolerance(tolerance)

    # Vérifions la symétrie
    for i in range(n):
        for j in range(i, n):
            if abs(A[i][j] - A[j][i]) > tolerance:
                raise ValueError(f"La matrice n'est pas symétrique : A[{i}][{j}] = {A[i][j]}, A[{j}][{i}] = {A[j][i]}, différence = {abs(A[i][j]-A[j][i])} > {tolerance}.")

    L = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i+1):
            s = sum(L[i][k] * L[j][k] for k in range(j))
            if i == j:
                diagonal = A[i][i] - s
                if diagonal <= tolerance:
                    raise ValueError(f"Matrice non définie positive : terme diagonal L[{i}][{i}]^2 = {diagonal} <= {tolerance}.")
                L[i][j] = diagonal ** 0.5
            else:
                if abs(L[j][j]) < tolerance:
                    raise ValueError(f"Pivot nul lors de la factorisation : L[{j}][{j}] = {L[j][j]}.")
                L[i][j] = (A[i][j] - s) / L[j][j]

    return L