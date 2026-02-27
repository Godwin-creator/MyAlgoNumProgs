from utils.linear_utils import norme_vecteur, copie_vecteur

def gauss_seidel(A, b, x0=None, tol=1e-6, max_iter=100):
    n = len(A)
    x = copie_vecteur(x0) if x0 else [0.0] * n
    x_old = [0.0] * n

    for iteration in range(max_iter):
        x_old[:] = x[:]  # sauvegarde de l'itération précédente
        for i in range(n):
            s1 = sum(A[i][j] * x[j] for j in range(i))       # valeurs déjà mises à jour
            s2 = sum(A[i][j] * x_old[j] for j in range(i+1, n))  # anciennes
            if A[i][i] == 0:
                raise ValueError("Élément diagonal nul")
            x[i] = (b[i] - s1 - s2) / A[i][i]

        diff = norme_vecteur([x[i] - x_old[i] for i in range(n)])
        if diff < tol:
            return x, iteration+1, True

    return x, max_iter, False