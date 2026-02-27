from utils.linear_utils import norme_vecteur, copie_vecteur

def jacobi(A, b, x0=None, tol=1e-6, max_iter=100):
    n = len(A)
    x = copie_vecteur(x0) if x0 else [0.0] * n
    x_new = [0.0] * n

    for iteration in range(max_iter):
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            if A[i][i] == 0:
                raise ValueError("Élément diagonal nul")
            x_new[i] = (b[i] - s) / A[i][i]

        # Calcul de l'erreur relative
        diff = norme_vecteur([x_new[i] - x[i] for i in range(n)])
        if diff < tol:
            return x_new, iteration+1, True
        x, x_new = x_new, x  # échange

    return x, max_iter, False