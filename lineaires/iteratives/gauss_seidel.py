from utils.verifications import verifier_egalite_dimensions, verifier_tolerance, verifier_iterations, verifier_vecteur
from utils.linear_utils import norme_vecteur, copie_vecteur

def gauss_seidel(A, b, x0=None, tol=1e-6, max_iter=100):
    """
    Méthode de Gauss-Seidel pour résoudre A x = b.
    Paramètres :
        A : matrice carrée (liste de listes)
        b : second membre (liste)
        x0 : vecteur initial (liste, optionnel)
        tol : tolérance sur la variation relative
        max_iter : nombre maximal d'itérations
    Retourne :
        (x, iterations, converged)
    Lève une exception si un élément diagonal est nul.
    """
    n = verifier_egalite_dimensions(A, b)
    tol = verifier_tolerance(tol)
    max_iter = verifier_iterations(max_iter)

    if x0 is None:
        x = [0.0] * n
    else:
        verifier_vecteur(x0, n, "x0")
        x = copie_vecteur(x0)

    # Vérification des diagonales
    for i in range(n):
        if abs(A[i][i]) < 1e-12:
            raise ValueError(f"Élément diagonal A[{i}][{i}] nul ou trop petit : {A[i][i]}. La méthode de Gauss-Seidel ne peut pas s'appliquer.")

    for iteration in range(max_iter):
        x_old = x[:]  # copie pour le calcul de la différence
        for i in range(n):
            s1 = sum(A[i][j] * x[j] for j in range(i))        # valeurs déjà mises à jour
            s2 = sum(A[i][j] * x_old[j] for j in range(i+1, n))  # anciennes valeurs
            x[i] = (b[i] - s1 - s2) / A[i][i]

        diff = norme_vecteur([x[i] - x_old[i] for i in range(n)])
        if diff < tol:
            return x, iteration+1, True

    return x, max_iter, False