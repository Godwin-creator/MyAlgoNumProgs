from utils.verifications import verifier_matrice_carree, verifier_tolerance
from utils.linear_utils import copie_matrice

def cholesky(A, tol=1e-12):
    """
    Factorisation de Cholesky A = L * L^T pour une matrice symétrique définie positive.
    Paramètres :
        A : matrice carrée symétrique (liste de listes)
        tol : seuil pour détecter une matrice non définie positive
    Retourne :
        L : matrice triangulaire inférieure (liste de listes)
    Lève une exception si la matrice n'est pas symétrique ou pas définie positive.
    """
    n = verifier_matrice_carree(A)
    tol = verifier_tolerance(tol)

    # Vérification de la symétrie
    for i in range(n):
        for j in range(i, n):
            if abs(A[i][j] - A[j][i]) > tol:
                raise ValueError(f"La matrice n'est pas symétrique : A[{i}][{j}] = {A[i][j]}, A[{j}][{i}] = {A[j][i]}, différence = {abs(A[i][j]-A[j][i])} > {tol}.")

    L = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i+1):
            s = sum(L[i][k] * L[j][k] for k in range(j))
            if i == j:
                diag = A[i][i] - s
                if diag <= tol:
                    raise ValueError(f"Matrice non définie positive : terme diagonal L[{i}][{i}]^2 = {diag} <= {tol}.")
                L[i][j] = diag ** 0.5
            else:
                if abs(L[j][j]) < tol:
                    raise ValueError(f"Pivot nul lors de la factorisation : L[{j}][{j}] = {L[j][j]}.")
                L[i][j] = (A[i][j] - s) / L[j][j]

    return L