from utils.linear_utils import copie_matrice, copie_vecteur

def gauss_pivot(A, b):
    n = len(A)
    A = copie_matrice(A)
    b = copie_vecteur(b)

    for k in range(n-1):
        # Recherche du pivot maximal dans la colonne k
        pivot_row = max(range(k, n), key=lambda r: abs(A[r][k]))
        if abs(A[pivot_row][k]) < 1e-12:
            raise ValueError("Matrice singulière ou numériquement instable")
        # Échange des lignes si nécessaire
        if pivot_row != k:
            A[k], A[pivot_row] = A[pivot_row], A[k]
            b[k], b[pivot_row] = b[pivot_row], b[k]

        # Élimination
        for i in range(k+1, n):
            factor = A[i][k] / A[k][k]
            for j in range(k, n):
                A[i][j] -= factor * A[k][j]
            b[i] -= factor * b[k]

    # Remontée
    x = [0.0] * n
    for i in range(n-1, -1, -1):
        s = sum(A[i][j] * x[j] for j in range(i+1, n))
        if A[i][i] == 0:
            raise ValueError("Matrice singulière")
        x[i] = (b[i] - s) / A[i][i]
    return x