from utils.linear_utils import copie_matrice, copie_vecteur

def gauss_sans_pivot(A, b):
    n = len(A)
    # Création des copies pour ne pas modifier les originaux
    A = copie_matrice(A)
    b = copie_vecteur(b)

    # Triangularisation
    for k in range(n-1):
        if A[k][k] == 0:
            raise ValueError(f"Pivot nul à l'étape {k}. Utilisez la méthode avec pivot.")
        for i in range(k+1, n):
            factor = A[i][k] / A[k][k]
            for j in range(k, n):
                A[i][j] -= factor * A[k][j]
            b[i] -= factor * b[k]

    # Résolution par remontée
    x = [0.0] * n
    for i in range(n-1, -1, -1):
        s = sum(A[i][j] * x[j] for j in range(i+1, n))
        if A[i][i] == 0:
            raise ValueError("Matrice singulière")
        x[i] = (b[i] - s) / A[i][i]
    return x