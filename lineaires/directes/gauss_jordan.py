from utils.linear_utils import copie_matrice, copie_vecteur

def gauss_jordan(A, b):
    n = len(A)
    A = copie_matrice(A)
    b = copie_vecteur(b)

    for k in range(n):
        # Pivot partiel
        pivot_row = max(range(k, n), key=lambda r: abs(A[r][k]))
        if abs(A[pivot_row][k]) < 1e-12:
            raise ValueError("Matrice singulière")
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
                for j in range(k, n):
                    A[i][j] -= factor * A[k][j]
                b[i] -= factor * b[k]

    # La solution est directement b (car la matrice est devenue identité)
    return b