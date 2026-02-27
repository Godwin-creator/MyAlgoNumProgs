from utils.verifications import verifier_egalite_dimensions, verifier_tolerance, verifier_iterations, verifier_vecteur
from utils.linear_utils import norme_vecteur, copie_vecteur

def jacobi(A, b, x0=None, tol=1e-6, max_iter=100):
    """
    Méthode de Jacobi pour résoudre A x = b.
    Paramètres :
        A : matrice carrée (liste de listes)
        b : second membre (liste)
        x0 : vecteur initial (liste, optionnel, par défaut vecteur nul)
        tol : tolérance sur la variation relative
        max_iter : nombre maximal d'itérations
    Retourne :
        (x, iterations, converged) : solution, nombre d'itérations effectuées, booléen de convergence
    Lève une exception si la matrice n'est pas à diagonale dominante (stricte) ? Non, on laisse l'utilisateur juger.
    """
    n = verifier_egalite_dimensions(A, b)
    tol = verifier_tolerance(tol)
    max_iter = verifier_iterations(max_iter)

    if x0 is None:
        x = [0.0] * n
    else:
        verifier_vecteur(x0, n, "x0")
        x = copie_vecteur(x0)

    x_new = [0.0] * n

    # Vérification que les éléments diagonaux ne sont pas nuls
    for i in range(n):
        if abs(A[i][i]) < 1e-12:
            raise ValueError(f"Élément diagonal A[{i}][{i}] nul ou trop petit : {A[i][i]}. La méthode de Jacobi ne peut pas s'appliquer.")

    for iteration in range(max_iter):
        for i in range(n):
            s = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - s) / A[i][i]

        # Calcul de l'erreur relative
        diff = norme_vecteur([x_new[i] - x[i] for i in range(n)])
        if diff < tol:
            return x_new, iteration+1, True

        # Échange des références pour éviter une copie inutile
        x, x_new = x_new, x

    return x, max_iter, False