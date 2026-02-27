from utils.linear_utils import resoudre_LU, copie_matrice

def crout(A):
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]

    for i in range(n):
        # Calcul de la colonne i de L (sous la diagonale)
        L[i][i] = 1.0  # diagonale unité
        for j in range(i, n):
            s = sum(L[i][k] * U[k][j] for k in range(i))
            U[i][j] = A[i][j] - s

        for j in range(i+1, n):
            s = sum(L[j][k] * U[k][i] for k in range(i))
            if U[i][i] == 0:
                raise ValueError("Pivot nul dans la factorisation LU")
            L[j][i] = (A[j][i] - s) / U[i][i]

    return L, U